/* ============================================================
   KORDOVAN LEATHER — Theme JavaScript
   ============================================================ */

'use strict';

// ============================================================
// UTILITIES
// ============================================================
const KDV = {
  utils: {
    formatMoney(cents, format) {
      const value = (cents / 100).toFixed(0);
      return `PKR ${Number(value).toLocaleString()}`;
    },
    debounce(fn, delay = 300) {
      let timer;
      return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), delay);
      };
    },
    fetchJSON(url, options = {}) {
      return fetch(url, {
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        ...options
      }).then(r => r.json());
    }
  }
};

// ============================================================
// ANNOUNCEMENT BAR
// ============================================================
class AnnouncementBar {
  constructor(el) {
    this.el = el;
    this.closeBtn = el.querySelector('.announcement-bar__close');
    this.storageKey = 'kdv-announcement-closed';
    this.init();
  }

  init() {
    if (sessionStorage.getItem(this.storageKey)) {
      this.el.remove();
      return;
    }
    this.closeBtn?.addEventListener('click', () => this.close());
    this.startMarquee();
  }

  close() {
    sessionStorage.setItem(this.storageKey, '1');
    this.el.style.height = this.el.offsetHeight + 'px';
    requestAnimationFrame(() => {
      this.el.style.transition = 'height 300ms ease, opacity 300ms ease';
      this.el.style.height = '0';
      this.el.style.overflow = 'hidden';
      this.el.style.opacity = '0';
    });
    setTimeout(() => this.el.remove(), 320);
  }

  startMarquee() {
    const track = this.el.querySelector('.announcement-bar__track');
    if (!track) return;
    const items = track.querySelectorAll('.announcement-bar__item');
    if (items.length <= 1) return;

    let current = 0;
    setInterval(() => {
      items[current].style.opacity = '0';
      items[current].style.transform = 'translateY(-8px)';
      current = (current + 1) % items.length;
      setTimeout(() => {
        items.forEach((item, i) => {
          item.style.display = i === current ? 'block' : 'none';
          item.style.opacity = '1';
          item.style.transform = 'translateY(0)';
        });
      }, 300);
    }, 4000);

    items.forEach((item, i) => {
      item.style.transition = 'opacity 300ms ease, transform 300ms ease';
      if (i > 0) item.style.display = 'none';
    });
  }
}

// ============================================================
// HEADER — Scroll behaviour + Mobile menu
// ============================================================
class SiteHeader {
  constructor(el) {
    this.el = el;
    this.hamburger = document.querySelector('.header__hamburger');
    this.mobileMenu = document.querySelector('.mobile-menu');
    this.mobileClose = document.querySelector('.mobile-menu__close');
    this.overlay = document.querySelector('.mobile-menu-overlay');
    this.isTransparent = el.classList.contains('header--transparent');
    this.init();
  }

  init() {
    this.onScroll();
    window.addEventListener('scroll', () => this.onScroll(), { passive: true });
    this.hamburger?.addEventListener('click', () => this.openMenu());
    this.mobileClose?.addEventListener('click', () => this.closeMenu());
    this.overlay?.addEventListener('click', () => this.closeMenu());
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') this.closeMenu();
    });
  }

  onScroll() {
    const scrolled = window.scrollY > 50;
    this.el.classList.toggle('scrolled', scrolled);
  }

  openMenu() {
    this.mobileMenu?.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    this.hamburger?.setAttribute('aria-expanded', 'true');
  }

  closeMenu() {
    this.mobileMenu?.classList.remove('is-open');
    document.body.style.overflow = '';
    this.hamburger?.setAttribute('aria-expanded', 'false');
  }
}

// ============================================================
// PRODUCT GALLERY
// ============================================================
class ProductGallery {
  constructor(el) {
    this.el = el;
    this.mainImg = el.querySelector('.product-gallery__main img');
    this.thumbs = el.querySelectorAll('.product-gallery__thumb');
    this.currentIndex = 0;
    this.init();
  }

