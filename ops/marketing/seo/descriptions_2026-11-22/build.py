import json, re, sys
OUT = sys.argv[1]
def ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
def faq(qs): return "<h3>Questions we get</h3>" + "".join(f"<p><strong>{q}</strong><br>{a}</p>" for q,a in qs)
CARE = {
 "crazy": "<h3>Care</h3><p>Crazy Horse leather is waxed, so scuffs blend back in when you rub them with a warm thumb. Wipe it with a dry cloth, keep it away from long soaks, and give it a little leather balm every few months. The colour deepens and the surface picks up a patina that is yours alone.</p>",
 "smooth": "<h3>Care</h3><p>Wipe with a soft dry cloth, keep it out of rain and direct heat for long periods, and condition it with a little leather balm every few months. Real leather softens and darkens slowly with use, which is the point.</p>",
 "nappa": "<h3>Care</h3><p>Nappa is soft, fine-grained leather. Wipe it with a dry cloth, keep it away from water and sharp objects, and condition it lightly every few months to keep it supple.</p>",
 "pebbled": "<h3>Care</h3><p>Pebbled leather has a textured grain that hides small scratches well. Wipe it with a soft dry cloth, let it air-dry naturally if it gets wet, and condition it every few months. Stuff the bag lightly when it is stored so it keeps its shape.</p>",
}
STD = "<h3>Delivery, payment and warranty</h3><p>Handcrafted in Pakistan from genuine leather, never coated synthetic. Cash on delivery is available across Pakistan, delivery is free on orders over Rs 5,500, and every piece is covered by our lifetime craftsmanship warranty on stitching and hardware. Need a measurement or a closer look at a colour? Message us on WhatsApp at 0333 2601161.</p>"
MTO = "<h3>Made to order: how it works</h3><p>Each pair is cut for one customer in the size you choose, so it is paid online at checkout (card, debit or JazzCash) and cannot be resold to anyone else. It takes about 3 weeks from checkout to your door; winter is our busiest season, so order early. Handcrafted in Pakistan and backed by our lifetime craftsmanship warranty. Questions about sizing? Message us on WhatsApp at 0333 2601161.</p>"
BELT_FAQ = ("What size should I order?", "Our belts are free size: they can be cut down and screwed back to fit any waist. Tell us your size on WhatsApp and we can help you get it right.")

P = {}
P["rfid-protected-kodo-smart-wallet"] = ("smooth",
 "<p>KODO is Kordovan's RFID-protected smart wallet, designed by us and made from two bonded layers of genuine Crazy Horse cow leather. It blocks contactless card skimming, carries up to ten cards, and stays slim enough for a front pocket.</p>"
 "<h3>What it carries</h3>" + ul(["RFID protection, so your contactless cards stay silent to skimmers","Up to 10 cards across 3 separate sections for cards, ID and cash","1 pull-tab pocket that presents your most-used card","High-quality elastic that keeps everything shut","Extremely slim and lightweight","Colours: Black, Brown, Black Gold and Brown Gold"]) +
 "<h3>Who it is for</h3><p>For anyone who carries cards rather than a stack of notes and wants a wallet that disappears in the pocket. With 169 verified reviews averaging 4.6 stars, it is one of our most-reviewed pieces.</p>",
 [("Does RFID protection really matter?","Contactless cards can be read from a short distance. The RFID layer blocks that signal while the cards are inside the wallet."),("Will it fit notes?","Yes, one section is for cash. It is built for a slim carry, so fold notes once.")])
P["tri-fold-premium-durable-belt"] = ("smooth",
 "<p>The Tri-Fold belt is made from premium cow leather folded three times, so each layer bonds to the next. The result is a belt that holds its shape and softens to your waist rather than cracking.</p>"
 "<h3>Details</h3>" + ul(["Premium cow leather, folded three times for strength","Free size: can be cut down and screwed back to fit any waist","Colours: Brown, Tan and Black","Works with jeans, chinos and formal trousers"]) +
 "<h3>Who it is for</h3><p>For the man who has gone through cheap belts that peel at the holes and wants one he buys once.</p>",
 [BELT_FAQ,("Which colour should I choose?","Brown and Tan go with casual wear and brown shoes; Black is the safe choice for office and formal wear.")])
