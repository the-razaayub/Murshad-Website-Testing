from bs4 import BeautifulSoup
from pathlib import Path
root=Path('/tmp/mur')

# menu.js fixes and card redesign
p=root/'menu.js'; s=p.read_text()
s=s.replace('function changeQty(k,d){const c=loadCart(),x=c.find(i=>i.key===k);if(!x)return;x.qty+=d;saveCart(x.qty>0?c.filter(i=>i.key!==k):c.filter(i=>i.key!==k))}',
'''function changeQty(k,d){const c=loadCart(),x=c.find(i=>i.key===k);if(!x)return;x.qty+=d;saveCart(x.qty>0?c:c.filter(i=>i.key!==k))}''')
s=s.replace('function addToCart(id,size){const i=MENU.find(x=>x.id===id);if(!i)return;const c=loadCart(),k=key(i,size),f=c.find(x=>x.key===k),p=priceOf(i,size);if(f)f.qty++;else c.push({key:k,id:i.id,name:i.name,size:size||"",price:p,qty:1});saveCart(c);openCart()}',
'''function addToCart(id,size){const i=MENU.find(x=>x.id===id);if(!i)return;const c=loadCart(),k=key(i,size),f=c.find(x=>x.key===k),p=priceOf(i,size);if(f)f.qty++;else c.push({key:k,id:i.id,name:i.name,size:size||"",price:p,qty:1});saveCart(c)}''')
s=s.replace('—','-')
old='''function card(i,source='menu',featured=false){\n  const hasSizes=!!i.sizes;\n  const priceText=hasSizes?`From ${money(Math.min(...Object.values(i.sizes)))}`:money(i.price);\n  const options=hasSizes?`<select class="size-select" id="size-${esc(i.id)}" aria-label="Choose size for ${esc(i.name)}">${Object.entries(i.sizes).map(([size,p])=>`<option value="${esc(size)}">${esc(size)} - ${money(p)}</option>`).join("")}</select>`:"";\n  return `<article class="food-card menu-card" data-item-id="${esc(i.id)}">\n    <div class="food-image-wrap"><img class="food-image" src="${esc(i.image||`assets/menu/${i.id}.svg`)}" alt="${esc(i.name)} placeholder"></div>\n    <div class="food-content">\n      <div class="food-title"><h3>${esc(i.name)}</h3><span>${priceText}</span></div>\n      ${i.description?`<p>${esc(i.description)}</p>`:""}\n      <div class="food-actions">${options}<button class="btn btn-green" onclick="addFromCard('${esc(i.id)}')">Add to Cart</button><button class="btn btn-outline" onclick="directWhatsApp('${esc(i.id)}','${esc(source)}')">WhatsApp</button></div>\n    </div>\n  </article>`;\n}'''
new='''function card(i,source='menu',featured=false){\n  const hasSizes=!!i.sizes;\n  const priceText=hasSizes?`From ${money(Math.min(...Object.values(i.sizes)))}`:money(i.price);\n  const options=hasSizes?`<div class="size-row"><label for="size-${esc(i.id)}">Size</label><select class="size-select" id="size-${esc(i.id)}" aria-label="Choose size for ${esc(i.name)}">${Object.entries(i.sizes).map(([size,p])=>`<option value="${esc(size)}">${esc(size)} - ${money(p)}</option>`).join("")}</select></div>`:"";\n  return `<article class="food-card menu-card" data-item-id="${esc(i.id)}">\n    <div class="food-image-wrap"><img class="food-image" src="${esc(i.image||`assets/menu/${i.id}.svg`)}" alt="${esc(i.name)} placeholder"></div>\n    <div class="food-content">\n      <div class="food-title"><h3>${esc(i.name)}</h3><span>${priceText}</span></div>\n      ${i.description?`<p>${esc(i.description)}</p>`:""}\n      ${options}\n      <div class="food-actions"><button class="btn btn-green" onclick="addFromCard('${esc(i.id)}')">Add to Cart</button><button class="btn btn-red" onclick="directWhatsApp('${esc(i.id)}','${esc(source)}')">Order Now</button></div>\n    </div>\n  </article>`;\n}'''
if old not in s: raise SystemExit('card block not found')
s=s.replace(old,new)
p.write_text(s)

# home static cards: normalize every food-card action area
p=root/'index.html'; html=p.read_text(); soup=BeautifulSoup(html,'html.parser')
for card in soup.select('.food-card'):
    # identify item id from any directWhatsApp/addFromCard handler
    onclicks=[x.get('onclick','') for x in card.select('[onclick]')]
    item_id=None
    for oc in onclicks:
        import re
        m=re.search(r"(?:directWhatsApp|addFromCard)\('([^']+)'",oc)
        if m: item_id=m.group(1); break
    if not item_id: continue
    actions=card.select_one('.food-actions')
    if not actions: continue
    sel=actions.select_one('.size-select')
    # retain the existing size select, but move it above the buttons
    actions.clear()
    if sel:
        wrap=soup.new_tag('div',attrs={'class':'size-row'})
        lab=soup.new_tag('label',attrs={'for':sel.get('id','')}); lab.string='Size'
        wrap.append(lab); wrap.append(sel); card.select_one('.food-content').insert(-1,wrap)
        # reselect actions after insertion
        actions=card.select_one('.food-actions')
    add=soup.new_tag('button',attrs={'class':'btn btn-green','onclick':f"addFromCard('{item_id}')"}); add.string='Add to Cart'
    order=soup.new_tag('button',attrs={'class':'btn btn-red','onclick':f"directWhatsApp('{item_id}','featured menu')"}); order.string='Order Now'
    actions.append(add); actions.append(order)
# Replace em dashes across text/attrs
for t in soup.find_all(string=True):
    if '—' in t: t.replace_with(t.replace('—','-'))
for tag in soup.find_all(True):
    for k,v in list(tag.attrs.items()):
        if isinstance(v,str) and '—' in v: tag.attrs[k]=v.replace('—','-')
# hero: use transparent logo as the actual heading
hero=soup.select_one('.hero-grid > div:first-child')
if hero:
    for x in hero.select('.eyebrow'): x.decompose()
    h=hero.select_one('h1')
    if h:
        h.clear(); h['class']=['hero-brand-heading']
        img=soup.new_tag('img',src='assets/murshad-logo-transparent.png',alt='Murshad Restaurant and Pizza Crust')
        h.append(img)
p.write_text(str(soup),encoding='utf-8')

# other html em dash cleanup
for fn in ['fast-food.html','desi-items.html','admin.html']:
    p=root/fn; txt=p.read_text(); p.write_text(txt.replace('—','-'))