  init() {
    this.thumbs.forEach((thumb, i) => {
      thumb.addEventListener('click', () => this.goTo(i));
    });

    // Touch swipe on main image
    let startX = 0;
    this.mainImg?.addEventListener('touchstart', e => {
      startX = e.changedTouches[0].clientX;
    }, { passive: true });
    this.mainImg?.addEventListener('touchend', e => {
      const diff = startX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        diff > 0 ? this.next() : this.prev();
      }
    }, { passive: true });
  }

  goTo(index) {
    const thumb = this.thumbs[index];
    if (!thumb) return;
    const src = thumb.dataset.full || thumb.querySelector('img')?.src;
    if (!src || !this.mainImg) return;

    this.mainImg.style.opacity = '0';
    setTimeout(() => {
      this.mainImg.src = src;
      this.mainImg.style.opacity = '1';
    }, 150);

    this.thumbs[this.currentIndex]?.classList.remove('active');
    thumb.classList.add('active');
    this.currentIndex = index;
  }

  next() { this.goTo((this.currentIndex + 1) % this.thumbs.length); }
  prev() { this.goTo((this.currentIndex - 1 + this.thumbs.length) % this.thumbs.length); }
}

// ============================================================
// VARIANT SELECTOR
// ============================================================
class VariantSelector {
  constructor(el) {
    this.form = el;
    this.variantInput = el.querySelector('input[name="id"]');
    this.variantButtons = el.querySelectorAll('.variant-btn');
    this.addToCartBtn = el.querySelector('.product-atc__add');
    this.priceEl = el.querySelector('.product-info__price-current');
    this.comparePriceEl = el.querySelector('.product-info__price-compare');
    this.savePriceEl = el.querySelector('.product-info__price-save');
    this.selectedEls = el.querySelectorAll('.product-variants__selected');

    // Read variants from JSON in page
    const variantsData = el.querySelector('[data-product-variants]');
    this.variants = variantsData ? JSON.parse(variantsData.textContent) : [];
    this.currentVariant = this.variants[0] || null;

    this.init();
  }

  init() {
    this.variantButtons.forEach(btn => {
      btn.addEventListener('click', () => this.handleVariantClick(btn));
    });
  }

  handleVariantClick(btn) {
    const group = btn.closest('.product-variants__options');
    group?.querySelectorAll('.variant-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // Update selected label
    const labelEl = btn.closest('.product-variants')?.querySelector('.product-variants__selected');
    if (labelEl) labelEl.textContent = btn.textContent.trim();

    this.findVariant();
  }

  findVariant() {
    const selectedOptions = [];
    this.form.querySelectorAll('.product-variants').forEach(group => {
      const active = group.querySelector('.variant-btn.active');
      if (active) selectedOptions.push(active.dataset.value);
    });

    const match = this.variants.find(v =>
      v.options.every((opt, i) => opt === selectedOptions[i])
    );

    if (match) {
      this.currentVariant = match;
      this.updatePrice(match);
      this.updateAvailability(match);
      if (this.variantInput) this.variantInput.value = match.id;
      // Update URL without reload
      const url = new URL(window.location.href);
      url.searchParams.set('variant', match.id);
      window.history.replaceState({}, '', url.toString());
    }
  }

  updatePrice(variant) {
    if (!this.priceEl) return;
    const price = KDV.utils.formatMoney(variant.price);
    this.priceEl.textContent = price;

    if (variant.compare_at_price && variant.compare_at_price > variant.price) {
      this.priceEl.classList.add('is-sale');
      if (this.comparePriceEl) {
        this.comparePriceEl.textContent = KDV.utils.formatMoney(variant.compare_at_price);
        this.comparePriceEl.style.display = '';
      }
      if (this.savePriceEl) {
        const saving = Math.round((1 - variant.price / variant.compare_at_price) * 100);
        this.savePriceEl.textContent = `Save ${saving}%`;
        this.savePriceEl.style.display = '';
      }
    } else {
      this.priceEl.classList.remove('is-sale');
      if (this.comparePriceEl) this.comparePriceEl.style.display = 'none';
      if (this.savePriceEl) this.savePriceEl.style.display = 'none';
    }
  }

  updateAvailability(variant) {
    if (!this.addToCartBtn) return;
    if (variant.available) {
      this.addToCartBtn.disabled = false;
      this.addToCartBtn.textContent = 'Add to Cart';
    } else {
      this.addToCartBtn.disabled = true;
      this.addToCartBtn.textContent = 'Sold Out';
    }
  }
}

// ============================================================
// ADD TO CART
// ============================================================
class AddToCart {
  constructor(form) {
    this.form = form;
    this.btn = form.querySelector('.product-atc__add');
    this.qtyInput = form.querySelector('.product-atc__qty-input');
    this.cartCount = document.querySelector('.header__cart-count');
    this.init();
  }