P["the-elite-mobile-wallet-unisex"] = ("nappa",
 "<p>The Elite is a full-length mobile wallet in genuine nappa leather, built with a dedicated chamber for your smartphone beside your cards and cash. Phone, cards and notes leave the house as one piece instead of three.</p>"
 "<h3>What it carries</h3>" + ul(["Dedicated mobile phone chamber","12 credit and debit card slots","1 ID window","2 cash slots","Measures 7.3\" L x 3.7\" W x 0.6\" D","Colours: Dave Brown and Midnight Black"]) +
 "<h3>Who it is for</h3><p>Men and women who carry a bag or a jacket pocket rather than a trouser pocket, travellers, and anyone tired of juggling a phone and a wallet. The phone chamber is what sets it apart from our standard long wallets.</p>",
 [("Will my phone fit?","It is sized for a standard smartphone. For very large phones or thick cases, message us your model on WhatsApp before ordering."),("Is it unisex?","Yes. The clean long shape works as a men's travel wallet or a women's clutch.")])
P["crazy-horse-long-wallet-unisex-kordovan-light"] = ("crazy",
 "<p>The Crazy Horse Long is a full-length wallet in genuine Crazy Horse cowhide with a rustic brown finish. Natural marks and scuffs are part of the leather, and they deepen into character the longer you carry it.</p>"
 "<h3>What it carries</h3>" + ul(["11 credit and debit card slots","1 ID window","2 full-size bill compartments, so notes stay flat and unfolded","Measures 7.5\" L x 3.8\" W","Colours: Light Brown and Dark Brown"]) +
 "<h3>Who it is for</h3><p>For those who carry more cards and full-size notes than a bifold can take. It works as a men's long wallet, a travel organiser or a slim unisex clutch.</p>",
 [("Long wallet or bifold?","Choose a long wallet if you carry more than 6 cards or prefer notes unfolded. Choose a bifold if it lives in your trouser pocket."),("Are the marks on the leather defects?","No. Crazy Horse leather is waxed and shows natural marks; they are what make each piece one of a kind.")])
P["leather-key-chain-with-belt-loop"] = ("smooth",
 "<p>Stop stuffing a bulky bunch of keys into your pocket. This genuine leather key chain slips onto your belt, keeps your keys where you can reach them, and looks better every year you use it.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather with a belt loop","Fits most standard belts","Holds house, car and office keys together","Colours: Black and Brown"]) +
 "<h3>Who it is for</h3><p>For drivers, office-goers and anyone who keeps losing keys. It is also an easy, useful gift, and it pairs well with any of our leather belts to make the most of free delivery over Rs 5,500.</p>",
 [("Will it fit my belt?","It is made to fit most standard belt widths. Message us your belt width on WhatsApp if you are unsure.")])
P["executive-comfort-oxford"] = (None,
 "<p>The Executive Comfort Oxford pairs genuine cow leather with a German VibraStep sole, so it looks formal and feels comfortable through a full office day. Classic Oxford lines, made in your size.</p>"
 "<h3>Details</h3>" + ul(["Genuine cow leather upper","German VibraStep sole for all-day comfort","Classic Oxford styling for office and formal wear","Sizes EU 39 / UK 5 to EU 45 / UK 11","Lifetime craftsmanship warranty on stitching and soles"]) +
 "<h3>Care</h3><p>Brush off dust after wear, use a shoe tree to keep the shape, and polish with a matching cream every few weeks. Let them rest a day between wears.</p>",
 [("How do I choose my size?","Order your usual UK size. If you are between sizes, message us on WhatsApp before ordering, because each pair is made for you.")])
P["bronco-handcrafted-wallet"] = ("crazy",
 "<p>The Bronco is a handcrafted bifold in genuine Crazy Horse cow leather with a waxed, distressed finish. It is the most rugged wallet we make, and it is built to scar, burnish and age into a patina that is yours alone.</p>"
 "<h3>What it carries</h3>" + ul(["4 credit and debit card slots","2 hidden slots for the cards you rarely use","1 large bill compartment","Approximately 3.5\" x 4.5\" when closed: true front-pocket size","Colours: Light Pullup and Pullup"]) +
 "<h3>Who it is for</h3><p>For men who want a wallet with character rather than shine. The waxed leather gives it a more vintage look than our smooth leather wallets.</p>",
 [("Will it look worn quickly?","It will change, and that is the idea. Light scratches blend back into the wax, and the leather darkens evenly with use.")])
