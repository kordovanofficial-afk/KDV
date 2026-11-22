import json, re, sys
exec(open('build.py').read().split('P = {}')[0].replace('OUT = sys.argv[1]',''))
NOTE = '<p><em>Real leather varies a little from piece to piece. Please read our <a href="/pages/product-disclaimer">product note</a> before ordering.</em></p>'
SHEEP = "<h3>Care</h3><p>Sheep leather is soft and light. Keep it away from long soaks, let it dry naturally at room temperature if it gets wet, and wipe it with a dry cloth. A little leather conditioner once a season keeps it supple.</p>"
VEGAN = "<h3>Delivery, payment and care</h3><p>The Diva is made from vegan leather (microfibre), not animal leather: it is waterproof, light and can be wiped clean with a damp cloth. Cash on delivery is available across Pakistan and delivery is free on orders over Rs 5,500. Questions about colour or size? Message us on WhatsApp at 0333 2601161.</p>"
GL = lambda c: ("<p>Leather winter gloves that keep your hands warm and still let you grip. Genuine sheep leather on the back, a stretch spandex palm for a close fit, and a soft fleece lining against the cold.</p>"
 "<h3>Details</h3>" + ul(["Genuine sheep leather with a stretch spandex palm","Soft stretch fleece lining for warmth","Non-slip palm patch for a secure grip on the steering wheel or handlebar","Adjustable wrist strap","Sizes S, M, L, XL and 2XL", f"Colour: {c}"]) +
 "<h3>Who it is for</h3><p>For winter drives and bike rides, early-morning commutes and northern trips. They make an easy winter gift, and pair well with a leather cap to reach free delivery over Rs 5,500.</p>")
P = {}
P["the-maverik-laptop-bag"] = ("smooth",
 "<p>The Maverik is our best-selling laptop bag: a slim, structured office bag in premium glazed cow leather with a smooth, polished surface and natural lustre. It carries a laptop, documents and the small things of a working day, and still looks sharp in a meeting.</p>"
 "<h3>What it carries</h3>" + ul(["1 padded laptop compartment for laptops up to 14.5 inches","3 small organiser slots for pens, cards and cables","1 front pocket","1 back zip pocket","Removable, adjustable shoulder strap","Measures 15.2\" L x 12\" H x 2.5\" W","Colours: Burgundy, Black and Tan"]) +
 "<h3>Who it is for</h3><p>For managers, bankers, consultants and anyone who carries a laptop to work every day. It is also a popular choice for team and client gifts, and we can add your company logo on bulk orders.</p>",
 [("Will my laptop fit?","The padded compartment takes laptops up to 14.5 inches. For a larger laptop, see the Extendable Travel Laptop Bag, which takes most laptops up to 15.5 inches."),("Can we order several for our team?","Yes. We offer corporate pricing on bulk orders and logo debossing on 10 or more pieces. Message us on WhatsApp.")])
P["copy-of-kordovans-crushable-premium-genuine-leather-western-cowboy-hat-s012"] = ("smooth",
 "<p>A genuine leather western hat built to be packed, sat on and pulled back into shape. The crushable crown takes a fold without creasing permanently, which makes this the one to own if your hat lives in a car, a bag or the back of a bike.</p>"
 "<h3>Details</h3>" + ul(["100% genuine leather, soft full-grain hide","Crushable and packable: reshapes after folding","Shaped brim that holds its curve","Lightweight for a full day in the sun"]) +
 "<h3>How to choose your size</h3>" + ul(["S: 20 to 21.5 inches","M: 21.5 to 22.5 inches","L: 22.5 to 23 inches","XL: 23 inches and above"]) + "<p>Measure around your head just above the ears and eyebrows. Between two sizes, pick the larger one.</p>",
 [("Will it lose its shape if I fold it?","No. The crown is made to fold for travel and push back into shape when you take it out."),("Is it good for travel?","Yes. It is our most packable hat, made for road trips and the northern areas.")])
P["durable-mens-leather-gloves-light-brown-kordovan"] = ("sheep", GL("Brown") + "<p>Rated 4.8 stars by 10 verified buyers.</p>",
 [("How do I choose my size?","Measure around your palm just below the knuckles. If you are between sizes, choose the larger one; the spandex palm gives a close fit."),("Can they get wet?","Light rain is fine. Let them dry naturally at room temperature, never on a heater.")])