  init() {
    this.form.addEventListener('submit', e => {
      e.preventDefault();
      this.submit();
    });

    // Quantity buttons
    this.form.querySelectorAll('.product-atc__qty-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const delta = btn.dataset.action === 'plus' ? 1 : -1;
        const current = parseInt(this.qtyInput?.value || 1);
        const next = Math.max(1, current + delta);
        if (this.qtyInput) this.qtyInput.value = next;
      });
    });
  }

  async submit() {
    if (!this.btn) return;
    const variantId = this.form.querySelector('input[name="id"]')?.value;
    const qty = parseInt(this.qtyInput?.value || 1);
    if (!variantId) return;

    const originalText = this.btn.textContent;
    this.btn.classList.add('loading');
    this.btn.textContent = 'Adding...';

    try {
      const data = await KDV.utils.fetchJSON('/cart/add.js', {
        method: 'POST',
        body: JSON.stringify({ id: variantId, quantity: qty })
      });

      this.btn.textContent = 'Added! ✓';
      this.btn.style.backgroundColor = 'var(--color-success)';
      this.btn.style.borderColor = 'var(--color-success)';
      this.updateCartCount();
      CartDrawer.instance?.open();

      setTimeout(() => {
        this.btn.textContent = originalText;
        this.btn.style.backgroundColor = '';
        this.btn.style.borderColor = '';
      }, 2000);
    } catch (err) {
      this.btn.textContent = 'Error — Try Again';
      setTimeout(() => { this.btn.textContent = originalText; }, 2000);
    } finally {
      this.btn.classList.remove('loading');
    }
  }

  async updateCartCount() {
    try {
      const cart = await KDV.utils.fetchJSON('/cart.js');
      if (this.cartCount) {
        this.cartCount.textContent = cart.item_count;
        this.cartCount.style.display = cart.item_count > 0 ? 'flex' : 'none';
      }
    } catch {}
  }
}

// ============================================================
// CART DRAWER
// ============================================================
class CartDrawer {
  static instance = null;

  constructor(el) {
    this.el = el;
    this.overlay = document.querySelector('.cart-drawer-overlay');
    this.closeBtn = el.querySelector('.cart-drawer__close');
    this.itemsContainer = el.querySelector('.cart-drawer__items');
    this.totalEl = el.querySelector('.cart-drawer__total');
    CartDrawer.instance = this;
    this.init();
  }

  init() {
    this.closeBtn?.addEventListener('click', () => this.close());
    this.overlay?.addEventListener('click', () => this.close());
    document.querySelector('.header__cart-btn')?.addEventListener('click', () => {
      this.open();
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') this.close();
    });
  }

  async open() {
    await this.refresh();
    this.el.classList.add('is-open');
    this.overlay?.classList.add('is-visible');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.el.classList.remove('is-open');
    this.overlay?.classList.remove('is-visible');
    document.body.style.overflow = '';
  }

  async refresh() {
    try {
      const cart = await KDV.utils.fetchJSON('/cart.js');
      this.render(cart);
    } catch {}
  }

