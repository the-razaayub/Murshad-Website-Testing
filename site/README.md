# Murshad Restaurant and Pizza Crust

Responsive restaurant website built from the supplied logo and menu.

## Main pages
- index.html — home, auto slider, featured menu, service options
- fast-food.html — complete fast-food menu grouped by category
- desi-items.html — complete desi menu grouped by category
- admin.html — local demo order view

## Replaceable images
- assets/placeholders/fast-food/<category>/ and assets/placeholders/desi-items/<category>/ - one folder per menu category (20 folders), one 900x600 (3:2) JPG per item, named after the item.
- assets/placeholders/slider/slider-2.jpg ... slider-5.jpg - homepage slider, 1600x650.
- assets/placeholders/coming-soon.jpg - shown automatically if any image file is missing.
- assets/placeholders/PLACEHOLDER_LIST.csv - full list (open in Excel): item, file, ratio, size.
- Keep the SAME file name and .jpg extension when replacing. assets/hero-food.jpg (slide 1) and story-food.jpg are real photos.
- Logos: assets/murshad-*.png

## Ordering
Cart data is stored only in the customer's browser. WhatsApp buttons open pre-filled messages. The website checkout can POST to a backend through config.js. Without a backend endpoint, checkout is demo/local only.

See START_HERE.docx for beginner-friendly publishing, testing and backend instructions.
