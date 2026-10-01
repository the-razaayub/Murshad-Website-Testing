from pathlib import Path
root=Path('/mnt/data/v12work')

# Update item modal markup on all menu-enabled pages.
modal_old='''<div class="item-modal-grid"><div class="item-modal-image-wrap"><img alt="" class="item-modal-image" id="itemModalImage" src="assets/menu-placeholder.svg"/></div><div class="item-modal-body"><div class="kicker" id="itemModalCategory">Menu item</div><h2 id="itemModalTitle"></h2><div class="item-modal-price" id="itemModalPrice"></div><p id="itemModalDescription"></p><div id="itemModalSizes"></div><div class="item-modal-actions"><button class="btn btn-green" id="itemModalAdd" type="button">Add to Cart</button><button class="btn btn-red" id="itemModalOrder" type="button">Order Now</button></div></div></div>'''
modal_new='''<div class="item-modal-stack"><div class="item-modal-image-wrap"><img alt="" class="item-modal-image" id="itemModalImage" src="assets/menu-placeholder.svg"/></div><div class="item-modal-body"><div class="kicker" id="itemModalCategory">Menu item</div><h2 id="itemModalTitle"></h2><p id="itemModalDescription"></p><div id="itemModalSizes"></div><div class="item-modal-price-row"><span>Total Price</span><div class="item-modal-price" id="itemModalPrice"></div></div><div class="item-modal-actions"><button class="btn btn-outline-red" id="itemModalAdd" type="button">🛒 Add to Cart</button><button class="btn btn-green" id="itemModalOrder" type="button">◉ Order Now</button></div></div></div>'''
for p in root.glob('*.html'):
    s=p.read_text()
    if modal_old in s:
        s=s.replace(modal_old, modal_new)
    p.write_text(s)

# Replace homepage CTA with reference-style green call-to-action.
p=root/'index.html'; s=p.read_text()
old='''<section class="section"><div class="container"><div class="cta"><div><h2>Have a full order in mind?</h2><p>Add items to your cart and submit online, or send the complete order through WhatsApp.</p></div><a class="btn btn-gold" href="tel:+923361994444">Call Us Now</a></div></div></section>'''
new='''<section class="section cta-section"><div class="container"><div class="cta"><div><h2>Hungry? Order Now</h2><p>Karahi, BBQ, Pulao, Pizza, Burgers &amp; more, delivered to your door.</p><div class="cta-actions"><a class="btn cta-call" href="tel:+923361994444"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M6.6 10.8a15.5 15.5 0 0 0 6.6 6.6l2.2-2.2c.3-.3.8-.4 1.2-.2 1.1.4 2.2.6 3.4.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C11.8 21 3 12.2 3 1.9c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.2.2 2.3.6 3.4.1.4.1.9-.2 1.2l-2.2 2.3z"></path></svg>Call Now</a><a class="btn cta-whatsapp" href="https://wa.me/923361994444?text=Hello%20Murshad%20Restaurant%2C%20I%20want%20to%20place%20an%20order.%20Please%20guide%20me." rel="noopener" target="_blank"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M20.5 3.5A11.8 11.8 0 0 0 12.1 0C5.5 0 .1 5.4.1 12c0 2.1.5 4.2 1.6 6L0 24l6.2-1.6A11.9 11.9 0 0 0 12 24c6.6 0 12-5.4 12-12 0-3.2-1.2-6.2-3.5-8.5zm-8.4 18.3c-1.8 0-3.6-.5-5.1-1.5l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12.1 21.8zm5.4-7.4c-.3-.2-1.8-.9-2.1-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-.9 1.1-.2.2-.3.2-.6.1-.3-.2-1.2-.4-2.3-1.4-.9-.8-1.4-1.8-1.6-2.1-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6-.1-.2-.7-1.7-.9-2.3-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.1 1.1-1.1 2.7s1.1 3.1 1.3 3.3c.2.2 2.2 3.4 5.4 4.7.8.3 1.4.5 1.9.6.8.2 1.5.2 2.1.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.4z"></path></svg>WhatsApp Order</a></div></div></div></section>'''
if old not in s:
    raise SystemExit('CTA target not found')
p.write_text(s.replace(old,new))