  render(cart) {
    if (!this.itemsContainer) return;

    if (cart.item_count === 0) {
      this.itemsContainer.innerHTML = `
        <div class="cart-drawer__empty">
          <p>Your cart is empty.</p>
          <a href="/collections/all" class="btn btn--primary btn--sm">Shop Now</a>
        </div>
      `;
      if (this.totalEl) this.totalEl.textContent = '';
      return;
    }

    this.itemsContainer.innerHTML = cart.items.map(item => `
      <div class="cart-drawer__item" data-key="${item.key}">
        <a href="${item.url}">
          <img src="${item.image}" alt="${item.product_title}" width="80" height="96">
        </a>
        <div class="cart-drawer__item-info">
          <a href="${item.url}" class="cart-drawer__item-title">${item.product_title}</a>
          <p class="cart-drawer__item-variant">${item.variant_title !== 'Default Title' ? item.variant_title : ''}</p>
          <div class="cart-drawer__item-footer">
            <div class="cart-item__qty">
              <button class="cart-item__qty-btn" data-action="minus" data-key="${item.key}">−</button>
              <span class="cart-drawer__qty">${item.quantity}</span>
              <button class="cart-item__qty-btn" data-action="plus" data-key="${item.key}">+</button>
            </div>
            <span class="cart-drawer__item-price">${KDV.utils.formatMoney(item.line_price)}</span>
          </div>
        </div>
      </div>
    `).join('');

    if (this.totalEl) {
      this.totalEl.innerHTML = `
        <span>Subtotal</span>
        <span>${KDV.utils.formatMoney(cart.total_price)}</span>
      `;
    }

    // Attach qty change handlers
    this.itemsContainer.querySelectorAll('.cart-item__qty-btn').forEach(btn => {
      btn.addEventListener('click', () => this.updateQty(btn.dataset.key, btn.dataset.action));
    });
  }

  async updateQty(key, action) {
    try {
      const cart = await KDV.utils.fetchJSON('/cart.js');
      const item = cart.items.find(i => i.key === key);
      if (!item) return;
      const newQty = action === 'plus' ? item.quantity + 1 : Math.max(0, item.quantity - 1);
      const updated = await KDV.utils.fetchJSON('/cart/change.js', {
        method: 'POST',
        body: JSON.stringify({ id: key, quantity: newQty })
      });
      this.render(updated);
      // Update header count
      const countEl = document.querySelector('.header__cart-count');
      if (countEl) {
        countEl.textContent = updated.item_count;
        countEl.style.display = updated.item_count > 0 ? 'flex' : 'none';
      }
    } catch {}
  }
}

// ============================================================
// PRODUCT TABS
// ============================================================
class ProductTabs {
  constructor(el) {
    this.el = el;
    this.btns = el.querySelectorAll('.product-tabs__btn');
    this.panels = el.querySelectorAll('.product-tabs__panel');
    this.init();
  }

  init() {
    this.btns.forEach(btn => {
      btn.addEventListener('click', () => this.show(btn.dataset.tab));
    });
  }

  show(tabId) {
    this.btns.forEach(b => b.classList.toggle('active', b.dataset.tab === tabId));
    this.panels.forEach(p => p.classList.toggle('active', p.id === tabId));
  }
}

// ============================================================
// SCROLL FADE-IN
// ============================================================
class ScrollAnimator {
  constructor() {
    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            this.observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    document.querySelectorAll('.fade-in').forEach(el => this.observer.observe(el));
  }
}

// ============================================================
// QUICK ADD
// ============================================================
class QuickAdd {
  static async add(variantId, qty = 1) {
    try {
      await KDV.utils.fetchJSON('/cart/add.js', {
        method: 'POST',
        body: JSON.stringify({ id: variantId, quantity: qty })
      });
      CartDrawer.instance?.open();
      const countEl = document.querySelector('.header__cart-count');
      if (countEl) {
        const cart = await KDV.utils.fetchJSON('/cart.js');
        countEl.textContent = cart.item_count;
        countEl.style.display = 'flex';
      }
    } catch {}
  }
}

// Quick Add buttons on collection pages
document.addEventListener('click', async (e) => {
  const btn = e.target.closest('.product-card__quick-add');
  if (!btn) return;
  e.preventDefault();
  const variantId = btn.dataset.variantId;
  if (!variantId) return;
  btn.textContent = 'Adding...';
  await QuickAdd.add(variantId);
  btn.textContent = 'Added! ✓';
  setTimeout(() => { btn.textContent = 'Quick Add'; }, 2000);
});

// ============================================================
// EMAIL SIGNUP
// ============================================================
class EmailSignup {
  constructor(form) {
    this.form = form;
    this.input = form.querySelector('.email-capture__input');
    this.submit = form.querySelector('.email-capture__submit');
    this.init();
  }

  init() {
    this.form.addEventListener('submit', e => {
      e.preventDefault();
      this.handleSubmit();
    });
  }

  handleSubmit() {
    const email = this.input?.value?.trim();
    if (!email || !email.includes('@')) {
      this.showError('Please enter a valid email address.');
      return;
    }
    // Shopify handles via the form action — let it submit naturally
    this.form.submit();
  }

