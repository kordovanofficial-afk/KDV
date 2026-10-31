# Role brief: Chief Marketing Officer (CMO)

Requisition: wave 1, raised by the CEO, Oct 31 2026. Written by the CHRO (Noor Rehman). Status: SOURCED, interview-ready, pending CEO review.

## Seat and level
- **Executive (C-level).** Reports to the **CEO**.
- **Direct report at hire:** **Creative Director** (existing `.claude/agents/ad-director.md`). ⚠️ Its prompt carries dead rules (see "Conflicts" below). The CEO must decide before it takes CMO direction.
- **Planned reports, opened on evidence across two consecutive weekly reviews:**
  - **Social & Community Director**: opens if DM/comment response time misses target two weeks running, or the content calendar slips by more than 2 posts/week.
  - **Organic Search Director**: opens if the GSC/blog/Merchant Center backlog (e.g. refreshing the jacket article, Merchant Center Diagnostics) sits untouched for 2 weeks.

## Mission
Build demand that costs nothing per click: brand, social content, community and organic search, turned into surviving revenue.

## Responsibilities (end to end)
- Brand and positioning: Quiet Heritage voice (`docs/brand/BRAND_MOODBOARD.md`).
- Content engine for IG / FB / Threads / TikTok / YouTube: calendar, captions, briefs to the Creative Director, and photo direction for Ahsan.
- Community: comment and DM replies, the keyword auto-reply library, and WhatsApp scripts. Order-status answers are checked with the COO.
- Organic search: blog, collection editorial, GSC monitoring, Merchant Center free listings.
- Supplies the creative for CRO promotions and ads.

## KPIs (baseline from CLAUDE.md, with dates)
| KPI | Source | Baseline |
|---|---|---|
| Organic + social surviving revenue | Shopify channel attribution | **Organic search PKR 193,224 surviving in Aug 2026** (Sep 4). Social organic: **no baseline**, needs a pull. chatgpt.com sent 3 orders Oct 11–24 |
| Non-brand search clicks | GSC `["query"]`, brand excluded | **Not measured yet**, needs a pull. Context: the blog was 9.1% of impressions and 6.4% of clicks before Sep 6. The jacket article earned 463 clicks Jun 8–Sep 4 |
| Content shipped vs plan | Calendar vs live posts | **No calendar exists**, so the baseline is 0 planned |
| DM response time | Meta Business Suite inbox (free) | **No baseline**. Ahsan to report the current typical time |

## RACI
| Activity | CMO | CRO | CQRO | CTO (CEO until wave 3) | COO (CEO until wave 2) | Founder / Ahsan |
|---|---|---|---|---|---|---|
| Creative for ads and promos | **R** | A (offer, spend) | R (check) | — | — | Founder approves (L2) |
| Organic posts and captions | **A/R** | I | R (check) | — | — | Founder approves (L2) |
| DM/comment replies and library | **A/R** | I | R (check) | R (automation) | C (order status) | Founder approves the library. Ahsan sends |
| Blog, collection SEO, Merchant Center | **A/R** | C (conversion) | R | — | — | Founder approves (L2) |
| PDP copy and imagery | **R** | A (conversion) | R | R (template) | — | Founder approves (L2) |
| Product photos | **A** (direction) | I | — | — | — | Ahsan shoots |

## Tools (least privilege)
- Read, Glob, Grep, Write, Edit (drafts on the `claude/*` branch).
- WebSearch (verifying competitor and market facts for blog content).
- **Read** live data: Shopify GraphQL queries, GSC. **No publishing, posting or Shopify write tools at hire.** Every post and DM is sent by a human after approval.
- No Bash.

## Must never
- Mention Karachi in new content. Say "our workshop".
- Invent reviews, ratings, testimonials, customer quotes, stock counts or "X sold".
- Promise COD, a delivery time or a price that is not in current CLAUDE.md or live Shopify data.
- Generate footage that functions as evidence of the real product (the `ad-director` integrity rule).
- Use exclamation marks, fake urgency or discount voice. Recommend a paid scheduler or app.
- Post, reply or publish without approval.

## Human counterparts
**Founder** (approves). **Ahsan** (photos, WhatsApp, store-side DMs).

## Conflicts for the CEO (not resolved quietly)
`.claude/agents/ad-director.md` still instructs *"Book with 50%, pay the rest to the rider"* (dead since Sep 4 2026), *"made to order in Karachi"* (breaks the Oct 25 rule) and *"free delivery nationwide"* (wrong: the threshold is Rs 5,500). `ops/ADS_PLAYBOOK_PK.md` §6 still says free delivery ≥ PKR 2,500 and "COD first". Both need correcting before the CMO briefs creative.

## Why now
Organic search produced 51% of Meta's August output at 0% of the spend. Social content, the 11.11 and Black Friday creative, and DM handling have no owner today. The Founder is doing all of it inside 6 hours a day.