# Append V12 CSS so it overrides the accumulated prior refinements cleanly.
css=root/'styles.css'
css_add=r'''

/* V12 reference menu + item preview + persistent checkout bar */
.item-modal-box{width:min(560px,calc(100vw - 28px));max-height:92vh;padding:0;border:2px solid #f0c800;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 28px 80px rgba(0,0,0,.38)}
.item-modal-stack{display:flex;flex-direction:column}
.item-modal-image-wrap{width:100%;height:280px;padding:0;border-radius:0;background:#c91612;overflow:hidden;display:flex;align-items:center;justify-content:center}
.item-modal-image{width:100%;height:100%;aspect-ratio:auto;object-fit:cover;border-radius:0;background:#c91612}
.item-modal-body{padding:22px 34px 28px;background:#fff}
.item-modal-body .kicker{display:none}
.item-modal-body h2{margin:0 0 6px;font-size:31px;line-height:1.08;color:#252525}
.item-modal-body p{margin:0 0 16px;color:#687385;font-size:16px;line-height:1.45}
.item-modal-price-row{display:flex;align-items:center;justify-content:space-between;gap:12px;border-top:1px solid #e7e7e7;padding-top:18px;margin-top:18px}
.item-modal-price-row>span{font-size:16px;color:#687385}
.item-modal-price{margin:0;color:var(--red);font-size:29px;font-weight:950}
.item-modal-actions{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}
.item-modal-actions .btn{min-height:58px;border-radius:16px;font-size:16px}
.btn-outline-red{background:#fff;color:var(--red);border:2px solid var(--red)}
.item-modal-body #itemModalSizes{display:grid;gap:12px}
.item-modal-body .size-row,.item-modal-body .choice-row{display:grid;gap:7px;margin:0}
.item-modal-body .size-row label,.item-modal-body .choice-row label{font-size:15px;font-weight:900;color:#272727}
.item-modal-body .size-select{height:58px;border:2px solid #dfe3e8;border-radius:13px;background:#fff;padding:9px 12px;font-size:14px}
.item-modal-close{right:12px;top:12px;width:42px;height:42px;background:#fff;color:#222;font-size:22px;box-shadow:0 4px 12px rgba(0,0,0,.12)}

/* Card footprint stays at the established V11 size; only content is more prominent. */
#murshad-menu .food-card,.vertical-menu-card,#searchResults .vertical-menu-card{grid-template-columns:minmax(0,65fr) minmax(145px,35fr);min-height:155px;height:155px}
#murshad-menu .food-title h3,.vertical-menu-card .food-title h3{font-size:21px}
#murshad-menu .food-content>p,.vertical-menu-card .food-content p{font-size:15px;line-height:1.38}
#murshad-menu .food-price,.vertical-menu-card .food-price{font-size:20px}
#murshad-menu .add-card-btn,.vertical-menu-card .add-card-btn{min-height:40px;padding:8px 15px;font-size:14px}

/* Persistent checkout bar: hidden until the cart contains an item. */
.persistent-checkout{position:fixed;left:50%;bottom:10px;transform:translateX(-50%);width:min(575px,calc(100vw - 28px));min-height:68px;background:#0d8f45;color:#fff;border:2px solid #f2c900;border-radius:999px;z-index:110;display:grid;grid-template-columns:1.05fr .8fr 1.15fr;align-items:center;box-shadow:0 12px 30px rgba(0,0,0,.24);overflow:hidden}
.persistent-checkout[hidden]{display:none}
.persistent-checkout .pc-segment{min-width:0;height:42px;display:flex;align-items:center;justify-content:center;padding:0 16px;font-weight:950}
.persistent-checkout .pc-segment+.pc-segment{border-left:2px solid rgba(255,255,255,.35)}
.persistent-checkout .pc-count{gap:9px;color:#fff}
.persistent-checkout .pc-cart-icon{width:22px;height:22px;fill:none;stroke:var(--gold);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.persistent-checkout .pc-total{color:var(--gold);white-space:nowrap}
.persistent-checkout .pc-action{color:#fff;background:transparent;border:0;font:inherit;cursor:pointer;white-space:nowrap}
.persistent-checkout .pc-action:hover{background:rgba(255,255,255,.07)}

/* Reference green order section */
.cta-section{padding-top:0;padding-bottom:0;background:transparent}
.cta-section .container{width:100%;max-width:none}
.cta{border-radius:0;border-bottom:4px solid var(--gold);padding:54px 5%;min-height:310px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:#0b8a3e}
.cta h2{font-size:clamp(38px,4vw,58px);margin:0 0 8px;color:#fff}
.cta p{font-size:20px;line-height:1.45;margin:0;color:#fff}
.cta-actions{display:flex;justify-content:center;gap:18px;margin-top:28px;flex-wrap:wrap}
.cta-actions .btn{min-width:195px;min-height:58px;border-radius:999px;font-size:17px}
.cta-call{background:#fff;color:#087b38}
.cta-whatsapp{background:var(--gold);color:#151515}
.cta-actions svg{width:22px;height:22px;fill:currentColor}

@media(max-width:700px){
  .item-modal-box{width:calc(100vw - 20px);max-height:94vh;border-radius:19px}
  .item-modal-image-wrap{height:220px}
  .item-modal-body{padding:18px 18px 20px}
  .item-modal-body h2{font-size:27px}
  .item-modal-body p{font-size:14px}
  .item-modal-actions{grid-template-columns:1fr 1fr;gap:8px}
  .item-modal-actions .btn{min-height:52px;font-size:14px;padding:8px 7px}
  .persistent-checkout{bottom:7px;min-height:60px;width:calc(100vw - 18px)}
  .persistent-checkout .pc-segment{height:38px;padding:0 8px;font-size:12px}
  .persistent-checkout .pc-cart-icon{width:18px;height:18px}
  .cta{min-height:330px;padding:42px 18px}
  .cta h2{font-size:39px}
  .cta p{font-size:16px}
  .cta-actions{width:100%;gap:10px}
  .cta-actions .btn{width:100%;min-width:0}
}
'''
css.write_text(css.read_text()+css_add)

