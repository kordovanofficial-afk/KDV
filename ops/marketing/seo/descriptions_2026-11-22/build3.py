import json, re
exec(open('build2.py').read().split('\nP = {}\n')[0])
CARE['sheep']=SHEEP
P={}
CLIF = lambda col, sizes: ("<p>The Clifford is a classic western cowboy hat in genuine leather with a lightweight build, so you can wear it all day without noticing it. It tops off jeans, a leather jacket or a winter outfit, for road trips, horse riding, golf or a day outdoors.</p>"
 "<h3>Details</h3>" + ul(["100% genuine leather","Lightweight for all-day comfort","Classic western shape with a shaped brim", f"Colour: {col}", f"Sizes: {sizes}"]) +
 "<h3>How to choose your size</h3><p>Measure around your head just above the ears and eyebrows. Between two sizes, pick the larger one, or message us your measurement on WhatsApp and we will tell you which size to order.</p>")
P["copy-of-kordovans-premium-leather-western-cowboy-hat-rustic-maroon"] = ("smooth", CLIF("Faded Black","S, M, L and XL (23 inches and above)") + "<p>A verified buyer called it top quality, very light and a perfect fit.</p>",
 [("Faded Black or Rustic Brown?","Faded Black is the darker, sharper look; Rustic Brown is the warmer, classic western shade.")])
P["kordovans-clifford-cowboy-hat-rustic-brown"] = ("smooth", CLIF("Rustic Brown","S, M, L, XL (23 inches and above) and XXL (24 inches and above)"),
 [("Do you have large sizes?","Yes. The Rustic Brown comes up to XXL, for heads 24 inches and above."),("Faded Black or Rustic Brown?","Rustic Brown is the warmer, classic western shade; Faded Black is the darker, sharper look.")])
P["kodo-vertical-2-0"] = ("smooth",
 "<p>The KODO Vertical 2.0 is a slim, vertical smart wallet in premium top-grain leather with RFID protection. A pull strap brings your most-used cards up in one move, and a front slip pocket keeps cash within reach.</p>"
 "<h3>What it carries</h3>" + ul(["Pull-strap mechanism for quick card access","Additional card slots","Front slip pocket for cash","RFID protection for contactless cards","Soft suede-lined interior","Colours: Brown and Black"]) +
 "<h3>Who it is for</h3><p>For professionals, minimalists and travellers who want a front-pocket wallet that stays slim and organised.</p>",
 [("What does the pull strap do?","Pull the strap and your cards rise out together, so you can pick the one you need without digging.")])
P["copy-of-mens-leather-fanny-pack"] = ("sheep",
 "<p>Carry your essentials securely and hands-free. This unisex fanny pack in premium sheep leather has a place for your phone, keys, wallet and tissues, plus a hidden back pocket for cash or a passport.</p>"
 "<h3>What it carries</h3>" + ul(["One large main zip compartment","2 front pockets","Hidden rear zip pocket for valuables","Adjustable strap with an easy-fasten clasp","Wear it on the waist or across the body","Measures 14.5\" L x 5.5\" H","Colours: Brown and Black"]) +
 "<h3>Who it is for</h3><p>For travellers, bikers, shoppers and anyone who wants their hands free in a crowd. Rated 4.5 stars by verified buyers.</p>",
 [("Can I wear it across my chest?","Yes. Lengthen the strap and wear it as a cross-body sling, or shorten it for the waist.")])
P["tp-natural-milled-leather-dopp-kit"] = ("smooth",
 "<p>A leather dopp kit for the modern traveller. It keeps your grooming essentials and toiletries organised in natural milled leather that develops a rich patina over time, telling the story of your travels.</p>"
 "<h3>Details</h3>" + ul(["Natural milled premium leather","Compartments for grooming essentials, toiletries and travel necessities","Compact yet roomy: fits in your luggage without bulk","Brass hardware and YKK zips","Colours: Black, Brown and Tan"]) +
 "<h3>Who it is for</h3><p>For weekend getaways, business trips and Umrah travel, and a thoughtful gift for a man who travels.</p>",
 [("Will it leak if a bottle opens?","It is leather, not a waterproof liner, so keep liquids capped or in a small zip bag inside.")])
P["the-ripper-case-by-kordovan"] = ("smooth",
 "<p>No more crushed packs in your pocket. The Ripper Case is a dual-compartment leather cigarette case in genuine cow leather that protects your cigarette box and keeps your lighter right beside it.</p>"
 "<h3>Details</h3>" + ul(["Genuine cow leather","Fits a standard-size cigarette box","Separate lighter slot","Durable, sleek design","Colours: Black, Tan and Brown"]) +
 "<h3>Who it is for</h3><p>For smokers who want something smarter than a crushed pack, and a practical gift.</p>",
 [("Will a king-size pack fit?","It fits a standard-size box. For other sizes, message us on WhatsApp first.")])
P["copy-of-natural-oil-tanned-leather-casual-belt-rustic-brown"] = ("smooth",
 "<p>The Rider Jeans Belt is a vintage-style belt in 100% genuine leather with a single-prong buckle in a metallic finish. It is the easy, everyday belt for jeans and casual trousers.</p>"
 "<h3>Details</h3>" + ul(["Pit-tanned, oil-treated cowhide","Single-prong buckle with a metallic finish","Vintage look that suits jeans and chinos","Free size: can be cut down and screwed back to fit any waist"]) +
 "<h3>Who it is for</h3><p>For work, weekends and travel, and anyone who wants a belt that looks better with every wear.</p>",
 [BELT_FAQ])