P["vouge-jewellery-case"] = ("smooth",
 "<p>The Trinity Jewellery Case keeps your jewellery safe, organised and ready to travel. It is made from premium glazed cow leather and lined with soft fabric that protects pieces from scratches.</p>"
 "<h3>Details</h3>" + ul(["Premium glazed cow leather exterior","Soft inner fabric lining that protects against scratches","Two compartments for jewellery and small trinkets","Colours: Black, Tan, Maroon and Red"]) +
 "<h3>Who it is for</h3><p>For anyone who travels with rings, earrings and chains, and a thoughtful gift for weddings, birthdays and Eid. Leather where you would normally accept plastic.</p>",
 [("Is it good as a gift?","Yes, it makes a thoughtful gift for weddings, birthdays and Eid.")])
P["imperial-keychain"] = ("smooth",
 "<p>The Imperial Keychain is cut from premium, high-grade leather for a bold, refined look that never goes out of style. It is a small piece of leather that outlasts the keys it carries.</p>"
 "<h3>Details</h3>" + ul(["Premium genuine leather","Sturdy, durable build for daily use","Colours: Tan, Maroon, Chocolate Brown and Black"]) +
 "<h3>Who it is for</h3><p>For car keys, house keys or as an easy add-on gift. Pair it with a wallet or belt to reach free delivery over Rs 5,500.</p>",
 [("Which colour ages best?","Tan shows the most change over time and develops a rich patina; Black stays the most uniform.")])
P["mocha-mate"] = ("smooth",
 "<p>A best-seller for a simple reason: it carries more than a card-only slim wallet. The Mocha Mate is a genuine cow leather bifold with an outer button-closure pocket on the back for small essentials, the everyday wallet for those who carry a little more.</p>"
 "<h3>What it carries</h3>" + ul(["5 to 6 card slots","Spacious cash pocket","ID window for quick access","Outer button-closure pocket for small essentials","100% genuine cow leather"]) +
 "<h3>Who it is for</h3><p>For men who want one organised wallet for cards, cash, ID and the small things that usually float loose in a pocket. Rated 4.6 stars by verified buyers.</p>",
 [("What goes in the button pocket?","Small essentials such as a SIM tool, a folded receipt, a spare key or a memory card."),("Is it slim?","It is a compact bifold that fits a trouser pocket comfortably.")])
P["the-truckkr-bi-fold"] = ("crazy",
 "<p>A bifold that zips. The Truckkr is handcrafted from genuine Crazy Horse cow leather with an external zip compartment, secure small-item storage that standard bifolds skip, alongside dedicated card and cash slots.</p>"
 "<h3>What it carries</h3>" + ul(["External zip compartment for small items","Dedicated card and cash compartments","Compact, slim bifold design","100% genuine Crazy Horse cow leather that develops a unique patina"]) +
 "<h3>Colour note</h3><p>Crazy Horse leather reads darker in person than on most screens: expect a deep, rich brown that lightens where it rubs over time.</p>",
 [("Why a zip pocket?","It keeps small items such as a key, a SIM card or folded notes secure, so nothing slips out when you open the wallet.")])
P["kordovans-affordable-cowboy-hat"] = ("smooth",
 "<p>A plain black leather western hat with a contrast striped band around the crown. It is the simplest hat in our range and the easiest to wear with anything, from jeans to a winter jacket.</p>"
 "<h3>Details</h3>" + ul(["100% genuine leather","Contrast striped band","Shaped brim","Lightweight for long wear in the sun","Sizes S to XL"]) +
 "<h3>How to choose your size</h3><p>Measure around your head just above the ears and eyebrows. Between two sizes, pick the larger one. Message us your measurement on WhatsApp if you are unsure.</p>",
 [("Can I wear it in the heat?","Yes. It is lightweight leather, made for long days outdoors.")])
