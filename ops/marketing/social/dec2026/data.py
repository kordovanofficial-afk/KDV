# Kordovan Dec 2026 organic Instagram plan: 12 feed posts + 30 stories. Edit here, run build.py.
# Rules baked in: no coins, no city names, no "workshop", no animal-skin/tobacco words, no faces, no fake scarcity,
# no invented reviews/customers, jackets = top-grain sheepskin, MTO = about 3 weeks, COD NOT on MTO.
BRAND = {"alabaster":"#F7F2EA","espresso":"#241C16","cognac":"#A0623A","tan":"#C08B5C","brass":"#B0894F","stone":"#8B8174","border":"#DDD2C0"}

# ---- FEED (1080x1350, 4:5) ----
# keys: n, date, wd, pillar, title, upload, link, prod, scene, comp, cam, light, pal, tone_i, tone_p, logo, text, cap, tags
FEED = [
dict(n=1,date="Tue 1 Dec",pillar="Proof & detail",title="Look closer: Mocha Mate grain",upload="Mocha Mate (brown) product photo + logo PNG",link="/products/mocha-mate",
 prod="the Mocha Mate leather bifold wallet in brown (approx. #5E3B25), with its outer button pocket and ID window",
 scene="a macro close-up on a worn, honey-coloured walnut desk #8A6A4B with visible wood grain; one folded wallet in the lower two thirds, the stitched edge and button pocket in sharp focus; a blurred steel pen and a white ceramic cup of chai (no steam text) far behind",
 comp="wallet fills about 70% of the frame width, rotated 12° clockwise, placed on the lower-right third; the top-left third stays calm wood and soft blur so the logo can sit there",
 cam="phone macro look, 50 mm equivalent, camera 25 cm from the wallet at 30° above the desk, shallow depth of field: stitching sharp, the far end of the wallet gently soft",
 light="window daylight from the left at 5200 K, soft, with a faint warm bounce from the desk; thin natural shadows under the stitch line, no flash",
 pal="walnut #8A6A4B, leather brown #5E3B25, cream cup #EFE6D8, Alabaster #F7F2EA highlights",
 tone_i="quiet, tactile, confident: a person looked closely at the thing and liked what they saw",
 tone_p="honest everyday leather: durable, slightly rugged, premium without being shiny; grain and stitching are the stars",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied (do not redraw), recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Inter Medium 30 px, Alabaster #F7F2EA, left-aligned at x=70, y=1230: "Look closer."',
 cap="Real leather has a grain you can see and stitching you can feel. Look closer.\nAsli leather ko dekhein, chhoo kar dekhein. Mocha Mate, Rs 3,200. Cash on delivery available. Link bio mein.",
 tags="#kordovan #leatherwallet #realleather #walletformen #handcraftedinpakistan"),
dict(n=2,date="Thu 3 Dec",pillar="In use",title="What fits in the Mocha Mate",upload="Mocha Mate (brown) product photo + logo PNG",link="/products/mocha-mate",
 prod="the Mocha Mate bifold wallet in brown (approx. #5E3B25), shown open",
 scene="a top-down flat-lay on a pale oak table #D8C3A0: the wallet open at the centre with four plain bank cards (no readable numbers, no bank logos), a blank ID-style card with a blurred photo area, two folded Pakistani rupee notes (blurred denominations), a spare house key and a plain black pen beside it",
 comp="strict top-down, wallet at the centre-left filling 55% of the width, items fanned loosely around it with 4–6 cm gaps, a bit of casual asymmetry; 160 px of clear table at the bottom for the line of text",
 cam="top-down 90°, 35 mm equivalent, everything in focus edge to edge, slight natural vignette",
 light="large soft window light from the top-left at 5400 K, gentle diffuse shadows to the bottom-right, no hard flash",
 pal="oak #D8C3A0, leather brown #5E3B25, notes in muted green and violet (blurred), steel #8E9399",
 tone_i="organised, practical, a little satisfying — like a tidy desk before work",
 tone_p="a wallet that holds a real day: cards, cash, ID and a spare key, without bulk",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Espresso #241C16, 90 px wide, top-left at x=70, y=70",
 text='one line in Inter Medium 30 px, Espresso #241C16, centred at y=1270: "Everything you carry. Nothing you don\'t."',
 cap="Cards, cash, ID and a spare key, with room left over. What does your wallet carry?\nCards, cash, CNIC aur chaabi, sab ek jagah. Aap ke wallet mein kya hota hai?",
 tags="#kordovan #whatsinmywallet #everydaycarry #leatherwallet #pakistan"),
dict(n=3,date="Sat 5 Dec",pillar="Gifting & culture",title="Shaadi season: a gift that outlives the photos",upload="Bastion wallet (brown) product photo + logo PNG",link="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet",
 prod="The Bastion distressed leather bifold wallet in brown (approx. #6B4A32)",
 scene="a plain kraft-paper gift box #C9A87A, lid leaning against it, the wallet resting open-faced inside on cream tissue paper #F2E9DA; beside the box a folded embroidered cream-and-gold cloth (soft, out of focus) hinting at a wedding, a brass pen and a blank folded card with no writing",
 comp="box in the lower-centre filling 60% of the width, wallet visible at a 20° angle, top third left empty and softly blurred; no ribbon, no bow",
 cam="eye-level 3/4 view slightly above the box, 50 mm look, shallow depth of field so the wallet and tissue are sharp and the cloth melts away",
 light="warm tungsten-leaning window light 4300 K from the right, soft shadows, a gentle golden feel without glow effects",
 pal="kraft #C9A87A, tissue #F2E9DA, leather #6B4A32, gold thread #B0894F, Espresso #241C16 shadow areas",
 tone_i="warm, family, celebratory but understated: the quiet moment before a wedding",
 tone_p="a considered gift: distressed, characterful leather that gets better with age",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Fraunces Regular 40 px, Alabaster #F7F2EA, centred at y=210: "A gift that outlives the wedding photos."',
 cap="Shaadi season. For the groom, the brother, the father — a wallet that gets better every year.\nShaadi ka mausam. Aise tohfe ke liye jo saalon saath rahe. Link bio mein.",
 tags="#kordovan #shaadiseason #giftideas #leatherwallet #madeinpakistan"),
dict(n=4,date="Tue 8 Dec",pillar="Proof & detail",title="Care: wipe, condition, repeat",upload="any brown leather wallet photo + logo PNG",link="/blogs/news",
 prod="a brown leather bifold wallet (approx. #5E3B25), matching the uploaded photo",
 scene="a clean folded white cotton cloth #F4F1EC, a small round tin of neutral leather balm with its lid off (plain unbranded tin, no label text), and a soft-bristle brush, all on a grey-stone counter #B9B4AC; the wallet lies slightly angled with a fresh sheen on one half and matt on the other, showing the difference honestly",
 comp="L-shaped arrangement: wallet at centre-right, cloth bottom-left, tin top-left corner; clear space at the bottom 200 px",
 cam="top-down 70° slightly angled, 50 mm look, sharp across the wallet and tin",
 light="soft overcast daylight 6000 K from the top, very low contrast, no harsh specular on the leather",
 pal="stone #B9B4AC, cream cloth #F4F1EC, leather #5E3B25, tin steel #A9A39A",
 tone_i="calm, educational, reassuring: care is easy, not a chore",
 tone_p="leather that is meant to be used, wiped and looked after — it lasts",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Espresso #241C16, 90 px wide, top-left at x=70, y=70",
 text='one line in Inter Medium 30 px, Espresso #241C16, centred at y=1260: "Wipe. Condition. Repeat. Twice a year."',
 cap="Looking after leather takes two minutes: wipe with a dry cloth, add a little balm twice a year, keep it out of rain and heat. That's it.\nLeather ki hifazat aasaan hai: khushk kapra, saal mein do baar balm. Bas.",
 tags="#kordovan #leathercare #realleather #leatherwallet #tips"),
dict(n=5,date="Thu 10 Dec",pillar="In use",title="Winter ride: gloves on the handlebar",upload="Men's gloves (brown) product photo + logo PNG",link="/products/durable-mens-leather-gloves-light-brown-kordovan",
 prod="the men's brown sheep-leather winter gloves (approx. #9A6B43) with fleece lining and wrist strap, one glove gripping the handlebar, the other resting on the tank",
 scene="a motorbike handlebar and mirror in cold early-morning mist on an empty road, soft bare trees far behind, faint breath-of-winter haze; the rider is not visible — only the gloved hand and handlebar",
 comp="the gripping glove at the lower-centre filling 45% of the width, wrist strap visible and fastened, empty misty top 35% of the frame",
 cam="low three-quarter angle from the right at handlebar height, 35 mm look, shallow depth of field; glove and grip sharp, road and trees soft",
 light="low winter sunrise 4500 K from behind-left creating a thin rim light on the glove edges, cool blue-grey shadows #6F7C86, natural haze",
 pal="mist grey #C9CED2, glove tan #9A6B43, black handlebar #1C1A18, cold blue shadows #6F7C86",
 tone_i="crisp, early, honest: the first cold morning commute",
 tone_p="warm, grippy, working gloves for Pakistani winters — soft leather that moves with your fingers",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Fraunces Regular 44 px, Alabaster #F7F2EA, centred at y=210: "Cold hands, sorted."',
 cap="Fleece-lined sheep leather, a non-slip palm and an adjustable strap. Rs 1,950. Cash on delivery across Pakistan.\nSardi ki subah, garam haath. Link bio mein.",
 tags="#kordovan #leathergloves #winterpakistan #bikerlife #madeinpakistan"),
dict(n=6,date="Sat 12 Dec",pillar="Trust & people",title="Your parcel, packed with care",upload="Kordovan branded box/mailer photo (or any real parcel photo) + logo PNG",link="/pages/shipping-policy",
 prod="a plain parcel box and tissue paper with a small Kordovan sticker, containing a brown leather wallet (use the uploaded photo exactly for any visible branding)",
 scene="a packing table #D5CBBE with a closed cardboard parcel taped neatly, a roll of brown tape, a pair of scissors, a few sheets of cream tissue, a blank printed address slip (name and address lines blurred, unreadable) and a phone face-down; nothing else",
 comp="parcel centre-right at 55% width, tape and scissors left, address slip lower-left slightly overlapping the parcel; calm space at the bottom for text",
 cam="top-down 60°, 35 mm look, sharp across the parcel and slip",
 light="soft window daylight 5600 K from the left, natural shadows, no flash",
 pal="table #D5CBBE, cardboard #B98B55, tissue #F5EEE2, tape tan #A57A4A",
 tone_i="careful, human, trustworthy: someone packs every order by hand",
 tone_p="the product is protected and arrives clean and on time",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Espresso #241C16, 90 px wide, top-left at x=70, y=70",
 text='one line in Inter Medium 30 px, Espresso #241C16, centred at y=1265: "Packed carefully. Sent across Pakistan."',
 cap="Every order is checked, wrapped and packed before it leaves. Free delivery over Rs 5,500, cash on delivery on wallets, bags and belts.\nHar order dekh kar, lapet kar bheja jata hai.",
 tags="#kordovan #behindthescenes #shoppakistan #cashondelivery #leatherwallet"),
dict(n=7,date="Tue 15 Dec",pillar="Proof & detail",title="Hardware and grain: the Executive briefcase",upload="Executive Leather Briefcase product photo + logo PNG",link="/products/the-executive-leather-briefcase-office-bag",
 prod="The Executive leather briefcase office bag in dark brown (match the uploaded photo exactly), close crop on its flap, stitching and metal clasp",
 scene="the briefcase standing on a charcoal desk #3A3633 beside a closed laptop and a black notebook, a soft window behind; only the upper-front third of the bag is visible, tightly cropped",
 comp="bag corner and clasp placed on the right-third power point; left half shows soft desk and notebook; 150 px empty at the bottom",
 cam="close, slightly low angle 35°, 85 mm look, sharp on the clasp and stitch line, rest softly blurred",
 light="side window light from the left at 5000 K, gentle highlight rolling off the clasp metal, soft shadows",
 pal="charcoal #3A3633, leather brown (match photo), metal #B0894F, paper white #F2F0EC",
 tone_i="focused, professional, quietly powerful",
 tone_p="a serious bag for serious work days: structure, weight and detail",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Fraunces Regular 40 px, Alabaster #F7F2EA, left-aligned at x=70, y=1230: "Built for the long workday."',
 cap="Structure, stitching and a clasp that closes with a click. The Executive office bag with a laptop compartment.\nOffice ke liye mazboot, saaf-suthra bag. Link bio mein.",
 tags="#kordovan #officebag #leatherbriefcase #workstyle #madeinpakistan"),
dict(n=8,date="Thu 17 Dec",pillar="In use",title="Packed for the week: Rastov backpack",upload="The Rastov Backpack product photo + logo PNG",link="/products/rl-the-hilford-backpack",
 prod="The Rastov leather backpack with its flap and buckle closure (match the uploaded photo exactly)",
 scene="a bedroom floor corner at morning: the backpack open flap on a pale rug #E5DDD0, beside it a folded grey hoodie, a paperback, earphones in a small pouch, a water bottle and a charger — a real-life packing flat-lay",
 comp="backpack at the centre-right standing upright at 50% width, items arranged loosely around, shot slightly from above at 40°; clear 200 px at the bottom",
 cam="35 mm look, 40° above, everything sharp, natural tiny lens distortion at the edges",
 light="morning window light from the left at 5300 K, soft realistic shadows, one faint sun patch on the rug",
 pal="rug #E5DDD0, hoodie #8F9399, leather per photo, book spine muted teal #5C7A7E",
 tone_i="relaxed, everyday, aspirational but real",
 tone_p="a leather backpack that carries a normal day — tougher and better-looking each year",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Espresso #241C16, 90 px wide, top-left at x=70, y=70",
 text='one line in Inter Medium 30 px, Espresso #241C16, centred at y=1270: "Packed. Zipped. Gone."',
 cap="Laptop, book, charger, water: the Rastov takes the week in stride.\nPura hafta, ek bag mein. Link bio mein.",
 tags="#kordovan #leatherbackpack #everydaycarry #commute #madeinpakistan"),
dict(n=9,date="Sat 19 Dec",pillar="Gifting & culture",title="Winter jackets: order early",upload="The Iconic black biker jacket product photo + logo PNG",link="/products/iconic-mens-black-sheepskin-leather-jacket",
 prod="The Iconic black leather biker jacket in top-grain sheepskin (match the uploaded photo exactly)",
 scene="the jacket on a plain wooden hanger #A98962 hooked on a dark door #2B2926 in a quiet room; a window with pale winter light on one side; a wool scarf folded on a chair edge in the corner",
 comp="jacket centred filling 70% of the height, a slight natural sag in the shoulders; deep negative space on the left for text",
 cam="straight-on, eye level, 50 mm look, sharp on the leather, soft background",
 light="cool window light 6200 K from the right, a thin warm lamp bounce 3200 K from the lower-left, true-to-life contrast showing leather sheen and grain",
 pal="door #2B2926, hanger #A98962, black leather #151413, scarf muted red #7C3B35",
 tone_i="moody, calm, winter-evening; unhurried confidence",
 tone_p="a jacket that is cut to your size and made to last: serious, not flashy",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='two lines, Fraunces Regular 42 px, Alabaster #F7F2EA, left-aligned at x=70, y=1170: "Made to your size." and "Order early: about 3 weeks to your door."',
 cap="Every jacket is cut after you order, so allow about 3 weeks. Winter is our busiest season, so order early. Paid online, free delivery.\nSardiyon ke liye jacket abhi order karein, taiyar hone mein takreeban 3 hafte.",
 tags="#kordovan #leatherjacket #bikerjacket #winterstyle #madetoorder"),
dict(n=10,date="Tue 22 Dec",pillar="Drops & offers",title="Free delivery over Rs 5,500",upload="Mocha Mate (brown) + men's gloves (brown) product photos + logo PNG",link="/collections/mens-leather-wallets",
 prod="the Mocha Mate brown wallet and the men's brown leather gloves, together",
 scene="a neat flat-lay on a deep-green felt surface #2E4A3F: wallet on the left, gloves crossed on the right, a small plain brown card-board tag with no writing between them, a sprig of dried pine on the bottom edge",
 comp="symmetry broken on purpose: wallet 30% width left-centre, gloves 40% width right-centre, 150 px empty at the top and bottom for text",
 cam="top-down 85°, 50 mm look, tack-sharp",
 light="soft window light from the top-left at 5400 K, short shadows, no flash",
 pal="felt #2E4A3F, leather #5E3B25 and #9A6B43, tag #C9A87A, pine #3D5A4A",
 tone_i="festive but restrained: a thoughtful gift pairing, not a sale poster",
 tone_p="practical pieces people actually use, wrapped up together",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='two lines, centred: "Free delivery over Rs 5,500." in Fraunces Regular 46 px Alabaster #F7F2EA at y=190, and "Wallet + gloves, one parcel." in Inter Medium 30 px Brass #B0894F at y=260',
 cap="Pair a wallet with gloves and your delivery is free, because it is free on every order over Rs 5,500.\nRs 5,500 se zyada ke order par delivery free.",
 tags="#kordovan #freedelivery #giftideas #winteressentials #leatherwallet"),
dict(n=11,date="Thu 24 Dec",pillar="Proof & detail",title="Built to last: the desk, a year on",upload="Mocha Mate (brown) product photo + logo PNG",link="/products/mocha-mate",
 prod="the Mocha Mate brown wallet in everyday use (match the uploaded product shape exactly; show a slightly warm, naturally broken-in finish only on the edges, not heavy ageing)",
 scene="an evening desk with a matte steel wristwatch #B8BCC0, a worn paperback, a green leather notebook (no logo), a brass desk lamp turned on and a cup of tea; the wallet sits in the pool of lamp light",
 comp="wallet at the lamp-lit centre filling 40% width, objects around it at 60–90% opacity of focus, gentle vignette; 200 px empty at the top",
 cam="eye-level 3/4 view, 50 mm look, shallow depth of field, lamp creates soft bokeh at the back",
 light="warm lamp light 3000 K from the right, cool blue ambient 6500 K from the window on the left, high realism",
 pal="lamp amber #E8B77A, notebook green #2F4A3C, leather #5E3B25, steel #B8BCC0",
 tone_i="reflective, end-of-year, quiet pride in good things that last",
 tone_p="a daily companion that looks better after months of use",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Fraunces Regular 44 px, Alabaster #F7F2EA, centred at y=210: "Buy it once. Carry it for years."',
 cap="The best gifts, and the best buys, are the ones you stop thinking about because they just work.\nEk baar kharidein, saalon istemal karein.",
 tags="#kordovan #builttolast #leatherwallet #quality #madeinpakistan"),
dict(n=12,date="Sat 26 Dec",pillar="In use",title="New year, one upgrade: slim wallet",upload="The Razor RFID wallet (black) product photo + logo PNG",link="/products/the-razor-rfid-smart-leather-wallet-kordovan",
 prod="The Razor ultra-slim RFID leather wallet in black (match the uploaded photo exactly)",
 scene="a close side-view of the back pocket of dark indigo jeans #2B3445 (no label or logo visible) with the slim wallet half-slid out; next to it a smoother, thinner outline than a bulky brown wallet shown softly blurred in the background pocket of a second pair of jeans for contrast",
 comp="foreground pocket at the left-centre taking 50% of the width, the wallet at a 15° angle; blurred second pocket at the right-back; empty denim top 25%",
 cam="close-up 35 mm look, slightly low angle, shallow depth of field, real fabric texture visible",
 light="indoor daylight 5500 K from the right, soft shadow, no flash",
 pal="denim #2B3445, black leather #1C1A18, stitching tan #B8956A",
 tone_i="playful, practical, light-hearted — the pocket test",
 tone_p="slim, smart and light: a wallet that disappears in the pocket",
 logo="the uploaded Kordovan horse-head logo PNG exactly as supplied, recoloured Alabaster #F7F2EA, 90 px wide, top-left at x=70, y=70",
 text='one line in Fraunces Regular 44 px, Alabaster #F7F2EA, centred at y=210: "Resolution: carry less."',
 cap="Fewer cards, no bulk, RFID protection. The Razor slides in and out without a bulge.\nNaya saal, halka wallet.",
 tags="#kordovan #slimwallet #rfidwallet #newyear #everydaycarry"),
]