P["tp-the-nova-weaved-leather-wallet-clutch"] = ("smooth",
 "<p>Elegance you can weave into any day. The Nova is a women's clutch and wallet with an exquisite handwoven leather exterior, a piece that moves easily from work to a dinner party to a weekend out.</p>"
 "<h3>What it carries</h3>" + ul(["Multiple compartments for cash, cards and essentials","Zipped pocket for small valuables","Secure magnetic closure","Premium handwoven leather with a distinctive texture","Colours: Black, Blue, Tan and Brown"]) +
 "<h3>Who it is for</h3><p>For women who want a wallet that doubles as an evening clutch, and an elegant gift for weddings, birthdays and Eid.</p>",
 [("Will a phone fit inside?","It is built as a wallet and clutch for cards, cash and essentials. Message us your phone model on WhatsApp and we will confirm.")])
P["premium-saffiano-leather-wallet"] = ("smooth",
 "<p>Saffiano is the leather of boardrooms: a fine cross-hatched matte texture that reads as quiet luxury from across the table. This modern bifold pairs it with a classic Kordovan logo plaque and a distinctive angular edge.</p>"
 "<h3>What it carries</h3>" + ul(["Large interior bill slot backed by discreet security slots","Transparent ID window","Interior card slots","Matte saffiano finish with signature cross-hatch grain","Angular edge detail and KORDOVAN logo plaque","Colours: Emerald Green and Midnight Black"]) +
 "<h3>Which colour?</h3><p><strong>Emerald Green</strong> is the statement; <strong>Midnight Black</strong> is the executive default.</p>",
 [("Does saffiano scratch easily?","No. The cross-hatch finish is one of the most scratch-resistant leather surfaces, which is why it stays sharp for office use.")])
P["the-money-clip-minimal-wallet"] = ("crazy",
 "<p>Minimal on the outside, magnetic on the inside. The Money Clip is a slim wallet in fine Crazy Horse cow leather with a strong built-in magnetic clip that keeps your notes locked in place: no fumbling, no bulk.</p>"
 "<h3>What it carries</h3>" + ul(["Magnetic money clip that holds up to 20 notes","5 card slots","Centre slot for notes or receipts","Compact: 3.2\" x 4.8\"","100% genuine Crazy Horse cow leather"]) +
 "<h3>Who it is for</h3><p>For front-pocket carriers who want cash and cards in the slimmest possible piece. Rated 5 stars by 9 verified buyers.</p>",
 [("Will the magnet damage my cards?","The clip is for notes. Keep cards in the card slots, away from the magnet, as you would with any magnetic clip.")])
P["the-luke-minimalist-wallet"] = ("smooth",
 "<p>A wallet that carries more by standing tall. The Luke is a vertical billfold in full-grain cow leather that fits 6 to 8 cards and up to 20 notes into a profile slimmer than most standard wallets.</p>"
 "<h3>What it carries</h3>" + ul(["6 to 8 cards","Up to 20 notes","Centre vertical slot for notes or receipts","Hand-stitched seams","Compact: 3.2\" x 4.3\", for formal or casual wear"]) +
 "<h3>Who it is for</h3><p>For men who want a slim, distinctive wallet that reads as a statement piece, not a generic fold. Rated 4.7 stars by 6 verified buyers.</p>",
 [("Vertical or bifold?","A vertical wallet sits slimmer in a front or shirt pocket; a bifold suits a back trouser pocket.")])
P["sheppard-wallet"] = ("sheep",
 "<p>Stylish, functional and soft to the touch. The Sheppard is cut from supple sheep leather and has a button pocket that keeps small essentials secure: an easy everyday wallet that stays slim while carrying more than it looks.</p>"
 "<h3>What it carries</h3>" + ul(["9 card slots","2 ID windows with snap buttons","2 bill slots for folded notes","Button pocket for small essentials","Soft, lightweight sheep leather"]) +
 "<h3>Who it is for</h3><p>For men who want a light, organised wallet at an everyday price.</p>",
 [("What goes in the button pocket?","Small essentials such as a SIM tool, a folded receipt or a spare key.")])
P["the-armour-dual-mobile-wallet-with-notepad"] = ("smooth",
 "<p>When one piece has to hold everything, the Armour answers. This long-format genuine cow leather wallet is really an organiser: two exterior phone slots, a built-in reading-glasses case and a notepad pocket with a pen loop, plus the card slots and ID window you would expect.</p>"
 "<h3>What it carries</h3>" + ul(["Two exterior mobile phone slots","Built-in reading-glasses case","Notepad pocket and pen loop","Interior card slots and ID window","100% genuine cow leather, long format","Colour: Brown"]) +
 "<h3>Who it is for</h3><p>For those who leave the house with more than cards: two phones, glasses and notes, carried as a single piece. A thoughtful gift for fathers and business owners.</p>",
 [("Will two phones fit?","It has two exterior phone slots sized for standard smartphones. Message us your phone models on WhatsApp if they are very large.")])
NOTE_FOR={"copy-of-mens-leather-fanny-pack"}
out={}
for h,(care,body,qs) in P.items():
    html=body+CARE[care]+faq(qs)+STD+(NOTE if h in NOTE_FOR else "")
    txt=re.sub("<[^>]+>"," ",html).lower()
    for bad in ["coin","karachi","workshop","hand-cut","limited stock","loose change","rs 6","order yours today"]:
        assert bad not in txt,(h,bad)
    out[h]={"html":html,"words":len(txt.split())}
json.dump(out,open('batch3.json','w'),indent=1)
for h,v in out.items(): print(v['words'],h)