P["durable-mens-leather-gloves-black-kordovan"] = ("sheep", GL("Black") + "<p>Rated 4.7 stars by 6 verified buyers.</p>",
 [("How do I choose my size?","Measure around your palm just below the knuckles. If you are between sizes, choose the larger one; the spandex palm gives a close fit."),("Black or brown?","Black is the classic, goes with everything and hides road dust. Brown is warmer and pairs with brown jackets and boots.")])
P["durable-womens-leather-gloves-dark-red-kordovan"] = ("sheep",
 "<p>Keep warm without giving up style. These women's gloves combine genuine sheep leather with 4-way stretch spandex, so they contour to your hands for a close, elegant fit, with a cosy fleece lining inside.</p>"
 "<h3>Details</h3>" + ul(["Genuine sheep leather with a 4-way stretch spandex palm","Soft stretch fleece lining for warmth","Non-slip palm patch for a secure grip","Elegant, classic cut","Sizes S, M, L and XL","Colour: Dark Red"]) +
 "<h3>Who it is for</h3><p>For winter commutes, evenings out and northern trips, and a thoughtful winter gift.</p>",
 [("How do I choose my size?","Measure around your palm just below the knuckles. Between sizes, choose the larger one.")])
P["natural-grain-double-stich-leather-belt"] = ("smooth",
 "<p>When smarter occasions call, the Executive belt brings a fine yet visible natural grain and neat double stitching. It is made from pit-tanned, oil-treated cowhide that will stay in your wardrobe for years.</p>"
 "<h3>Details</h3>" + ul(["100% pure leather: pit-tanned and oil-treated cowhide","Double-stitched edges","Snap system for interchanging buckles, so one strap works for office and weekend","Free size: can be cut down and screwed back to fit any waist","Colours: Chocolate Brown, Camel, Black and Tan"]) +
 "<h3>Who it is for</h3><p>For office wear, weddings and formal events, and a reliable everyday belt. One of our best-selling belts and an easy gift.</p>",
 [BELT_FAQ,("Can I change the buckle?","Yes. The snap system lets you swap buckles without tools.")])
P["double-pocket-extendable-travel-laptop-bag-natural-milld-leather-black"] = ("smooth",
 "<p>When you truly need to carry it all, the Extendable Travel Laptop Bag gives you organised space that grows with the trip. It is crafted in softly textured natural milled cow leather, with a padded laptop sleeve and a centre zip that expands the bag by an extra 1.5 inches.</p>"
 "<h3>What it carries</h3>" + ul(["Padded sleeve for most laptops up to 15.5 inches","Centre expansion zip: 1.5 inches of extra capacity","Front pocket for smaller items","Multi-functional inner compartments","Soft leather carry handle","Removable, adjustable padded shoulder strap","Colours: Black, Brown and Tan"]) +
 "<h3>Who it is for</h3><p>For business travellers and anyone who carries a larger laptop plus files, chargers and an overnight change. It works as a daily office bag and expands for trips.</p>",
 [("Will a 15.6-inch laptop fit?","It fits most laptops up to 15.5 inches. Send us your model on WhatsApp and we will confirm."),("Is it good for flights?","Yes. It is made as a carry-on work bag for business travel.")])
P["the-luxurious-ladies-clutch"] = ("smooth",
 "<p>The Luxurious Ladies Clutch is a wallet and clutch in one, in cow leather with an elegant ostrich-pattern texture. It keeps your phone, cards, notes and receipts organised, and is smart enough to carry on its own or slip into a handbag.</p>"
 "<h3>What it carries</h3>" + ul(["12 credit and debit card slots","1 ID window","2 compartments that hold most smartphones","Inner long pocket for notes, bills and receipts","Internal zip pocket for small valuables","Tuck-lock closure","Measures 7.5\" L x 3.8\" W x 1.3\" D","Colours: Black, Chocolate Brown, and White & Brown"]) +
 "<h3>Who it is for</h3><p>For women who want one piece for the office, weddings and evenings out, and a gift she will actually use.</p>",
 [("Is the ostrich pattern real ostrich?","No. It is genuine cow leather with an ostrich-style texture pressed into it.")])