# ---- STORIES (1080x1920, 9:16) ----
# keys: d, wd, type, title, upload, link, prod, scene, comp, cam, light, pal, tone_i, tone_p, text, sticker
STORIES = [
dict(d=1,wd="Tue",type="Welcome",title="December starts",upload="Mocha Mate (brown) photo + logo PNG",link="/products/mocha-mate",prod="the Mocha Mate brown bifold wallet",scene="a wooden desk with a small steaming cup of chai in a clay cup #B98B55 and a window with pale winter sun",comp="wallet low in the frame at y≈1050, 50% width, text zone above",cam="35 mm look, eye level, shallow depth of field",light="soft window light 5200 K from the left",pal="oak #C79A62, clay #B98B55, leather #5E3B25",tone_i="warm, fresh start, cosy",tone_p="a reliable everyday companion",text='"December edit." (Fraunces Bold 80 px, Alabaster #F7F2EA, centred y≈520)',sticker="Link sticker to the Mocha Mate page"),
dict(d=2,wd="Wed",type="Poll",title="Black or brown?",upload="Razor RFID wallet (black) + Razor wallet (brown) photos + logo PNG",link="",prod="two Razor RFID slim wallets, one black and one brown, side by side",scene="a slate-grey surface #5E6368 with a soft shadow gradient",comp="the two wallets stacked diagonally at the centre, filling 55% of the width, leaving clean space for the poll sticker at y≈1250",cam="top-down 80°, 50 mm look",light="soft diffuse light 5600 K from the top",pal="slate #5E6368, black #1C1A18, brown #5E3B25",tone_i="playful, decisive",tone_p="a clean, slim everyday choice",text='"Black or brown?" (Fraunces Bold 76 px, Alabaster #F7F2EA, centred y≈480)',sticker="Poll sticker: Black / Brown"),
dict(d=3,wd="Thu",type="Proof",title="Look closer: stitching",upload="Bastion wallet (brown) photo + logo PNG",link="",prod="the stitched edge of The Bastion distressed brown wallet",scene="a macro close-up of the stitch line and edge paint on rough distressed leather, a walnut surface behind",comp="stitch line runs diagonally across the centre, in focus; soft blur at the corners",cam="macro 60 mm, 20 cm distance, shallow depth of field",light="raking side light 5000 K to show every micro-crease",pal="distressed brown #6B4A32, thread #C9A87A, walnut #8A6A4B",tone_i="intimate, close, tactile",tone_p="real leather: uneven, characterful, honest",text='"Look closer." (Fraunces Bold 80 px, Alabaster #F7F2EA, centred y≈480)',sticker="none"),
dict(d=4,wd="Fri",type="Culture",title="Jummah Mubarak",upload="a brown leather wallet photo + logo PNG",link="",prod="a plain brown leather wallet resting beside a string of wooden prayer beads",scene="a clean white prayer mat edge and a soft morning window; calm and uncluttered",comp="wallet and beads in the lower-centre, large calm space above",cam="top-down 70°, 50 mm look",light="soft morning light 5400 K",pal="white #F4F1EC, wood #8A6A4B, leather #5E3B25",tone_i="peaceful, respectful, quiet",tone_p="present but not the focus",text='"Jummah Mubarak." (Fraunces Bold 76 px, Alabaster #F7F2EA over a soft dark gradient, centred y≈520)',sticker="none"),
dict(d=5,wd="Sat",type="Question",title="What do you carry daily?",upload="Mocha Mate (brown) photo + logo PNG",link="",prod="a brown wallet among everyday-carry items: phone (face-down), keys, a steel watch",scene="a flat-lay on a linen-textured surface #D9D0C2",comp="items arranged in the lower 55% of the frame with the top 40% left plain for the question box",cam="top-down 85°, 35 mm look",light="soft window light from the left 5300 K",pal="linen #D9D0C2, leather #5E3B25, steel #B8BCC0",tone_i="curious, conversational",tone_p="one item in a real daily kit",text='"What do you carry daily?" (Fraunces Bold 72 px, Espresso #241C16, centred y≈480)',sticker="Question sticker"),
dict(d=6,wd="Sun",type="Product",title="Cold hands, sorted",upload="Men's gloves (brown) photo + logo PNG",link="/products/durable-mens-leather-gloves-light-brown-kordovan",prod="the men's brown sheep-leather gloves",scene="a misty winter morning bench near a park #A9AFB2 with faint breath-of-cold haze",comp="gloves laid together, fingers pointing up-right, at y≈1000 filling 45% width",cam="35 mm look, 30° above",light="cool morning light 6000 K with a faint warm rim",pal="mist #C9CED2, glove tan #9A6B43, bench #6B6258",tone_i="cold, crisp, early",tone_p="warm, soft, ready for winter",text='"Cold hands, sorted." (Fraunces Bold 76 px, Alabaster #F7F2EA, y≈520)',sticker="Link sticker to the gloves page"),
dict(d=7,wd="Mon",type="Product",title="Carry your Monday",upload="Executive Briefcase photo + logo PNG",link="/products/the-executive-leather-briefcase-office-bag",prod="The Executive leather briefcase office bag",scene="an office floor beside a desk, a closed laptop on the desk edge, pale morning light",comp="bag standing at the centre, filling 55% of the width, handle up",cam="eye level, 50 mm look",light="soft side window light 5300 K",pal="floor #CFC7BB, desk #8F8A83, leather per photo",tone_i="focused, professional",tone_p="structured and serious",text='"Carry your Monday." (Fraunces Bold 76 px, Espresso #241C16, y≈480)',sticker="Link sticker to the Executive page"),
dict(d=8,wd="Tue",type="FAQ",title="Is it real leather?",upload="three plain leather swatches (or any wallet) photo + logo PNG",link="/blogs/news/real-vs-fake-leather-how-to-check",prod="three small genuine leather swatches in brown, tan and black next to a wallet",scene="a clean stone counter #CFCAC2",comp="swatches fanned in a row at the centre, wallet behind them, top zone free",cam="top-down 70°, 50 mm look",light="soft diffuse light 5600 K",pal="stone #CFCAC2, browns #5E3B25 #9A6B43, black #1C1A18",tone_i="clear, no-nonsense, honest",tone_p="proof of material",text='two lines: "Is it real leather?" (Fraunces Bold 72 px Espresso #241C16 y≈470) and "Yes. Handcrafted in Pakistan." (Inter Medium 36 px Espresso y≈590)',sticker="Link sticker to the real-vs-fake guide"),
dict(d=9,wd="Wed",type="Product",title="The pocket test",upload="Razor RFID (black) photo + logo PNG",link="/products/the-razor-rfid-smart-leather-wallet-kordovan",prod="The Razor slim black RFID wallet half out of a back jeans pocket",scene="dark indigo jeans #2B3445 close crop, no label",comp="pocket at the centre, wallet at 15° tilt, 55% width",cam="close 35 mm, slightly low",light="indoor daylight 5500 K",pal="denim #2B3445, black #1C1A18",tone_i="light, playful",tone_p="slim to the point of disappearing",text='"Pocket test: passed." (Fraunces Bold 72 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the Razor page"),
dict(d=10,wd="Thu",type="Trust",title="Delivery day",upload="a parcel photo + logo PNG",link="/pages/shipping-policy",prod="a plain cardboard parcel with a small sticker",scene="a front doorstep with a soft concrete step #BDB7AE and a pot plant at the edge, daylight",comp="parcel centred low at y≈1100 filling 45% width",cam="slight high angle 30°, 35 mm look",light="overcast daylight 6000 K",pal="concrete #BDB7AE, cardboard #B98B55, plant #4B6B50",tone_i="friendly, everyday, expected",tone_p="arrives safe and on time",text='"Free delivery over Rs 5,500." (Fraunces Bold 66 px, Espresso #241C16, y≈480)',sticker="Link sticker to the shipping page"),
dict(d=11,wd="Fri",type="Care",title="Wipe. Condition. Repeat.",upload="a brown wallet photo + logo PNG",link="",prod="a brown leather wallet being wiped with a white cloth",scene="a stone counter, a small plain tin of balm, hands cropped at the wrist",comp="wallet and hand in the centre, 55% width",cam="top-down 65°, 50 mm look",light="soft daylight 5800 K",pal="stone #B9B4AC, cream #F4F1EC, leather #5E3B25",tone_i="calm, instructive",tone_p="easy to look after",text='"Wipe. Condition. Repeat." (Fraunces Bold 72 px, Espresso #241C16, y≈480)',sticker="none"),
dict(d=12,wd="Sat",type="Culture",title="Shaadi season, sorted",upload="Bastion wallet (brown) photo + logo PNG",link="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet",prod="The Bastion brown wallet next to a man's wrist in a crisp white cuff with a cufflink and steel watch, cropped at the chest down with NO head or face",scene="a dressing-room counter with soft warm light and a hanging sherwani blurred in the back",comp="wrist and wallet lower-centre, 55% width",cam="close 50 mm look, shallow depth of field",light="warm 4000 K light from the left",pal="cuff white #F4F1EC, gold #B0894F, leather #6B4A32",tone_i="festive, refined, a bit emotional",tone_p="a groom-ready accessory",text='"Shaadi season, sorted." (Fraunces Bold 72 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the Bastion page"),
dict(d=13,wd="Sun",type="Poll",title="Bifold or slim?",upload="Mocha Mate + Razor photos + logo PNG",link="",prod="a brown bifold wallet and a black slim wallet, side by side",scene="a pale oak table #D8C3A0",comp="two wallets at the centre-left and centre-right, equal size, poll space at y≈1250",cam="top-down 80°, 50 mm look",light="soft diffuse light 5500 K",pal="oak #D8C3A0, brown #5E3B25, black #1C1A18",tone_i="light, fun",tone_p="two honest options",text='"Bifold or slim?" (Fraunces Bold 76 px, Espresso #241C16, y≈480)',sticker="Poll sticker: Bifold / Slim"),
dict(d=14,wd="Mon",type="Product",title="Commute-ready",upload="The Rastov Backpack photo + logo PNG",link="/products/rl-the-hilford-backpack",prod="The Rastov leather backpack on a cafe chair",scene="a quiet cafe window seat, a mug on the table, daylight",comp="backpack centred, 50% width",cam="eye-level 35 mm",light="window light 5400 K",pal="chair #6B6258, table #C9B79B, leather per photo",tone_i="urban, easy",tone_p="a practical leather backpack",text='"Commute-ready." (Fraunces Bold 76 px, Espresso #241C16, y≈470)',sticker="Link sticker to the Rastov page"),
dict(d=15,wd="Tue",type="Trust",title="Packing day",upload="a parcel/tissue photo + logo PNG",link="",prod="a leather wallet being wrapped in cream tissue, hands cropped at the wrist",scene="a packing table #D5CBBE with tape and a plain box",comp="hands and wallet at the centre, 55% width",cam="top-down 65°, 35 mm look",light="soft daylight 5600 K",pal="table #D5CBBE, tissue #F5EEE2, leather #5E3B25",tone_i="careful, human",tone_p="protected and neat",text='"Your order, wrapped by hand." (Fraunces Bold 66 px, Espresso #241C16, y≈470)',sticker="none"),
dict(d=16,wd="Wed",type="Product",title="Winter jackets: order early",upload="The Iconic jacket photo + logo PNG",link="/products/iconic-mens-black-sheepskin-leather-jacket",prod="The Iconic black leather biker jacket on a wooden hanger",scene="a dark door #2B2926 and window light",comp="jacket centred, 70% of the height",cam="straight-on 50 mm look",light="cool window light 6200 K",pal="door #2B2926, black leather #151413",tone_i="moody, calm",tone_p="serious winter leather",text='two lines: "Made to your size." (Fraunces Bold 70 px Alabaster #F7F2EA y≈470) and "Order early: about 3 weeks to your door." (Inter Medium 34 px Alabaster y≈580)',sticker="Link sticker to the Iconic page"),
dict(d=17,wd="Thu",type="Product",title="RFID protected",upload="Kodo Vertical 2.0 photo + logo PNG",link="/products/kodo-vertical-2-0",prod="the Kodo Vertical 2.0 RFID slim leather wallet with its pull strap",scene="a clean graphite surface #3C3F43",comp="wallet standing slightly angled, strap pulled out, 50% width",cam="close 50 mm look",light="soft side light 5200 K",pal="graphite #3C3F43, leather per photo",tone_i="smart, modern",tone_p="slim and protected",text='"RFID protected. Pull-strap access." (Fraunces Bold 66 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the Kodo page"),
dict(d=18,wd="Fri",type="Mood",title="Friday chai",upload="Mocha Mate photo + logo PNG",link="",prod="the Mocha Mate brown wallet next to a cup of chai",scene="a rooftop ledge at dusk with soft city lights blurred far away (no identifiable landmarks)",comp="wallet and cup at the lower-centre",cam="35 mm look",light="dusk blue-orange 3800 K",pal="dusk #E8B77A / #5F6F8C, leather #5E3B25",tone_i="relaxed, cosy",tone_p="a daily companion",text='"Friday, slowed down." (Fraunces Bold 70 px, Alabaster #F7F2EA, y≈480)',sticker="none"),
dict(d=19,wd="Sat",type="Question",title="What should we show next?",upload="wallet + belt + gloves photos + logo PNG",link="",prod="a wallet, a belt and a pair of gloves in a neat row",scene="a pale oak table #D8C3A0",comp="three items in a row in the lower half, question space above",cam="top-down 75°, 35 mm look",light="soft daylight 5400 K",pal="oak #D8C3A0, browns",tone_i="inviting, curious",tone_p="a small range",text='"Which one next?" (Fraunces Bold 72 px, Espresso #241C16, y≈470)',sticker="Question sticker"),
dict(d=20,wd="Sun",type="Gifting",title="Abbu ke liye",upload="Bastion wallet photo + logo PNG",link="/products/the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet",prod="a brown wallet in an open kraft box with cream tissue and a blank tag",scene="a warm table by a window",comp="box centred at y≈1100, 55% width",cam="top-down 70°",light="warm window light 4400 K",pal="kraft #C9A87A, leather #6B4A32",tone_i="warm, family",tone_p="a considered gift",text='"Abbu ke liye." (Fraunces Bold 76 px, Alabaster #F7F2EA over a soft dark gradient, y≈480)',sticker="Link sticker to the Bastion page"),
dict(d=21,wd="Mon",type="Product",title="Road-ready",upload="Truckkr zip wallet photo + logo PNG",link="/products/the-truckkr-bi-fold",prod="the Truckkr zip bifold wallet in a hand resting on a car steering wheel, hand cropped at the wrist",scene="a car interior with a blurred road ahead, no logos",comp="hand and wallet low-centre, 50% width",cam="close 35 mm look",light="daylight through the windscreen 5600 K",pal="dash #2B2926, leather per photo",tone_i="grounded, practical",tone_p="a secure zip wallet",text='"Road-ready." (Fraunces Bold 76 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the Truckkr page"),
dict(d=22,wd="Tue",type="Offer",title="Free delivery over Rs 5,500",upload="wallet + gloves photos + logo PNG",link="/collections/mens-leather-wallets",prod="a brown wallet and a pair of brown gloves",scene="a deep-green felt surface #2E4A3F",comp="wallet and gloves at the lower-centre, clean space above",cam="top-down 85°",light="soft light 5400 K",pal="felt #2E4A3F, leather browns",tone_i="festive but restrained",tone_p="useful pieces",text='"Free delivery over Rs 5,500." (Fraunces Bold 68 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the wallets page"),
dict(d=23,wd="Wed",type="Proof",title="Hardware close-up",upload="Executive Briefcase photo + logo PNG",link="",prod="the clasp and stitching of The Executive briefcase",scene="a macro on its flap and clasp, a soft charcoal blur behind",comp="clasp on the centre-right",cam="macro 85 mm look",light="raking light 5000 K",pal="charcoal #3A3633, metal #B0894F",tone_i="precise, premium",tone_p="detail you can feel",text='"Details." (Fraunces Bold 80 px, Alabaster #F7F2EA, y≈480)',sticker="none"),
dict(d=24,wd="Thu",type="Poll",title="Gloves: brown or black?",upload="men's brown gloves + black gloves photos + logo PNG",link="",prod="two pairs of men's leather gloves, one brown and one black",scene="a pale stone bench #CFCAC2 with soft mist",comp="gloves crossed at the centre, poll space at y≈1250",cam="top-down 70°",light="cool soft light 6000 K",pal="stone #CFCAC2, browns, black",tone_i="playful",tone_p="winter basics",text='"Brown or black?" (Fraunces Bold 76 px, Espresso #241C16, y≈470)',sticker="Poll sticker: Brown / Black"),
dict(d=25,wd="Fri",type="Culture",title="Quaid-e-Azam Day",upload="a brown wallet photo + logo PNG",link="",prod="a plain brown wallet",scene="a deep green and white soft-gradient background #1F4D3A to #F4F1EC with a small crescent-and-star paper cutout as a subtle prop (no flags, no text)",comp="wallet at the lower-centre, 45% width",cam="top-down 70°",light="soft light 5500 K",pal="green #1F4D3A, white #F4F1EC, leather #5E3B25",tone_i="proud, dignified",tone_p="made in Pakistan",text='"Made in Pakistan. Carried with pride." (Fraunces Bold 64 px, Alabaster #F7F2EA, y≈480)',sticker="none"),
dict(d=26,wd="Sat",type="Product",title="One upgrade for 2027",upload="Razor RFID photo + logo PNG",link="/products/the-razor-rfid-smart-leather-wallet-kordovan",prod="The Razor black slim wallet beside a fat worn-out wallet shown softly blurred",scene="a clean white desk #F4F1EC",comp="slim wallet sharp at the centre-left, the bulky one softly blurred at the right",cam="top-down 60°",light="soft light 5600 K",pal="white #F4F1EC, black #1C1A18",tone_i="light, witty",tone_p="slim vs bulky",text='"One upgrade for 2027." (Fraunces Bold 70 px, Espresso #241C16, y≈470)',sticker="Link sticker to the Razor page"),
dict(d=27,wd="Sun",type="FAQ",title="Cash on delivery?",upload="a parcel photo + logo PNG",link="/pages/shipping-policy",prod="a plain parcel being handed over at a door, hands cropped at the wrist",scene="a front door and a soft hallway",comp="parcel at the centre",cam="eye-level 35 mm",light="daylight 5600 K",pal="door #7A6A58, cardboard #B98B55",tone_i="easy, trusting",tone_p="simple and safe",text='two lines: "Cash on delivery?" (Fraunces Bold 70 px Espresso #241C16 y≈470) and "Yes, on wallets, bags and belts." (Inter Medium 34 px Espresso y≈580)',sticker="Link sticker to the shipping page"),
dict(d=28,wd="Mon",type="Product",title="Make an entrance",upload="Clifford cowboy hat (rustic brown) photo + logo PNG",link="/products/kordovans-clifford-cowboy-hat-rustic-brown",prod="the Clifford brown leather cowboy hat on a wooden stand",scene="a dark wood shelf #3A2D22 with a single warm lamp",comp="hat centred at y≈1000, 55% width",cam="eye-level 50 mm look",light="warm lamp 3200 K",pal="wood #3A2D22, leather per photo",tone_i="bold, a little cinematic",tone_p="statement leather",text='"Make an entrance." (Fraunces Bold 76 px, Alabaster #F7F2EA, y≈480)',sticker="Link sticker to the Clifford page"),
dict(d=29,wd="Tue",type="Poll",title="2027: what's your carry?",upload="wallet, belt and gloves photos + logo PNG",link="",prod="a wallet, a belt and a bag handle in a neat flat-lay",scene="a pale oak table #D8C3A0",comp="items low in the frame, poll space at y≈1250",cam="top-down 75°",light="soft light 5400 K",pal="oak #D8C3A0, browns",tone_i="forward-looking, friendly",tone_p="a small kit",text='"2027 carry: wallet, belt or bag?" (Fraunces Bold 66 px, Espresso #241C16, y≈470)',sticker="Poll sticker: Wallet / Belt / Bag"),
dict(d=30,wd="Wed",type="Thanks",title="Thank you, Pakistan",upload="wallet, belt, gloves and a bag photos + logo PNG",link="",prod="a wallet, a belt, gloves and a small bag arranged together",scene="a warm wooden table #8A6A4B",comp="items in a loose circle at the lower-centre",cam="top-down 70°",light="warm light 4500 K",pal="wood #8A6A4B, leather browns",tone_i="grateful, warm",tone_p="a family of products",text='two lines: "Thank you, Pakistan." (Fraunces Bold 76 px Alabaster #F7F2EA y≈470) and "See you in 2027." (Inter Medium 36 px Brass #B0894F y≈590)',sticker="none"),
]

# ===================== REVISIONS Nov 24 (after CMO / CQRO / Alex review) =====================
def _f(n): return next(p for p in FEED if p["n"] == n)
def _s(d): return next(s for s in STORIES if s["d"] == d)

# F4 care wording (matches live copy)
p = _f(4); p["text"] = p["text"].replace("Wipe. Condition. Repeat. Twice a year.", "Wipe. Condition. Repeat. Every few months.")
p["cap"] = p["cap"].replace("add a little balm twice a year", "add a little balm every few months").replace("saal mein do baar balm", "kuch mahine baad balm")
# F5 gloves: both gloves laid on the parked bike, no COD claim
p = _f(5)
p["prod"] = "the men's brown sheep-leather winter gloves (approx. #9A6B43) with fleece lining and wrist strap, the pair laid side by side"
p["scene"] = "a parked motorbike in cold early-morning mist on an empty road: the pair of gloves rests on the seat and fuel tank, wrist straps visible, soft bare trees far behind, faint winter haze; no rider"
p["comp"] = "the gloves at the lower-centre filling 45% of the width, fingers pointing up-right; empty misty top 35% of the frame"
p["cap"] = "Fleece-lined sheep leather, a non-slip palm and an adjustable strap. Rs 1,950. Delivery across Pakistan.\nSardi ki subah, garam haath. Link bio mein."
# F6 packing: only what we can prove + real-photo option
p = _f(6); p["cap"] = "Packed carefully before it leaves. Free delivery over Rs 5,500.\nHar order ehtiyat se pack hota hai."
p["real_option"] = "OPTIONAL: if Ahsan can take a real phone photo of a real parcel being packed, use that instead of this image."
# F8 Rastov out of stock -> Venture Pack
p = _f(8)
p.update(title="Light bag, full day: Venture sling", upload="Venture Pack product photo + logo PNG", link="/products/tp-venture-pack",
 prod="the Venture Pack genuine leather cross-body sling bag (match the uploaded photo exactly)",
 scene="a bedroom floor corner at morning: the sling bag on a pale rug #E5DDD0 beside a folded grey hoodie, a phone (face-down), earphones in a small pouch, a bunch of keys, sunglasses and a pocket notebook, a real-life packing flat-lay",
 comp="the bag at the centre-right at 45% width, items arranged loosely around it, shot from above at 40°; clear 200 px at the bottom")
p["text"] = 'one line in Inter Medium 30 px, Espresso #241C16, centred at y=1270: "Light bag. Full day."'
p["cap"] = "Phone, keys, cards and a notebook: the Venture sling carries the day, hands-free.\nHalka bag, poora din. Link bio mein."
# F9 jackets: reason beside the lead time
p = _f(9)
p["text"] = 'two lines, Fraunces Regular 42 px, Alabaster #F7F2EA, left-aligned at x=70, y=1170: "Made to your size." and "Cut for you. About 3 weeks to your door."'
p["cap"] = "Every jacket is cut for you after you order, so allow about 3 weeks. Winter is our busiest season, so order early. Paid online, free delivery over Rs 5,500.\nSardiyon ke liye jacket abhi order karein: aap ke naap par kat kar, takreeban 3 hafte."
# F10 price truth: two wallets (Rs 3,200 + Rs 2,450 > Rs 5,500)
p = _f(10)
p.update(title="Free delivery over Rs 5,500: two wallets", upload="Mocha Mate (brown) + The Razor (black) product photos + logo PNG", link="/collections/mens-leather-wallets",
 prod="the Mocha Mate brown bifold wallet and The Razor black slim wallet, side by side")
p["scene"] = "a neat flat-lay on a deep-green felt surface #2E4A3F: the two wallets side by side, a small plain brown card-board tag with no writing between them, a sprig of dried pine on the bottom edge"
p["comp"] = "the two wallets each about 35% of the width, left and right of centre, slightly different angles; 150 px empty at the top and bottom for text"
p["text"] = 'two lines, centred: "Free delivery over Rs 5,500." in Fraunces Regular 46 px Alabaster #F7F2EA at y=190, and "Two wallets, one parcel." in Inter Medium 30 px Brass #B0894F at y=260'
p["cap"] = "Delivery is free on every order over Rs 5,500, and two wallets are enough to get there.\nRs 5,500 se zyada ke order par delivery free."
# F11 no 'a year on' proof claim
p = _f(11)
p["title"] = "Buy it once: the evening desk"
p["prod"] = "the Mocha Mate brown wallet exactly as photographed (new, no ageing, no fake wear)"
# F12 drop the second pocket
p = _f(12)
p["scene"] = "a close side-view of the back pocket of dark indigo jeans #2B3445 (no label or logo visible) with the slim black wallet half-slid out, a few stitch details of the denim visible"
p["comp"] = "the pocket at the left-centre taking 55% of the width, the wallet at a 15° angle; plain denim top 25%"

# ---- Stories ----
def real(d, brief):
    s = _s(d); s["real"] = brief
real(2,  "Photograph one black and one brown wallet (Razor RFID) side by side on a plain light surface by a window, top-down. Keep it casual, not styled.")
real(3,  "Phone macro, 10-15 cm away, daylight: the stitch line and edge of a real Bastion wallet. Tap to focus on the stitching.")
real(5,  "Your own everyday-carry on your desk: phone, keys, watch and your wallet. One quick top-down snap, leave the top 40% of the frame plain.")
real(8,  "Close-up of a real wallet's cut edge and grain next to the product card, daylight. No props.")
real(10, "A real parcel on your doorstep or desk, daylight, one snap from slightly above.")
real(11, "Your own wallet being wiped with a dry cloth (hand cropped at the wrist), daylight, top-down.")
real(13, "A brown bifold (Mocha Mate) and a black slim wallet (Razor) side by side on a table, top-down.")
real(15, "Ahsan packing a real order: hands, tissue and box only (no faces, no customer names or addresses visible).")
real(19, "A wallet, a belt and a pair of gloves in a row on a store counter, top-down.")
real(24, "Brown gloves and black gloves crossed on a bench or table, top-down, daylight.")
real(27, "A real parcel being handed over at a door: hands and parcel only, no faces, no address visible.")
_s(8)["text"]  = 'two lines: "Is it real leather?" (Fraunces Bold 72 px Espresso #241C16 y≈470) and "Our wallets: genuine leather, handcrafted in Pakistan." (Inter Medium 34 px Espresso y≈590)'
_s(10)["text"] = '"Free delivery over Rs 5,500." (Fraunces Bold 66 px, Espresso #241C16, y≈480)'
_s(15)["text"] = '"Packed carefully." (Fraunces Bold 70 px, Espresso #241C16, y≈470)'
_s(27)["text"] = 'two lines: "Cash on delivery?" (Fraunces Bold 70 px Espresso #241C16 y≈470) and "Yes, except made-to-order jackets and shoes." (Inter Medium 32 px Espresso y≈580)'
_s(11)["text"] = '"Wipe. Condition. Repeat." (Fraunces Bold 72 px, Espresso #241C16, y≈480)'
_s(1)["text"]  = '"Warm December. Real leather." (Fraunces Bold 72 px, Alabaster #F7F2EA, centred y≈520)'
s = _s(4); s.update(upload="Kordovan logo PNG only", prod="NONE: this image has no product", scene="a bowl of plain dates on a white linen cloth, a soft morning window, calm and uncluttered", comp="the bowl at the lower-centre, 40% width, large calm space above", noprod=True,
 tone_p="not applicable: a pure greeting", pal="white #F4F1EC, dates #4A2F1E, wood #8A6A4B")
s = _s(9); s.update(title="Up to 20 notes, zero bulk", upload="The Money Clip photo + logo PNG", link="/products/the-money-clip-minimal-wallet",
 prod="The Money Clip crazy horse leather money clip wallet holding a small fold of notes (blurred denominations)", scene="a clean oak desk #D8C3A0 and a soft window", comp="wallet at the centre-left at 55% width, a pen beside it",
 text='"Up to 20 notes. Zero bulk." (Fraunces Bold 68 px, Espresso #241C16, y≈480)', sticker="Link sticker to the Money Clip page")
s = _s(14); s.update(upload="CEO Executive Office Bag photo + logo PNG", link="/products/the-executive-ceo-office-bag", prod="the CEO Executive Office Bag (premium glazed leather; match the uploaded photo)")
s = _s(16); s["text"] = 'two lines: "Made to your size." (Fraunces Bold 70 px Alabaster #F7F2EA y≈470) and "Cut for you. About 3 weeks to your door." (Inter Medium 34 px Alabaster y≈580)'
s = _s(17); s.update(title="Slim and vertical: The Luke", upload="The Luke wallet photo + logo PNG", link="/products/the-luke-minimalist-wallet",
 prod="The Luke minimalist vertical leather wallet", scene="a clean graphite surface #3C3F43", text='"Slim. Vertical. Sorted." (Fraunces Bold 72 px, Alabaster #F7F2EA, y≈480)', sticker="Link sticker to The Luke page")
s = _s(22); s.update(title="Why 3 weeks?", upload="The Spy jacket photo + logo PNG", link="/products/mens-spy-brown-leather-bomber-jacket", type="FAQ",
 prod="the sleeve and shoulder of The Spy brown leather bomber jacket on a wooden hanger", scene="a dark door #2B2926 with a pale window light, close crop on the sleeve cuff and shoulder seam",
 comp="the shoulder and sleeve diagonal across the centre, 60% width", cam="close 50 mm look, shallow depth of field", light="cool window light 6200 K", pal="door #2B2926, leather per photo",
 tone_i="calm, honest, explanatory", tone_p="a jacket cut for one customer",
 text='two lines: "Why 3 weeks?" (Fraunces Bold 76 px Alabaster #F7F2EA y≈470) and "Because each jacket is cut for you." (Inter Medium 34 px Alabaster y≈590)', sticker="Link sticker to The Spy page")
s = _s(23); s.update(title="Weekend, sorted", upload="Forester 3-in-1 photo + logo PNG", link="/products/the-forester-backpack-duffle-bag", type="Product",
 prod="the Forester 3-in-1 leather duffle & backpack", scene="a hallway floor by a door with a folded jacket beside it", comp="bag centred, 55% width", cam="eye-level 35 mm", light="soft daylight 5400 K", pal="floor #CFC7BB, leather per photo",
 tone_i="easy, ready to go", tone_p="a roomy leather travel bag", text='"Weekend, sorted." (Fraunces Bold 76 px, Espresso #241C16, y≈480)', sticker="Link sticker to the Forester page")
s = _s(25); s.update(scene="a plain deep green to white soft gradient #1F4D3A to #F4F1EC, nothing else in the background", pal="green #1F4D3A, white #F4F1EC, leather #5E3B25")
s = _s(29); s.update(title="Soft where it counts", type="Product", upload="Men's gloves (black) photo + logo PNG", link="/products/durable-mens-leather-gloves-black-kordovan",
 prod="the men's black sheep-leather gloves, one turned to show the fleece lining", scene="a dark slate surface #3C3F43 with a soft light", comp="gloves at the lower-centre, 55% width",
 cam="close 50 mm look", light="soft side light 5200 K", pal="slate #3C3F43, black #1C1A18, fleece cream #E9DFCB", tone_i="warm, tactile", tone_p="soft, warm and well made",
 text='"Soft where it counts." (Fraunces Bold 72 px, Alabaster #F7F2EA, y≈480)', sticker="Link sticker to the gloves page")
