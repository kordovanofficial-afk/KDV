import type { Register, ToolCallResult } from 'claude-code'

// Higgsfield tools that spend credits.
const HF_SPEND =
  /^mcp__Higgsfield__(generate_|execute_preset|upscale_|outpaint_image|reframe|remove_background|relight_image|motion_control|ai_influencer_generate|ads_studio_generate|dubbing|voice_change|shorts_studio_create|scene_builder_3d_generate|create_voice_from_confirmed_audio)/
// Higgsfield tools that return an exact quote when called with params.get_cost.
const HF_QUOTABLE = /^mcp__Higgsfield__generate_(image|video|audio)(_batch)?$/
const APIFY_RUN = /apify.*__call-actor$/
const META_MONEY = /^mcp__Facebook_Ads_MCP__ads_(activate_entity|update_entity)$/

// Money conversion. Higgsfield's pay-as-you-go card rate (its own pricing data, Oct 30 2026)
// is 18 credits per US dollar. PKR_PER_USD is approximate: edit it when the rate moves.
const CREDITS_PER_USD = 18
const PKR_PER_USD = 280

type Args = Record<string, unknown>

const textOf = (r: ToolCallResult): string => ('text' in r && typeof r.text === 'string' ? r.text : '')

const firstNumber = (text: string, key: string): number | undefined => {
  const m = text.match(new RegExp(`"${key}"\\s*:\\s*([0-9.]+)`))
  return m ? Number(m[1]) : undefined
}

const fmt = (n: number) => (Number.isInteger(n) ? String(n) : n.toFixed(2))

const money = (credits: number) => {
  const usd = credits / CREDITS_PER_USD
  const pkr = Math.round(usd * PKR_PER_USD)
  return `$${usd.toFixed(2)} (about Rs ${pkr.toLocaleString('en-US')})`
}

export const register: Register = on => {
  on('tool.call', async ($, e, next) => {
    const tool = e.tool
    const args = e as unknown as Args
    let question: string | undefined

    if (HF_SPEND.test(tool)) {
      const short = tool.replace('mcp__Higgsfield__', '')
      let cost: number | undefined
      let quoteNote = ''

      if (tool === 'mcp__Higgsfield__ads_studio_generate') {
        try {
          const skip = new Set(['tool', 'tool_use_id', 'agentId', 'requestMeta', 'expected_credits', 'idempotency_key'])
          const quoteArgs = Object.fromEntries(Object.entries(args).filter(([k]) => !skip.has(k)))
          const q = await $.tool.call({ ...quoteArgs, tool: 'mcp__Higgsfield__ads_studio_quote' } as never)
          const c = firstNumber(textOf(q), 'credits') ?? firstNumber(textOf(q), 'total_credits')
          if (c === undefined) throw new Error('no quote')
          cost = c
        } catch {
          quoteNote = 'Higgsfield did not return a quote for this ad batch.'
        }
      } else if (HF_QUOTABLE.test(tool)) {
        try {
          const single = tool.replace(/_batch$/, '')
          const items: Args[] = tool.endsWith('_batch')
            ? ((args.requests as { params?: Args }[] | undefined) ?? []).map(r => r.params ?? {})
            : [args.params as Args]
          let total = 0
          for (const p of items) {
            if (!p || typeof p !== 'object') throw new Error('unquotable params')
            const q = await $.tool.call({ tool: single, params: { ...p, get_cost: true } } as never)
            const c = firstNumber(textOf(q), 'credits')
            if (c === undefined) throw new Error('no quote')
            total += c
          }
          cost = total
        } catch {
          quoteNote = 'Higgsfield did not return a quote for this one.'
        }
      } else {
        quoteNote = 'Higgsfield does not quote this action in advance, so the exact cost is unknown.'
      }

      let balance: number | undefined
      try {
        balance = firstNumber(textOf(await $.tool.call({ tool: 'mcp__Higgsfield__balance' } as never)), 'credits')
      } catch {}

      const costLine = cost !== undefined ? `This costs ${fmt(cost)} credits = ${money(cost)} at the pay-as-you-go card rate.` : quoteNote
      const balLine = balance !== undefined ? ` Balance: ${fmt(balance)} credits.` : ''
      const shortfall =
        cost !== undefined && balance !== undefined && cost > balance
          ? ` You are ${fmt(cost - balance)} credits (${money(cost - balance)}) short, so it will fail unless you top up.`
          : ''
      question = `Higgsfield ${short}: ${costLine}${balLine}${shortfall} Go ahead?`
    } else if (APIFY_RUN.test(tool)) {
      const opts = (args.callOptions ?? {}) as Args
      const cap = typeof opts.maxTotalChargeUsd === 'number' ? opts.maxTotalChargeUsd : undefined
      const actor = typeof args.actor === 'string' ? args.actor : 'an actor'
      question = cap !== undefined
        ? `Apify ${actor}: charged by usage, capped at $${fmt(cap)} for this run. Go ahead?`
        : `Apify ${actor}: charged by usage with no spending cap set on this run. Go ahead?`
    } else if (META_MONEY.test(tool)) {
      const blob = JSON.stringify(args)
      const daily = firstNumber(blob, 'daily_budget')
      const lifetime = firstNumber(blob, 'lifetime_budget')
      const activates = tool.endsWith('activate_entity') || /"status"\s*:\s*"ACTIVE"/.test(blob)
      if (daily !== undefined) question = `Meta ads: sets a daily budget of PKR ${fmt(daily / 100)}. Go ahead?`
      else if (lifetime !== undefined) question = `Meta ads: sets a lifetime budget of PKR ${fmt(lifetime / 100)}. Go ahead?`
      else if (activates) question = 'Meta ads: this makes ads live, so they start spending at their set budgets. Go ahead?'
    }

    if (!question) return next(e)

    let answer = 'No'
    try {
      answer = await $.ui.ask(question, { options: ['Yes', 'No'], header: 'Cost check' })
    } catch {}
    if (answer !== 'Yes') return { deny: `${$.plugin.name}: the user said no to the cost, so it was not run.` }
    return next(e)
  }).catch(($, e, next) =>
    next.called ? next(e) : { deny: `${$.plugin.name}: the cost check failed, so this was not run. Ask again.` },
  )
}
