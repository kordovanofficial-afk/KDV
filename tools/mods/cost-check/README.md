# cost-check (Claude Code mod)

Before any action that spends money in a connected app, this mod stops the call, shows the cost and asks Yes or No.

- **Higgsfield:** any credit-spending tool (image, video, audio, upscale, presets, ads studio, voice). For image, video and
  audio generations it gets Higgsfield's exact quote first and shows your current balance. Other actions say the cost
  is not quoted in advance.
- **Apify:** actor runs, showing the spending cap set on the run (or that none is set).
- **Meta ads:** budget changes (shown in PKR) and anything that makes ads live.

"No", or closing the question, cancels the action. If the check itself fails, the action is blocked, never run unasked.

Install in a new session: copy this folder to `~/.claude/dev-mods/<session-id>/cost-check/`, or run Claude Code with
`--plugin-dir tools/mods/cost-check`.
