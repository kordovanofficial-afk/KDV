import type { Register } from 'claude-code'

const PANE = 'kordovan-team'
const TITLE = 'Kordovan team'

type Person = { name: string; seat: string; does: string }
const TEAM: Person[] = [
  { name: 'You', seat: 'Founder', does: 'Approves every hire, spend and live change' },
  { name: 'Claude', seat: 'CEO', does: 'Runs the team, routes your asks, morning brief' },
  { name: 'Hamna', seat: 'CQRO · Quality', does: 'Fact-checks everything before it reaches you' },
  { name: 'Noor', seat: 'CHRO · People', does: 'Hires and reviews agents' },
  { name: 'Sana', seat: 'CRO · Revenue', does: 'Meta ads, offers, sales, conversion' },
  { name: 'Omar', seat: 'CMO · Marketing', does: 'Content, creatives, captions, SEO' },
  { name: 'Creative Dir.', seat: 'under Omar', does: 'Video ad production packages' },
  { name: 'Zain', seat: 'COO · Operations', does: 'Stock, workshop, PostEx, store report' },
  { name: 'Ayesha', seat: 'CFO · Finance', does: 'Real margins, cash, discount floor' },
  { name: '(open)', seat: 'CTO · Tech', does: 'Wave 3: our own apps and automations' },
]

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'team', description: 'Show the Kordovan team beside the chat' })
    void $.ui.open({ id: PANE, title: TITLE })
    return next(e)
  })

  on('command.run', { command: 'team' }, async $ => {
    await $.ui.open({ id: PANE, title: TITLE })
    return { text: 'Team pane opened.' }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text } = $.ui.resolve(e)
    return (
      <Box flexDirection="column">
        <Text dimColor>Name the person when you ask: "Omar, …"</Text>
        {TEAM.map(p => (
          <Box flexDirection="column" marginTop={1}>
            <Text bold>{p.name} <Text dimColor>· {p.seat}</Text></Text>
            <Text dimColor>{p.does}</Text>
          </Box>
        ))}
      </Box>
    )
  })
}