# Inject persistent checkout bar markup before footer on pages that have the cart drawer.
bar='''<div class="persistent-checkout" id="persistentCheckout" hidden><div class="pc-segment pc-count"><svg class="pc-cart-icon" aria-hidden="true" viewBox="0 0 24 24"><path d="M3 4h2l2.1 10.1a2 2 0 0 0 2 1.6h7.8a2 2 0 0 0 1.9-1.4L21 7H6"></path><circle cx="10" cy="20" r="1.5"></circle><circle cx="18" cy="20" r="1.5"></circle></svg><span id="persistentCheckoutCount">0 Items</span></div><div class="pc-segment pc-total" id="persistentCheckoutTotal">Rs. 0</div><button class="pc-segment pc-action" type="button" onclick="openCheckout()">Checkout →</button></div>'''
for p in root.glob('*.html'):
    s=p.read_text()
    if 'id="cartDrawer"' in s and 'id="persistentCheckout"' not in s:
        marker='<div aria-hidden="true" class="modal" id="checkoutModal">'
        if marker in s:
            s=s.replace(marker, bar+'\n'+marker, 1)
            p.write_text(s)

# Patch cart rendering to update persistent bar on every cart mutation.
js=root/'menu.js'; s=js.read_text()
s=s.replace('''function renderCartBadge(){const n=loadCart().reduce((s,i)=>s+i.qty,0);document.querySelectorAll("[data-cart-count]").forEach(x=>x.textContent=n)}''','''function renderCartBadge(){const c=loadCart(),n=c.reduce((s,i)=>s+i.qty,0),total=c.reduce((s,i)=>s+i.price*i.qty,0);document.querySelectorAll("[data-cart-count]").forEach(x=>x.textContent=n);const bar=document.querySelector('#persistentCheckout'),count=document.querySelector('#persistentCheckoutCount'),sum=document.querySelector('#persistentCheckoutTotal');if(bar){bar.hidden=n===0;if(count)count.textContent=`${n} ${n===1?'Item':'Items'}`;if(sum)sum.textContent=money(total)}}''')
# Ensure modal price displays selected size immediately and on changes.
old='''sizes.innerHTML=html;if(!m.classList.contains('open'))history.pushState({murshadModal:'item'},'',location.href);m.classList.add('open');m.setAttribute('aria-hidden','false');document.body.style.overflow='hidden'}'''
new='''sizes.innerHTML=html;const refreshModalPrice=()=>{const chosen=i.sizes?document.querySelector('#itemModalSize')?.value||Object.keys(i.sizes)[0]:'';const p=priceOf(i,chosen);document.querySelector('#itemModalPrice').textContent=money(p)};document.querySelector('#itemModalSize')?.addEventListener('change',refreshModalPrice);refreshModalPrice();if(!m.classList.contains('open'))history.pushState({murshadModal:'item'},'',location.href);m.classList.add('open');m.setAttribute('aria-hidden','false');document.body.style.overflow='hidden'}'''
if old not in s:
    raise SystemExit('modal JS target not found')
s=s.replace(old,new)
js.write_text(s)
