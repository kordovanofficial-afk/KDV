# Kordovan teaser (15s, 9:16)

HyperFrames project (skills in `.claude/skills/hyperframes*`). Footage + fonts + gsap live in `assets/` (not committed, ~12MB):
run `prep.sh` from a folder that has `src/IMG_1481.MOV` + `src/IMG_1485.MOV` (recover from git history: `git show <commit>:mocha-mate/originals/IMG_1485.MOV`) and `../fonts/`, then copy gsap.min.js (npm pack gsap@3.14.2) into `assets/`.
Render: `npx hyperframes@0.8.195 render --quality delivery --output Kordovan_Teaser_15s.mp4`.
