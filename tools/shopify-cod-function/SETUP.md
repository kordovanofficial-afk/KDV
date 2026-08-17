# Hide COD on made-to-order products

A Shopify Function that removes **Cash on Delivery (COD)** from checkout when the
cart contains a made-to-order item. Everything else in the catalogue keeps COD.

Shopify has no setting for this. Conditional payment rules only exist as
Functions, and a Function has to be deployed from a real app — which is why this
needs a terminal once. After the first deploy you never touch it again.

---

## What you need first

- **A computer you can install things on** (not a phone)
- **Node.js** — download the LTS build from <https://nodejs.org> and install it.
  Click through the defaults.
- **A Shopify Partner account** — free, sign up at
  <https://partners.shopify.com>. Use the same email as the store if you like.

That is the whole shopping list. About 10 minutes.

---

## Step 1 — Open a terminal

- **Windows:** press Start, type `powershell`, hit Enter.
- **Mac:** press Cmd+Space, type `terminal`, hit Enter.

A black or white text window opens. You paste commands into it and press Enter
after each one. Wait for each to finish before pasting the next.

Check Node installed correctly by pasting this:

```
node --version
```

You should see something like `v22.11.0`. Any number 16 or higher is fine. If it
says "not recognized", Node did not install — reinstall and reopen the terminal.

---

## Step 2 — Create the app

Paste these one at a time.

```
npm install -g @shopify/cli@latest
```

```
shopify app init --name kordovan-checkout-rules
```

It will ask a few questions:

| Question | Answer |
| --- | --- |
| Log in to Shopify | A browser opens — log in and click **Allow** |
| Which organisation | Pick your Partner organisation |
| Create this project as a new app | **Yes** |
| Get started building your app | Pick **Start with Remix** (any is fine) |

When it finishes, move into the new folder:

```
cd kordovan-checkout-rules
```

---

## Step 3 — Generate the empty function

```
shopify app generate extension
```

Answer:

| Question | Answer |
| --- | --- |
| Type of extension | Scroll to **Payment customization** and pick it |
| Name | `hide-cod-made-to-order` |
| Language | **JavaScript** |

This creates a folder:
`extensions/hide-cod-made-to-order/src/`

---

## Step 4 — Replace two files

Inside `extensions/hide-cod-made-to-order/src/` there are two files with long
names starting `cart_payment_methods_transform_run`. **Open each one, select
everything, delete it, and paste in the matching file from this folder:**

| Replace this file | With this one |
| --- | --- |
| `src/cart_payment_methods_transform_run.graphql` | `function/src/cart_payment_methods_transform_run.graphql` |
| `src/cart_payment_methods_transform_run.js` | `function/src/cart_payment_methods_transform_run.js` |

Same filenames, just different contents. Nothing else changes.

> If the generated filenames differ slightly, match them by extension: the
> `.graphql` file gets the `.graphql` contents, the `.js` file gets the `.js`
> contents.

Then regenerate the types:

```
shopify app function typegen
```

---

## Step 5 — Deploy

```
shopify app deploy
```

Say **Yes** when it asks to confirm. Then install the app on the live store:

```
shopify app dev
```

Press `p` to open the preview URL, and click **Install app** when the browser
asks. Once installed you can close the terminal with `Ctrl+C`.

---

## Step 6 — Switch it on

This last bit is in the admin, no terminal.

1. Shopify admin → **Settings** → **Payments**
2. Scroll to **Payment method customizations** → **Add customization**
3. Pick **hide-cod-made-to-order**
4. Give it a name: `Hide COD on made-to-order`
5. **Save**, then make sure it shows as **Active**

---

## Step 7 — Test it before trusting it

Do both of these on the live store:

1. **Add a wallet to the cart** and go to checkout.
   → Cash on Delivery should still be there.
2. **Add any jacket to the cart** and go to checkout.
   → Cash on Delivery should be gone. Bank Deposit and card remain.

If test 2 still shows COD, wait two minutes and hard-refresh — Shopify caches
checkout briefly after a customization is activated.

---

## How it decides

A product counts as made to order if **either** is true:

- its `custom.made_to_order` metafield is `true`, **or**
- it carries the `made-to-order` tag

Both are already set on all 30 jackets. Two signals rather than one so the rule
does not silently break if a future product is missed.

**For any new made-to-order product, just add the `made-to-order` tag.** That is
all. No code, no redeploy.

One line in the cart is enough to make the whole cart prepaid — Shopify cannot
apply different payment terms to different items in one order. The cart page and
cart drawer already say this before checkout, so it should not surprise anyone.

## Safety behaviour

- If COD is not offered at all, the function does nothing.
- If COD were somehow the *only* payment method, it does **not** hide it —
  a checkout with zero payment options is worse than a COD order you can chase.
- If the cart is empty or malformed, it does nothing.

All ten of these cases are covered by the tests in `function/test-notes.md`.

## If you want to turn it off

Settings → Payments → Payment method customizations → toggle it off. Takes
effect immediately. Nothing else in the store is affected.