P["shelby-thomas-soft-milled-leather-wallet"] = ("smooth",
 "<p>Some wallets take months to feel like yours. The Shelby & Thomas starts there. Cut from soft milled genuine cow leather, this bifold has a flexible, broken-in feel from the very first day, the easy-going cousin to our firmer leather wallets.</p>"
 "<h3>What it carries</h3>" + ul(["12 card slots","Flap ID window","2 internal cash slots","Topstitching and seaming detail","Two shades: Shelby and Thomas"]) +
 "<h3>Who it is for</h3><p>For men who carry a lot of cards and want a soft wallet that moulds to the pocket. Rated 4.8 stars by verified buyers.</p>",
 [("Does it get bulky with 12 cards?","Soft milled leather flexes around the cards, so it stays comfortable even when full.")])
P["genuine-sheep-leather-flat-cap-newsboy-unisex"] = ("sheep",
 "<p>A classic newsboy flat cap in genuine sheep leather. The smooth leather build is instantly recognisable, the seams are double stitched for strength, and an elastic sweatband inside gives a snug fit.</p>"
 "<h3>Details</h3>" + ul(["100% genuine sheep leather","Elastic inner sweatband for a close fit","Dual-stitched seams for added strength","Polyester lining that wipes clean with a damp cloth","Unisex","Colours: Brown, Black and Tan"]) +
 "<h3>Who it is for</h3><p>For winter mornings, drives and travel, and a smart finish over a jacket or sweater. A thoughtful winter gift.</p>",
 [("How should I clean it?","Wipe the lining with a damp cloth. For the leather outside, dry clean only.")])
P["nappa-leather-bifold-wallet-for-men-dark-brown"] = ("nappa",
 "<p>Every wardrobe needs one wallet that simply works. The Plain Bifold is Kordovan's classic: soft genuine nappa leather folded once, the horse-head mark embossed quietly on the front, and nothing else to announce it.</p>"
 "<h3>What it carries</h3>" + ul(["6 card slots","ID window","Full-width cash compartment","KORDOVAN embossed front","Topstitching and seaming details","Slim, contemporary profile"]) +
 "<h3>Which colour?</h3><p><strong>Tan</strong> is the warm, everyday choice that deepens with handling; <strong>Black</strong> is the formal one. Rated 4.75 stars by verified buyers. No gimmicks, no mechanisms: just the bifold, done properly.</p>",
 [("Is it slim enough for a trouser pocket?","Yes. It is deliberately compact and stays thin when full.")])
P["rigor-wallet-lite"] = ("sheep",
 "<p>Ten cards. Two bill compartments. Still slim. The Rigor Lite is built for organised minimalists who refuse to choose between capacity and profile: soft genuine sheep leather keeps it light while the layout takes everything a working day demands.</p>"
 "<h3>What it carries</h3>" + ul(["10 card slots","2 bill compartments for folded notes","Slim, flat profile that disappears into a pocket","100% genuine sheep leather, supple and lightweight","Colours: Brown and Black"]) +
 "<h3>Who it is for</h3><p>For first-time leather wallet buyers, students and anyone who wants a light everyday wallet. It is one of our most affordable handcrafted wallets.</p>",
 [("Sheep or cow leather?","Sheep leather is softer and lighter; cow leather is firmer and heavier. The Rigor Lite is made for a light, slim carry.")])
P["the-bastion-handcrafted-genuine-leather-bifold-wallet-for-men-slim-classic-everyday-wallet"] = ("smooth",
 "<p>Built for men who value durability, structure and timeless design. The Bastion is a classic bifold in premium genuine cow leather with a naturally distressed finish that deepens into a rich patina and makes every wallet uniquely yours.</p>"
 "<h3>What it carries</h3>" + ul(["Transparent ID window for quick access","Dedicated card slots","Smooth leather cash-fold compartment","Slim, structured profile","Colours: Tan and Brown"]) +
 "<h3>Who it is for</h3><p>For men who want rugged character in a slim everyday wallet. Not a trend-driven accessory: a long-term companion built to age beautifully.</p>",
 [("Will the distressed finish wear off?","No. It is part of the leather and deepens with use into a richer patina.")])
P["genuine-sheep-leather-adjustable-baseball-cap-unisex"] = ("sheep",
 "<p>A classic baseball cap in soft, supple genuine sheep leather, with traditional panelled styling, a well-rounded bill and an adjustable back strap for the right fit.</p>"
 "<h3>Details</h3>" + ul(["100% genuine sheep leather","Panelled crown","Curved visor with top stitching","Adjustable back strap: one size fits most","Unisex","Colours: Black, Brown, Red and White"]) +
 "<h3>Who it is for</h3><p>For drives, travel, weekends and winter outings, and an easy gift. Rated 4.8 stars by 5 verified buyers.</p>",
 [("Is the leather shiny?","No. It has a soft matte finish, which keeps it looking natural.")])