  showError(msg) {
    let err = this.form.querySelector('.email-error');
    if (!err) {
      err = document.createElement('p');
      err.className = 'email-error';
      err.style.cssText = 'color:var(--color-bg);font-size:0.75rem;margin-top:0.5rem;text-align:center;';
      this.form.appendChild(err);
    }
    err.textContent = msg;
  }
}

// ============================================================
// CART PAGE — INLINE QTY UPDATE
// ============================================================
class CartPage {
  constructor() {
    this.init();
  }

  init() {
    document.querySelectorAll('.cart-item__qty-btn').forEach(btn => {
      btn.addEventListener('click', () => this.updateItem(btn));
    });
    document.querySelectorAll('.cart-item__remove').forEach(btn => {
      btn.addEventListener('click', () => this.removeItem(btn));
    });
  }

  async updateItem(btn) {
    const item = btn.closest('.cart-item');
    const key = item?.dataset.key;
    const qtyEl = item?.querySelector('.cart-item__qty-input');
    if (!key || !qtyEl) return;

    const delta = btn.dataset.action === 'plus' ? 1 : -1;
    const newQty = Math.max(0, parseInt(qtyEl.value) + delta);
    qtyEl.value = newQty;

    try {
      await KDV.utils.fetchJSON('/cart/change.js', {
        method: 'POST',
        body: JSON.stringify({ id: key, quantity: newQty })
      });
      if (newQty === 0) {
        item.remove();
      }
      this.refreshTotals();
    } catch {}
  }

  async removeItem(btn) {
    const item = btn.closest('.cart-item');
    const key = item?.dataset.key;
    if (!key) return;
    try {
      await KDV.utils.fetchJSON('/cart/change.js', {
        method: 'POST',
        body: JSON.stringify({ id: key, quantity: 0 })
      });
      item.style.opacity = '0';
      item.style.transform = 'translateX(-20px)';
      item.style.transition = 'all 300ms ease';
      setTimeout(() => { item.remove(); this.refreshTotals(); }, 300);
    } catch {}
  }

  async refreshTotals() {
    try {
      const cart = await KDV.utils.fetchJSON('/cart.js');
      const totalEl = document.querySelector('.cart-summary__total-price');
      if (totalEl) totalEl.textContent = KDV.utils.formatMoney(cart.total_price);
      const countEl = document.querySelector('.header__cart-count');
      if (countEl) {
        countEl.textContent = cart.item_count;
        countEl.style.display = cart.item_count > 0 ? 'flex' : 'none';
      }
    } catch {}
  }
}

// ============================================================
// INIT ON DOM READY
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
  // Announcement bar
  const announcementEl = document.querySelector('.announcement-bar');
  if (announcementEl) new AnnouncementBar(announcementEl);

  // Header
  const headerEl = document.querySelector('.site-header');
  if (headerEl) new SiteHeader(headerEl);

  // Product gallery
  const galleryEl = document.querySelector('.product-gallery');
  if (galleryEl) new ProductGallery(galleryEl);

  // Variant selectors
  const productForm = document.querySelector('.product-form');
  if (productForm) {
    new VariantSelector(productForm);
    new AddToCart(productForm);
  }

  // Cart drawer
  const cartDrawerEl = document.querySelector('.cart-drawer');
  if (cartDrawerEl) new CartDrawer(cartDrawerEl);

  // Product tabs
  const tabsEl = document.querySelector('.product-tabs');
  if (tabsEl) new ProductTabs(tabsEl);

  // Email signup
  const emailForm = document.querySelector('.email-capture__form');
  if (emailForm) new EmailSignup(emailForm);

  // Scroll animations
  if ('IntersectionObserver' in window) new ScrollAnimator();

  // Cart page
  if (document.querySelector('.cart-page')) new CartPage();

  // Init cart count on load
  KDV.utils.fetchJSON('/cart.js').then(cart => {
    const countEl = document.querySelector('.header__cart-count');
    if (countEl) {
      countEl.textContent = cart.item_count;
      countEl.style.display = cart.item_count > 0 ? 'flex' : 'none';
    }
  }).catch(() => {});
});
