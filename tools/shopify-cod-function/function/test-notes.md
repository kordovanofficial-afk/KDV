# Test cases

Run against the logic in `src/cart_payment_methods_transform_run.js`, using the
store's real payment method names as they appear in order data:
`Cash on Delivery (COD)`, `Bank Deposit`, `Credit card`.

| Case | Cart | Expected |
| --- | --- | --- |
| Wallet only, no flags | one unflagged line | COD stays |
| Jacket via metafield | `custom.made_to_order = "true"` | COD hidden |
| Jacket via tag only | `made-to-order` tag, no metafield | COD hidden |
| Metafield explicitly false | `"false"` | COD stays |
| Mixed cart | wallet + jacket | COD hidden (whole cart is prepaid) |
| Empty cart | no lines | COD stays |
| COD is the only method | jacket, only COD offered | **COD stays** — never strand the buyer |
| No COD offered | jacket, card + bank only | no-op |
| Missing merchandise object | malformed line | COD stays |
| Undefined input | `{}` | COD stays |

All ten pass. The two that matter most are the mixed cart (Shopify cannot split
payment terms within an order, so one made-to-order line makes the whole cart
prepaid) and the strand guard.

To re-run after any edit, from this directory:

```
node --input-type=module -e "$(cat src/cart_payment_methods_transform_run.js | sed 's|^// @ts-check||')
const M=[{id:'gid://1',name:'Cash on Delivery (COD)'},{id:'gid://2',name:'Bank Deposit'},{id:'gid://3',name:'Credit card'}];
const line=(mto,tag)=>({merchandise:{product:{madeToOrder:mto===null?null:{value:mto},taggedMadeToOrder:tag}}});
console.log(cartPaymentMethodsTransformRun({cart:{lines:[line('true',false)]},paymentMethods:M}));"
```
