#!/usr/bin/env bash
# Assembles the seven paste-ready image prompts from the locked blocks.
# Edit a block here and every scene stays consistent — that is the whole point.
set -euo pipefail
cd "$(dirname "$0")"; mkdir -p prompts

ENV_BLOCK="in a small family leather workshop in Malir Cantt, Karachi — whitewashed plaster walls with a pale sage-green painted dado along the lower half, a grey polished-concrete floor, brown paper jacket patterns hung on nails, rolled hides stacked on open wooden shelving, an old black cast-iron industrial sewing machine with worn gold lettering, a grey steel almirah deep in the background, a single clear cutting-chai glass at the edge of the bench, hard warm Karachi sunlight entering through a high iron-grilled window on the frame left and falling in one clean shaft with fine dust suspended in it, a warm brass work lamp just out of frame right lifting the shadows, the room ordered and cared-for, a professional craft studio and not a factory floor"

GRADE="palette built on cognac brown and saddle tan leather against warm alabaster cream, parchment, walnut and aged antique brass with a single muted sage accent, warm high-contrast natural light, fine 35mm film grain, soft highlight roll-off, deep espresso shadows with absolutely no blue or teal in them, tactile close photography that makes the grain of the leather readable, unstyled editorial documentary look, shot on a full-frame camera"

NEG="no text, no graphics, no watermark, no logo, no lettering, no signage, no clutter, no plastic, no modern office, not a factory production line"

MAN="the hands and forearms of a Pakistani craftsman in his late thirties, warm brown skin, working hands with short clean nails and visible callus, no watch and no rings, wearing a plain solid-colour cotton shalwar kameez with the sleeves rolled to the elbow"

w(){ printf '%s, %s, %s, %s\n' "$1" "$ENV_BLOCK" "$GRADE" "$NEG" > "prompts/scene$2.txt"; }

w "A high three-quarter view looking down onto an empty scarred dark walnut leather workbench holding one rolled hide of cognac brown full-grain sheepskin, a folded brown paper jacket pattern, a stick of white tailor's chalk and a pair of heavy steel shears, arranged with generous space between them, no jacket and no person anywhere in frame, 35mm framing" 1

w "$MAN, drawing a long white chalk line along the edge of a brown paper pattern laid flat on a sheet of cognac brown full-grain sheepskin, the chalk held like a pencil, the hide filling most of the frame with its grain clearly visible, camera looking straight down from close above, 50mm framing" 2

w "Cut panels of cognac brown full-grain sheepskin arranged flat on the dark walnut workbench in the unmistakable shape of a jacket — two front panels, one back panel, two sleeves — with the brown paper pattern pushed to the edge of frame and the heavy steel shears resting beside it, camera directly overhead, no hands and no person in frame, 35mm framing" 3

w "$MAN, guiding two panels of cognac brown sheepskin under the needle of an old black cast-iron industrial sewing machine with worn gold lettering, the needle caught mid-stitch with a line of even stitching running back toward the camera, camera low and close beside the machine bed at needle height, 50mm framing with shallow depth of field" 4

w "$MAN, setting an antique-brass zip into the front edge of a part-finished cognac brown sheepskin jacket, quilted alabaster cream viscose lining turned back and visible beneath it, camera close and slightly above looking down the length of the zip, 85mm macro framing with shallow depth of field" 5

w "A finished cognac brown full-grain sheepskin biker jacket hanging on a broad wooden hanger from a plain iron rail, shoulders settled and sleeves hanging straight, the sunlit shaft catching one shoulder and the grain readable across the chest, the workbench soft and out of focus behind it, camera at chest height straight on, no hands and no person in frame, 50mm framing" 6

# Scene 7 deliberately swaps the environment block: the doorway replaces the window as the light source.
printf '%s, %s, %s, %s\n' \
  "A Pakistani man in his early thirties with warm brown skin and a neatly trimmed beard, seen from the collarbone down only with his face out of frame above the top edge, wearing the finished cognac brown sheepskin biker jacket over a plain charcoal t-shirt and dark indigo jeans, half turned away and walking toward a bright open doorway, camera at chest height behind him, 35mm framing" \
  "in a small family leather workshop in Malir Cantt, Karachi with whitewashed plaster walls and a pale sage-green painted dado, brown paper jacket patterns hung on nails and rolled hides on open wooden shelving soft behind him, hard warm Karachi daylight flaring through the open doorway ahead and rim-lighting his shoulders, fine dust suspended in the air" \
  "$GRADE" "$NEG" > prompts/scene7.txt

echo "wrote $(ls prompts/*.txt | wc -l) prompts"
wc -w prompts/*.txt | head -8
