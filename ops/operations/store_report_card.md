# Kordovan daily store report: Ahsan's card

Send **one** WhatsApp message to the Kordovan group at closing. Mr. Tahir replies **OK** once the TOTAL matches the cash drawer.

## How to write it
```
KDV 01/11
MOCHA 2
BAST-BR 1
CLIF-RB-M 1
RET LUKE 1
LINES 4
TOTAL Rs 15,100
```
- **Line 1:** `KDV` + date (day/month).
- **One line per item:** `CODE QTY`.
- **Customer return back onto the shelf:** `RET CODE QTY`.
- **`LINES`** = how many item lines you wrote. **`TOTAL`** = cash plus card taken at the counter.
- **Nothing sold:** `KDV 01/11 NIL`

## Rules (4)
1. **Walk-in sales only.** An online order packed from the shelf does **not** go in. Shopify already took it off.
2. **Never edit a sent message.** Made a mistake? Send `FIX 01/11 CODE QTY` with the correct line.
3. **Code not on this card?** Write the product name and colour in words. Zain sorts it out next morning. Never guess a code.
4. **Sizes:** hats and gloves take the size at the end: `-S` `-M` `-L` `-XL` `-XXL`.

## The 40 codes
**Men's wallets**
| Code | Item |
|---|---|
| MOCHA | Mocha Mate |
| BAST-BR | Bastion Brown |
| BAST-TN | Bastion Tan |
| LUKE | Luke |
| RAZ-BB | Razor Black Brown |
| RAZ-BRB | Razor Brown Black |
| RAZ-RB | Razor Red Black |
| RAZ-AB | Razor All Black |
| RAZ-ABR | Razor All Brown |
| RAZ-AR | Razor All Red |
| KODO-BK | KODO Black |
| KODO-BR | KODO Brown |
| KODO-BG | KODO Black Gold |
| KV2-BR | Kodo Vertical 2.0 Brown |
| RIGOR-BK | Rigor Lite Black |
| RIGOR-BR | Rigor Lite Brown |
| MIDTOWN | Midtown Lite |
| SHEP | Sheppard wallet |
| SHELBY | Shelby (Shelby & Thomas) |
| PLAIN-BK | Plain Bifold Black |
| PLAIN-TN | Plain Bifold Tan |
| ARIS-BR | Aristocrat Brown |
| ARIS-BK | Aristocrat Black |
| HUNTER | Hunter HM |
| SEAM | The Seamless |
| CLIP | Money Clip |
| STALLION | Stallion wallet |
| BRONCO | Bronco Pullup |
| ELITE-BR | Elite Mobile Wallet Dave Brown |
| ELITE-BK | Elite Mobile Wallet Midnight Black |

**Women's wallets**
| Code | Item |
|---|---|
| CLUTCH-WB | Luxurious Ladies Clutch White & Brown |
| CLUTCH-CH | Luxurious Ladies Clutch Chocolate |
| CLUTCH-BK | Luxurious Ladies Clutch Black |

**Hats, caps, gloves** (add the size at the end)
| Code | Item |
|---|---|
| CLIF-RB-(size) | Clifford Cowboy Hat Rustic Brown |
| CLIF-FB-(size) | Clifford Cowboy Hat Faded Black |
| STRIPE-(size) | Black Stripe Cowboy Hat |
| CAP-BK / CAP-BR | Sheep Leather Baseball Cap Black / Brown |
| FLAT-BK / FLAT-BR / FLAT-TN | Flat Cap Newsboy Black / Brown / Tan |
| GLV-BK-(size) / GLV-BR-(size) | Men's Winter Gloves Black / Brown |
| GLV-W-(size) | Women's Winter Gloves Dark Red |

Example: `CLIF-RB-M 1` = one Clifford Rustic Brown hat, size M.

*Card v1, Nov 1 2026 (COO). Codes are ranked by online sales because counter sales are not in Shopify yet. Mr. Tahir: send the
names of any counter best-sellers that are missing, and v2 adds them.*
