# Per-jacket data for the jackets shot sheet.
#
# Pulled from Shopify Admin API on 10 Aug 2026 (product_type:"Leather Jacket",
# 30 products). Everything except `lock`, `macro`, `wear` and `scene` is real
# catalogue data — those four are the art direction and are hand-written per
# jacket so no two jackets get the same prompt.
#
# ⚠️ The images could not be opened from this environment (the agent proxy
# refuses cdn.shopify.com), so `style`, `colour` and `lock` are derived from
# the product title, handle and image alt text — all of which name the style
# and the details explicitly. Every prompt is built around "keep the UPLOADED
# product 100% identical", so the garment always comes from the real photo;
# these fields only tell the generator what NOT to smooth away.
#
# fields:
#   pid     Shopify product id
#   name    display name (the real garment, not necessarily the Shopify title)
#   handle  storefront handle
#   price   PKR
#   sex     'm' | 'w'
#   style   biker | cafe racer | bomber | coat
#   colour  written colour, used verbatim in the prompts
#   lock    the details the generator must not lose, invent or tidy
#   macro   what Shot 4 fills the frame with — different for every jacket
#   wear    Shot 2 environment
#   scene   Shot 5 scene
#   warn    optional warning shown on the card

JACKETS = [
    dict(
        pid="8079155134704", name="Rebel — Brown Cafe Racer",
        handle="rebel-mens-brown-cafe-racer-sheepskin-leather-jacket",
        price="33,600", sex="m", style="cafe racer", colour="rich mid-brown",
        lock="stand-up band collar with its snap tab; single straight centre zip; "
             "minimal hardware; clean unbroken chest panels with no extra pockets; "
             "short hip-length hem; soft sheepskin drape",
        macro="the band collar where it meets the centre zip — the collar snap tab, "
              "the zip teeth and the topstitching that runs alongside them",
        wear="a bare whitewashed courtyard wall in flat early-morning light",
        scene="beside a parked vintage cafe-racer motorcycle on a quiet Karachi "
              "back street at first light, the bike softly out of focus behind him",
    ),
    dict(
        pid="8137559245040", name="Hawkeye — Brown Double-Breasted Vintage Coat",
        handle="hawkeye-mens-brown-double-breasted-vintage-coat-s012",
        price="32,000", sex="m", style="coat", colour="warm vintage brown",
        lock="full double-breasted front with BOTH rows of buttons and the correct "
             "button count; wide notch lapels; the waist belt and its buckle; the "
             "long below-the-knee length and the back vent; do not shorten it into "
             "a jacket",
        macro="one lapel edge where the double-breasted overlap folds back — the "
              "button, the buttonhole stitching and the grain running under it",
        wear="the stone doorway of an old colonial-era building, deep shade, "
             "diffused daylight",
        scene="walking a cold, misty Nathiagali hill road in early morning fog, "
              "pine trees soft and grey behind him, coat belted",
        warn="Shopify title says “Rebel | Men's Brown Cafe Racer” but the handle, "
             "every image filename and every alt text say Hawkeye double-breasted "
             "coat. Shoot it as the coat. See the note in the header.",
    ),
    dict(
        pid="8167106674928", name="Urban Rider — Brown Fur-Collar Biker",
        handle="mens-urban-rider-brown-leather-biker-jacket",
        price="35,000", sex="m", style="biker", colour="warm brown",
        lock="the shearling / fur collar — its exact volume, length and colour, "
             "kept as real fibre with visible individual hairs, never rendered as "
             "smooth fabric; asymmetric front zip; the collar must stay attached "
             "and sitting the way it does in the upload",
        macro="the join where the fur collar meets the leather shoulder — "
              "individual fibres against the grain, and the stitch line between them",
        wear="a cold open terrace at dusk, blue-grey sky behind, warm light on him",
        scene="leaning on the rail of a rooftop terrace in Islamabad at dusk, "
              "Margalla hills flattened into haze behind, collar turned up",
    ),
    dict(
        pid="8167109722352", name="The Iconic — Black Sheepskin",
        handle="iconic-mens-black-sheepskin-leather-jacket",
        price="22,000", sex="m", style="biker", colour="true black",
        lock="the clean uninterrupted panels — this is the plainest jacket in the "
             "range and its restraint is the product; do not add pockets, zips, "
             "studs or quilting that are not in the upload; keep the black a true "
             "neutral black, never blue-black or washed grey",
        macro="a plain expanse of the black sheepskin with a single seam crossing "
              "it — pure grain and one line of stitching, nothing else",
        wear="a plain parchment studio corner, soft even daylight",
        scene="hung on a wooden coat rack in a warm hallway beside a pair of dark "
              "leather boots and a folded wool scarf, no model",
    ),
    dict(
        pid="8167112540400", name="Legender Black — Black Biker",
        handle="mens-legender-black-black-leather-biker-jacket",
        price="28,000", sex="m", style="biker", colour="true black",
        lock="asymmetric front zip and its exact diagonal angle; the lapel that "
             "folds back when zipped; every zip pull and snap in the upload, at "
             "the same size and finish",
        macro="the asymmetric zip at chest height — the diagonal run of teeth, the "
              "zip pull hanging, and the leather buckling slightly either side",
        wear="a dim garage doorway, light spilling in from one side",
        scene="astride a stationary motorcycle in an underground car park, warm "
              "sodium light overhead, city night outside the ramp",
    ),
    dict(
        pid="8167115030768", name="The Apex — Black Suede Hybrid Bomber",
        handle="mens-apex-black-plain-suede-bomber-jacket",
        price="32,000", sex="m", style="bomber", colour="black suede",
        lock="SUEDE, not smooth leather — a soft matte nap with visible directional "
             "brushing and absolutely no sheen or specular highlight; the ribbed "
             "knit collar, cuffs and hem; the hybrid panel seams that split suede "
             "from the smoother sections",
        macro="the boundary where the suede nap meets a ribbed knit cuff — brushed "
              "fibres on one side, knit ribs on the other",
        wear="a matte charcoal wall, soft frontal light with no hotspots",
        scene="sitting on the steps of a university block on a cool overcast "
              "afternoon, a canvas bag beside him, flat even winter light",
    ),
    dict(
        pid="8170261512432", name="The Ace — Black MA-1 Bomber",
        handle="mens-ace-black-leather-bomber-jacket",
        price="27,500", sex="m", style="bomber", colour="true black",
        lock="the MA-1 silhouette — blouson body, ribbed knit collar, cuffs and "
             "hem, and the zipped utility pocket on the left sleeve with its flap; "
             "keep the lining colour exactly as it appears in the upload and do "
             "not invent an orange lining if there isn't one",
        macro="the zipped utility pocket on the sleeve — its flap, zip and the "
              "ribbed cuff just below it",
        wear="an airfield-grey concrete wall, hard-edged but diffused daylight",
        scene="standing on a railway platform in early winter light, an empty "
              "track and a blurred waiting train behind him",
    ),
    dict(
        pid="8170262823152", name="Cobalt — Blue Leather Bomber",
        handle="cobalt-mens-blue-leather-bomber-jacket",
        price="27,500", sex="m", style="bomber", colour="deep cobalt blue",
        lock="THE BLUE IS THE PRODUCT — reproduce the exact blue of the upload, "
             "neither shifted toward navy nor toward teal, and never desaturated "
             "toward grey to fit a warm palette; ribbed knit collar, cuffs and hem",
        macro="a fold of the blue leather catching light along its crease, so the "
              "blue reads at both its lightest and its deepest in one frame",
        wear="a warm parchment wall, so the blue is the only colour in frame",
        scene="crossing a rain-damp street at dusk, warm shopfront light behind, "
              "the blue lit clean and unmistakable against the warm background",
    ),
    dict(
        pid="8170264035568", name="The Allaric Alley — Distressed Brown Biker",
        handle="allaric-alley-distressed-brown-leather-biker-jacket",
        price="29,500", sex="m", style="biker", colour="distressed vintage brown",
        lock="THE DISTRESSING IS THE PRODUCT — every rub-through, colour "
             "variation, crease line and worn edge in the upload must survive; "
             "do not clean, even out, re-dye or smooth the finish; the jacket "
             "should look worn-in, not new",
        macro="a rubbed-through elbow or shoulder crease where the brown has worn "
              "back to a lighter tone — the full tonal range in one frame",
        wear="a weathered timber door, warm raking afternoon light",
        scene="leaning against a dusty jeep on a dry track at golden hour, low sun "
              "raking across the worn leather",
    ),
    dict(
        pid="8170267279600", name="The Spy — Brown Leather Bomber",
        handle="mens-spy-brown-leather-bomber-jacket",
        price="28,500", sex="m", style="bomber", colour="warm chocolate brown",
        lock="the bomber silhouette with ribbed collar, cuffs and hem; the front "
             "zip and any chest or welt pockets exactly as they appear; keep the "
             "brown warm and chocolate, not tan and not black-brown",
        macro="the ribbed knit hem where it meets the leather body — the knit "
              "texture, the seam and the leather grain above it",
        wear="a wood-panelled interior wall, warm lamp light from one side",
        scene="in a warm wood-panelled study, one hand in a pocket, a leather "
              "armchair and a low lamp softly behind",
    ),
    dict(
        pid="9018547667184", name="Stryker — Black Zippered-Accent Biker",
        handle="stryker-mens-black-zippered-leather-biker-jacket",
        price="27,000", sex="m", style="biker", colour="true black",
        lock="EVERY zip in the upload — count them and keep them all, at the same "
             "positions, angles, lengths and metal finish; the zipped accent "
             "pockets are what this jacket is; do not simplify the hardware",
        macro="two of the accent zips running at different angles across a black "
              "panel, teeth and pulls sharp, leather softly out of focus behind",
        wear="a dark grey studio corner, a single hard-ish key from the left so "
              "the metal reads",
        scene="under a garage strip-light at night, metal catching the light, the "
              "rest of the frame falling into shadow",
    ),
    dict(
        pid="9018548420848", name="Reacher — Black Ribbed-Collar Biker",
        handle="reacher-mens-black-leather-jacket",
        price="33,600", sex="m", style="biker", colour="true black",
        lock="the ribbed knit collar — the detail the jacket is named for; keep "
             "its exact height, rib spacing and colour, and keep it knit, never "
             "re-rendered as leather; front zip and pocket placement unchanged",
        macro="the ribbed knit collar standing up, its ribs running vertically, "
              "the leather shoulder seam just below it",
        wear="a cold concrete stairwell, daylight from above",
        scene="walking a broad city pavement on a cold bright morning, collar up, "
              "long shadows, crowd blurred well behind him",
    ),
    dict(
        pid="9018549305584", name="Wayne — Black Sheepskin",
        handle="wayne-mens-sheepskin-black-leather-jacket",
        price="25,900", sex="m", style="biker", colour="true black",
        lock="the soft sheepskin drape — this leather falls softly and creases "
             "rather than holding a stiff shape; keep the natural fold lines and "
             "the low sheen exactly as in the upload",
        macro="a soft natural fold in the sheepskin at the waist, the crease "
              "catching a low sheen along its ridge",
        wear="a warm plaster wall in low evening light",
        scene="at a small table outside a tea shop in the evening, a cup on the "
              "table, warm bulb light, street dark behind",
    ),
    dict(
        pid="9018549862640", name="Rockafella — Black Sheepskin Biker",
        handle="rockafella-mens-black-leather-jacket",
        price="29,800", sex="m", style="biker", colour="true black",
        lock="the wide notch lapels that fold back across the chest and the "
             "asymmetric zip beneath them; keep the lapel spread exactly as in "
             "the upload — it is what separates this from the plainer bikers",
        macro="where the folded lapel crosses the chest — the folded edge, the "
              "topstitching along it and the panel seam it meets",
        wear="a deep charcoal studio corner, soft directional key from the left",
        scene="stepping out of a hotel lobby at night, warm interior light behind "
              "him, cool street light on the shoulders",
    ),
    dict(
        pid="9018550157552", name="Durham Waxed — Black Biker, Brown Accents",
        handle="durham-waxed-mens-black-leather-biker-jacket",
        price="26,700", sex="m", style="biker", colour="waxed black with brown accents",
        lock="TWO-TONE — the black body and the brown accent panels, at exactly "
             "the positions and proportions in the upload; and the waxed finish, "
             "which has a low uneven lustre that pools on the high points; do not "
             "flatten it to matte or push it to gloss",
        macro="a seam where a brown accent panel meets the black body, the waxed "
              "lustre visible sitting differently on each of the two leathers",
        wear="a plain parchment wall, soft broad light so the wax lustre reads "
              "without a hotspot",
        scene="beside a stone wall on a wet morning, water beading on the waxed "
              "surface, flat overcast light",
    ),
    dict(
        pid="9018550354160", name="Maverick — Brown Sheepskin",
        handle="maverick-mens-brown-leather-jacket",
        price="32,000", sex="m", style="biker", colour="warm mid-brown",
        lock="the warm mid-brown tone, which must not slide toward tan or toward "
             "burgundy; the soft sheepskin drape; collar shape and zip placement "
             "exactly as uploaded",
        macro="the shoulder seam running down into the sleeve head, grain visible "
              "on both sides of the stitch line",
        wear="a sunlit stone wall, warm late-afternoon light",
        scene="on the steps of an old haveli in the late afternoon, warm stone, "
              "long shadows, one hand resting on a wooden rail",
    ),
    dict(
        pid="9018550583536", name="Alveraz — Black Sheepskin Biker",
        handle="alveraz-mens-black-sheepskin-biker-leather-jacket",
        price="23,000", sex="m", style="biker", colour="true black",
        lock="the slim close-cut fit — this is the leanest cut in the range and "
             "must not be rendered boxy or oversized; every seam line and zip "
             "position as uploaded",
        macro="the waist seam where the body narrows, one line of stitching "
              "curving across the frame",
        wear="a flat mid-grey wall, even frontal light",
        scene="on a narrow book-lined stair in a second-hand bookshop, warm bulb "
              "light, shelves soft behind",
    ),
    dict(
        pid="9018550943984", name="Rodriguez — Claret Quilted Biker",
        handle="rodriguez-mens-quilted-leather-biker-jacket",
        price="26,400", sex="m", style="biker", colour="deep claret / oxblood",
        lock="the CLARET colour — a deep red-brown oxblood, not brown and not "
             "bright red; and the quilted panels, with the exact quilt pattern, "
             "panel positions and stitch spacing of the upload",
        macro="the quilted panel — the raised diamonds or channels, the stitch "
              "lines pulling them in, in deep claret",
        wear="a soft parchment wall, warm broad light so the claret stays red "
              "and does not read brown",
        scene="in a warm restaurant interior at night, a candle out of focus on "
              "the table, the claret lit clearly against dark wood",
    ),
    dict(
        pid="9018551632112", name="Ralph — Dark Brown Zipper Biker",
        handle="ralph-mens-dark-brown-leather-biker-jacket",
        price="24,500", sex="m", style="biker", colour="dark chocolate brown",
        lock="the dark brown, kept clearly brown and not mistaken for black even "
             "in low light; the exposed front and pocket zips with their metal "
             "finish; all zip positions unchanged",
        macro="a pocket zip half-open on the dark brown leather, the teeth "
              "catching light and the grain reading clearly brown",
        wear="a warm cream wall, bright soft light so the brown stays brown",
        scene="beside a parked car at dusk, door just closed, keys in hand, "
              "warm street light picking the brown out of the shadow",
    ),
    dict(
        pid="9018552320240", name="Bohemia — Vintage Brown Sheepskin",
        handle="bohemia-mens-vintage-brown-sheepskin-leather-jacket",
        price="26,100", sex="m", style="biker", colour="vintage antiqued brown",
        lock="the antiqued finish — darker at the seams and creases, lighter "
             "across the panels; that tonal variation is the product and must "
             "not be evened out into one flat brown",
        macro="a seam where the antiquing has darkened the leather right at the "
              "stitch line and lightens away from it",
        wear="an old timber wall in warm low light",
        scene="in a workshop doorway at the end of the day, tools blurred behind, "
              "warm dust in the last of the light",
    ),
    dict(
        pid="9018552680688", name="Alonzo — Brown Sheepskin",
        handle="alonzo-mens-brown-sheepskin-leather-jacket",
        price="26,100", sex="m", style="biker", colour="warm brown",
        lock="the collar shape and how it sits open at the neck; the soft "
             "sheepskin body; keep the brown warm and even, without the antiquing "
             "of the Bohemia",
        macro="the open collar edge at the neck, the folded leather edge and the "
              "topstitching following it",
        wear="a pale linen backdrop, soft window light from the left",
        scene="on a terrace with cane chairs, morning tea on a low table, soft "
              "warm light, the city quiet below",
    ),
    dict(
        pid="9018553073904", name="Vanguard — Black Sheep Leather Biker",
        handle="vanguard-mens-black-leather-biker-jacket",
        price="25,350", sex="m", style="biker", colour="true black",
        lock="the panelled construction — the seam lines that split the body and "
             "sleeves into panels; keep every panel seam where it is, they are "
             "the design; zips and collar unchanged",
        macro="two panel seams meeting at the chest, both stitch lines sharp, "
              "black grain filling the rest of the frame",
        wear="a dark studio corner with a single soft key from above-left",
        scene="on a covered walkway at night, evenly spaced lights receding "
              "behind him, cool architecture, warm skin tone",
    ),
    dict(
        pid="9018553368816", name="Marc Ed — Black Sheepskin Biker",
        handle="marc-ed-mens-black-leather-jacket",
        price="29,400", sex="m", style="biker", colour="true black",
        lock="the collar and its fastening, the front zip line, and the sleeve "
             "zips at the cuff if present in the upload; keep the hardware finish "
             "identical",
        macro="a cuff zip half-open at the wrist, the sleeve leather folding "
              "slightly around it",
        wear="a smooth grey wall, soft even light",
        scene="beside a dark car on a cold night, one hand on the roof, city "
              "lights small and blurred behind",
    ),
    dict(
        pid="9018553598192", name="Sheppard — Black Cafe Racer",
        handle="sheppard-mens-cafe-racer-black-leather-jacket",
        price="24,300", sex="m", style="cafe racer", colour="true black",
        lock="the cafe-racer language — stand-up band collar with snap tab, "
             "straight centre zip, minimal pockets, short hip-length hem; do not "
             "give it biker lapels or an asymmetric zip",
        macro="the snap tab at the throat of the band collar, closed, with the "
              "top of the centre zip just below it",
        wear="a bare concrete wall, hard-edged but diffused light",
        scene="in a motorcycle workshop, a bike on a stand out of focus behind, "
              "warm work-light from one side",
    ),
    dict(
        pid="9018554155248", name="The Waxed Rider — Brown Waxed Sheepskin",
        handle="waxed-rider-mens-brown-leather-jacket",
        price="25,000", sex="m", style="biker", colour="waxed brown",
        lock="the waxed finish — an uneven low lustre that sits brighter on the "
             "creases and high points and duller in the hollows; that unevenness "
             "is the product, do not polish it flat or matte it out",
        macro="a crease running across the waxed brown leather, the wax catching "
              "brighter along the ridge and dulling into the hollow",
        wear="a pale wall in soft broad light so the uneven lustre reads",
        scene="on a wet street after rain, water beading on the waxed shoulders, "
              "reflected light on the pavement",
    ),
    dict(
        pid="9018554646768", name="Desert Voyager — Brown Sheepskin Bomber",
        handle="desert-voyager-mens-brown-sheepskin-leather-bomber-jacket",
        price="32,000", sex="m", style="bomber", colour="warm sand-brown",
        lock="the bomber shape with ribbed collar, cuffs and hem, and the warm "
             "sand-brown tone; keep the ribbing knit and the body soft; do not "
             "let the brown drift grey",
        macro="the ribbed knit cuff gathered at the wrist, the leather sleeve "
              "blousing softly above it",
        wear="a warm sand-toned wall, bright but soft daylight",
        scene="on a dry desert track at golden hour, low sun behind and to the "
              "side, dust in the air, flat open horizon",
    ),
    dict(
        pid="9018555334896", name="Nightfall — Diamond-Quilted Black Biker",
        handle="nightfall-mens-diamond-quilted-black-leather-jacket",
        price="27,500", sex="m", style="biker", colour="true black",
        lock="THE DIAMOND QUILTING — the exact diamond size, angle and stitch "
             "spacing, and the exact panels it appears on (shoulders and/or "
             "sleeves only, never the whole jacket unless the upload says so); "
             "the unquilted panels must stay smooth",
        macro="the diamond quilting set at a slight angle — raised diamonds, the "
              "stitch lines pulling between them, deep shadow in the channels",
        wear="a near-black studio corner, one soft raking key so the quilting "
              "casts its own shadows",
        scene="under a portico at night, overhead light raking across the quilted "
              "shoulders, the rest of the street dark",
    ),
    dict(
        pid="9018555859184", name="Shadow Rider — Black Cafe Racer",
        handle="shadow-rider-mens-black-cafe-racer-leather-jacket",
        price="25,600", sex="m", style="cafe racer", colour="true black",
        lock="band collar, straight centre zip, clean minimal front — the cafe "
             "racer language; do not add lapels, studs or extra pockets; keep the "
             "hem short and the fit close",
        macro="the straight centre zip running vertically through the frame, "
              "teeth sharp, black grain either side",
        wear="a plain dark wall with a single soft key from the right",
        scene="on a hill road at dawn, mist in the valley behind, helmet held at "
              "his side, cold blue light warmed only on him",
    ),
    dict(
        pid="8180111933680", name="Alison — Women's Black Biker",
        handle="alison-black-womens-biker-jacket",
        price="26,000", sex="w", style="biker", colour="true black",
        lock="the women's cut — narrower shoulders, shaped waist, shorter hem "
             "than the men's jackets; the asymmetric zip and the fold-back lapel; "
             "do not render it as a men's jacket on a woman",
        macro="the asymmetric zip crossing the chest at its diagonal, the lapel "
              "folding back above it",
        wear="a warm parchment wall, soft window light from the left",
        scene="on a city street at dusk, warm shopfront light behind, one hand in "
              "a pocket, walking unhurried",
    ),
    dict(
        pid="8180219347184", name="Sinclair — Women's Maroon Bomber",
        handle="bliss-maroon-leather-bomber-women-jacket",
        price="23,000", sex="w", style="bomber", colour="deep maroon",
        lock="THE MAROON — a deep wine red that must not slide to brown, claret "
             "or bright red; the bomber shape with ribbed knit collar, cuffs and "
             "hem; the women's shaped cut",
        macro="the ribbed knit collar in deep maroon, ribs running vertically, "
              "the leather shoulder seam just below",
        wear="a soft cream wall, bright even light so the maroon reads as red",
        scene="in a warm cafe interior in the evening, dark wood and low lamps, "
              "the maroon lit clean against them",
        warn="Renamed by the user from “Alison Black Women's Biker Jacket”. The "
             "SEO title still said “Alison — Black Women's Leather Biker Jacket” "
             "and has been corrected.",
    ),
]