P["the-aristocrat-wallet"] = ("smooth",
 "<p>Not every wallet needs to shout. The Aristocrat is the quiet one: a slim, classic-cut genuine leather wallet with clean lines and understated styling, for those who prefer restraint over rugged texture.</p>"
 "<h3>What it carries</h3>" + ul(["Multiple compartments for cards and cash","Slim, streamlined profile","Premium genuine leather construction","Colours: Brown and Black"]) +
 "<h3>Who it is for</h3><p>Equally at home in a suit pocket or a weekend jacket. <strong>Brown</strong> for warmth, <strong>Black</strong> for the boardroom. A safe, elegant gift for a father, husband or colleague.</p>",
 [("Will it fit a suit jacket pocket?","Yes. It is cut slim so it doesn't spoil the line of a jacket.")])
P["tp-the-corporate-laptop-bag"] = ("smooth",
 "<p>The Corporate is a structured leather briefcase for the modern professional, made for boardroom meetings, business travel and everyday office life. It keeps your laptop, documents and essentials organised behind a sturdy zip.</p>"
 "<h3>What it carries</h3>" + ul(["Compartments for your laptop, documents and essentials","Pen holders and a dedicated phone pocket","External pocket for quick-access items","Sturdy zip closure","Dual carry handles plus an adjustable, padded shoulder strap","Colours: Black, Tan and Brown"]) +
 "<h3>Who it is for</h3><p>For executives, lawyers and anyone who wants a briefcase that makes a statement. A strong corporate gift: ask us about bulk orders with your company logo.</p>",
 [("Will my laptop fit?","Send us your laptop model on WhatsApp and we will confirm before you order.")])
P["the-diva-tote"] = (None,
 "<p>Whether you are running errands, shopping or out for the evening, the Diva is a medium-size tote that stays organised thanks to its interior wall pocket. It comes with a matching pouch for your everyday essentials.</p>"
 "<h3>Details</h3>" + ul(["Vegan leather (microfibre): waterproof, light and washable","Top carry handles","Interior pocket for your phone","Fully lined","Matching pouch included","Folds flat when not in use","Measures 14\" L x 12\" H x 4\" W","Colours: Light Brown, Beige and Chocolate Brown"]) +
 "<h3>Who it is for</h3><p>For women who want one roomy, practical bag from day to night. Rated 4.7 stars by verified buyers, who mention how light and spacious it is.</p>",
 [("Is it real leather?","No. The Diva is vegan leather, which is waterproof and easy to wipe clean.")])
P["midtown-lite-wallet"] = ("sheep",
 "<p>Slim outside, organised inside. The Midtown Lite is cut from soft black sheep leather, one of the gentlest hides we use, and closes with a single snap button that keeps everything exactly where you left it.</p>"
 "<h3>What it carries</h3>" + ul(["9 card slots","2 ID windows with their own snap buttons","2 bill slots for folded notes","Outer snap pocket for small essentials","Secure snap-button closure","Colour: Black"]) +
 "<h3>Who it is for</h3><p>For anyone who wants a secure, light wallet that closes properly, and the easiest way into a handcrafted Kordovan wallet.</p>",
 [("Why a snap closure?","It keeps cards and notes from slipping out, even when the wallet is full.")])

NOTE_FOR = {"durable-mens-leather-gloves-light-brown-kordovan","durable-mens-leather-gloves-black-kordovan","durable-womens-leather-gloves-dark-red-kordovan","genuine-sheep-leather-flat-cap-newsboy-unisex","genuine-sheep-leather-adjustable-baseball-cap-unisex","double-pocket-extendable-travel-laptop-bag-natural-milld-leather-black"}
CARE["sheep"]=SHEEP
out={}
for h,(care,body,qs) in P.items():
    html = body + (CARE[care] if care else "") + faq(qs) + (VEGAN if h=="the-diva-tote" else STD) + (NOTE if h in NOTE_FOR else "")
    txt = re.sub("<[^>]+>"," ",html).lower()
    for bad in ["coin","karachi","workshop","hand-cut","pkr 1","rs 4,800","nadia","disclaimer (must"]:
        assert bad not in txt,(h,bad)
    if h=="the-diva-tote": assert "genuine leather" not in txt
    out[h]={"html":html,"words":len(txt.split())}
json.dump(out,open('batch2.json','w'),indent=1)
for h,v in out.items(): print(v['words'],h)
