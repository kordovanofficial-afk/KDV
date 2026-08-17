// @ts-check

/**
 * Hide Cash on Delivery when the cart contains a made-to-order product.
 *
 * Why this exists: jackets are cut for one customer over 4–7 working days and
 * are prepaid. When COD stayed selectable, roughly 60% of jacket orders were
 * placed on COD and then refused on the confirmation call, after the leather
 * had already been cut. Every one of those was a total loss.
 *
 * Shopify cannot split payment terms inside a single order, so one made-to-order
 * line makes the whole cart prepaid. That matches what the cart page now says.
 *
 * @typedef {import("../generated/api").CartPaymentMethodsTransformRunInput} RunInput
 * @typedef {import("../generated/api").CartPaymentMethodsTransformRunResult} RunResult
 */

/** @type {RunResult} */
const NO_CHANGES = { operations: [] };

/** Matches "Cash on Delivery (COD)" and any reasonable rename of it. */
const COD_PATTERN = /cash\s*on\s*delivery|(^|[^a-z])cod([^a-z]|$)/i;

/**
 * @param {RunInput} input
 * @returns {RunResult}
 */
export function cartPaymentMethodsTransformRun(input) {
  const lines = input?.cart?.lines ?? [];

  const cartIsMadeToOrder = lines.some((line) => {
    const product = line?.merchandise?.product;
    if (!product) return false;
    // Metafield values arrive as strings, never booleans.
    const flagged = product.madeToOrder?.value === "true";
    return flagged || product.taggedMadeToOrder === true;
  });

  if (!cartIsMadeToOrder) return NO_CHANGES;

  const methods = input?.paymentMethods ?? [];
  const cod = methods.filter((m) => COD_PATTERN.test(m?.name ?? ""));

  if (cod.length === 0) return NO_CHANGES;

  // Never strand the buyer. If COD were somehow the only method available,
  // hiding it would leave a checkout with nothing to pay by — worse than
  // allowing an order we can follow up on.
  if (cod.length >= methods.length) return NO_CHANGES;

  return {
    operations: cod.map((m) => ({
      paymentMethodHide: { paymentMethodId: m.id },
    })),
  };
}