P["tp-dblp-laptop-bag"] = ("pebbled",
 "<p>The DBLP Laptop Bag is built for office people on the move. It is crafted from pebbled top-grain cow leather, with organisers inside the laptop pocket and a trolley-handle slot so it rides on your suitcase when you travel.</p>"
 "<h3>What it carries</h3>" + ul(["Main laptop compartment with built-in organisers","Two front pockets for a phone, charger and pens","Trolley-handle slot for easy travel","Pebbled top-grain cow leather that hides everyday scratches","Colours: Black, Brown and Tan"]) +
 "<h3>Who it is for</h3><p>For professionals who commute daily and travel for work, and for companies looking for a gift their team will actually use. Ask us about corporate orders with your logo.</p>",
 [("Will my laptop fit?","Message us your laptop size on WhatsApp and we will confirm before you order."),("Can I order several for my company?","Yes. We offer corporate pricing on bulk orders; contact us on WhatsApp.")])
P["tp-millard-office-bag"] = ("pebbled",
 "<p>The Millard Office Bag is a structured briefcase in real pebbled top-grain leather, smart enough to walk into a meeting with and practical enough for every day of the week.</p>"
 "<h3>What it carries</h3>" + ul(["Three compartments, including a laptop compartment for up to 15 inches","Organiser in the first compartment for pens, cards and cables","Additional zip compartment on the back","Sized for A4 documents","Colours: Black, Blue, Tan and Brown"]) +
 "<h3>Who it is for</h3><p>For managers, lawyers, bankers and anyone who carries both files and a laptop. A strong choice for corporate gifting; ask us about logo orders.</p>",
 [("Will a 15.6-inch laptop fit?","The laptop compartment is made for laptops up to 15 inches. For larger models, message us on WhatsApp first.")])
P["buffalo-bob-leather-belt"] = ("smooth",
 "<p>The Buffalo Bob is a thick top-grain leather belt with a rugged buffalo-style finish, made to take daily wear and keep going. It is built for a lifetime of durable style.</p>"
 "<h3>Details</h3>" + ul(["Top-grain leather with a rugged finish","Thick, sturdy strap that softens to your waist rather than cracking","Free size: can be cut down and screwed back to fit any waist","Colours: Black and Brown"]) +
 "<h3>Who it is for</h3><p>For jeans and casual wear, and for anyone who wants a belt that looks better after a year than on day one.</p>",
 [BELT_FAQ])
P["diana-cross-body-bag-pebbled-leather"] = ("pebbled",
 "<p>The Diana Cross-body Bag combines style and practicality in pebbled top-grain leather. It sits close to the body, keeps your hands free, and works for both casual days and formal occasions.</p>"
 "<h3>What it carries</h3>" + ul(["Three spacious compartments","Cross-body wear, hands free","Pebbled top-grain leather that resists everyday scratches","Colours: Burgundy, Brown, Camel, Black and Navy Blue"]) +
 "<h3>Who it is for</h3><p>An everyday bag for women who want their phone, wallet, keys and essentials organised, from the office to a dinner out. Also available in Crazy Horse leather.</p>",
 [("Pebbled or Crazy Horse?","Pebbled leather is textured and stays neat; Crazy Horse is waxed and develops a rustic patina over time.")])
P["diana-cross-body-bag-crazy-horse-leather"] = ("crazy",
 "<p>The Diana Cross-body Bag in Crazy Horse cow leather brings a rustic, waxed finish to a practical everyday shape. It sits close to the body, keeps your hands free, and weathers beautifully with use.</p>"
 "<h3>What it carries</h3>" + ul(["Three spacious compartments","Cross-body wear, hands free","Waxed Crazy Horse leather that develops a patina","Colours: Crazy Camel and Crazy Brown"]) +
 "<h3>Who it is for</h3><p>For women who like leather with character, for both casual and formal occasions. Also available in pebbled leather in five colours.</p>",
 [("Pebbled or Crazy Horse?","Crazy Horse is waxed and ages into a rustic patina; pebbled leather is textured and stays neat.")])
P["the-seamless-stitch-less-wallet-brown"] = ("smooth",
 "<p>No stitches. No seams. No bulk. The Seamless is a stitch-less single-compartment wallet folded from one piece of leather. It is card-sized, holds up to 10 cards with cash tucked behind them, and ages remarkably over time.</p>"
 "<h3>What it carries</h3>" + ul(["Up to 10 cards plus cash in one compartment","Stitch-less, single-piece construction: no thread to fray","Card-sized: the slimmest carry we make","Genuine leather that ages with everyday use"]) +
 "<h3>Who it is for</h3><p>For minimalists, front-pocket carriers and anyone moving from a bulky bifold to something they forget is there.</p>",
 [("How can it hold 10 cards without stitching?","It is folded from a single piece of leather, so the shape itself holds the cards, with nothing to come apart.")])
P["tp-the-city-backpack"] = ("smooth",
 "<p>The City Backpack is a genuine leather backpack for the daily commute, the campus and the weekend. It carries your weight evenly on both shoulders, and the leather ages instead of wearing out like canvas or nylon.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather backpack","Carries weight evenly on both shoulders","Colours: Black, Brown and Tan"]) +
 "<h3>Who it is for</h3><p>For students, professionals who walk or ride to work, and anyone who prefers a backpack to a shoulder bag. For exact dimensions and inside pockets, message us on WhatsApp and we will send photos.</p>",
 [("Will my laptop fit?","Send us your laptop size on WhatsApp and we will confirm before you order.")])
P["tp-executive-a4-folder"] = ("smooth",
 "<p>The Executive A4 Folder keeps your documents flat, organised and professional, so nothing arrives at a meeting creased or dog-eared. It is genuine leather that makes a strong first impression across a table.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather A4 folder","Holds A4 documents flat","Made for meetings, interviews and client visits","Colours: Black and Brown"]) +
 "<h3>Who it is for</h3><p>For executives, lawyers, consultants and job seekers, and a polished corporate gift. Ask us about bulk orders with your company logo.</p>",
 [("Can I add our company logo?","Yes, on bulk corporate orders. Message us on WhatsApp for pricing and timing.")])
P["tp-voyager-suitcase-trolley-bag-1"] = ("smooth",
 "<p>The Voyager is a genuine leather suitcase trolley bag built for repeat trips, not one holiday. It rolls through airports and hotel lobbies, and it looks better on its tenth journey than its first.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather suitcase on wheels","Trolley handle for easy rolling","Built for frequent travel","Colours: Black and Brown"]) +
 "<h3>Who it is for</h3><p>For frequent business travellers and anyone who wants luggage that stands out from plastic shells. For exact dimensions and airline cabin sizing, message us on WhatsApp before you order.</p>",
 [("Is it cabin size?","Message us on WhatsApp with your airline and we will send the exact measurements.")])
P["leather-lanyard"] = ("smooth",
 "<p>A genuine leather lanyard for your office ID and access cards. It outlasts every fabric lanyard, sits comfortably around the neck, and adds a quiet touch of quality to your working day.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather","Holds an ID or access card","Comfortable for all-day wear","Colours: Black, Bodo and Tan"]) +
 "<h3>Who it is for</h3><p>For office staff, hospital and university teams, and companies that want a better staff lanyard. Ask us about bulk orders with your logo.</p>",
 [("Do you make bulk lanyards for companies?","Yes. Message us on WhatsApp with the quantity and we will quote.")])
P["the-masters-leather-laptop-bag"] = ("smooth",
 "<p>The Master's Leather Laptop Bag is made to carry a laptop and the working day around it. It is genuine leather with a slim profile that sits neatly over the shoulder or in the hand.</p>"
 "<h3>Details</h3>" + ul(["Genuine leather laptop bag","Slim profile for the daily commute","Two finishes: Croc (textured cow leather) and Multicolor"]) +
 "<h3>Who it is for</h3><p>For professionals who want a leather laptop bag without the weight of a full briefcase. Message us on WhatsApp for exact dimensions and to confirm your laptop fits.</p>",
 [("Is the Croc finish real crocodile?","No. It is cow leather with a croc texture pressed into it, not exotic skin.")])

out = {}
for h,(care,body,qs) in P.items():
    mto = h == "executive-comfort-oxford"
    html = body + (CARE[care] if care else "") + faq(qs) + (MTO if mto else STD)
    txt = re.sub("<[^>]+>"," ",html)
    for bad in ["coin","karachi","workshop","hand-cut","rs 4,800","rs 1","50%","4-7 days"]:
        assert bad not in txt.lower(), (h,bad)
    out[h] = {"html":html,"words":len(txt.split())}
json.dump(out, open(OUT,"w"), indent=1)
for h,v in out.items(): print(v["words"], h)
