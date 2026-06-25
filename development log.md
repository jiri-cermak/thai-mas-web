# Development Log — thai-mas-web

## April 27, 2026

**[DESIGN]** Color & font analysis of V3 mockup
- Analyzed existing palette: cream `#F9F4F0`, burgundy `#81053D`, gold `#D4AF37`, dark gray `#2D2D2D`.
- Typography: Playfair Display (headings) + Roboto Condensed (body).

**[DESIGN]** Gold proportion comparison V1 vs V3
- Compared gold usage ratio between `gemini mockup 27. dubna 2026 V1.html` and V3.
- V1 uses gold as a primary color (logo, subtitle, CTA button, card headings).
- V3 uses gold only as an accent (borders, hover states).
- Conclusion: V3 has ~3× less gold surface area than V1.

**[FEAT]** Created V4 mockup — `gemini mockup 27. dubna 2026 V4.html`
- CTA button: changed from burgundy bg to **gold bg `#D4AF37` with burgundy text `#81053D`**.
- CTA hover: burgundy bg with cream text.
- Reduced whitespace around H1 and CTA:
  - Hero top padding: `100px` → `60px`
  - Hero bottom padding: `120px` → `70px`
  - H1 bottom margin: `20px` → `10px`
  - Paragraph bottom margin (above CTA): `40px` → `24px`

**[FEAT]** Built live site from original content
- Scraped Czech text from `https://www.thajskemasaze-trebon.cz/`.
- Created `index.html` (homepage) and `cenik.html` (pricing) based on V4 design.
- Content included: hero motto, introduction paragraph, 5 massage services, full pricing tables, contact info, opening hours.
- Navigation: Úvodní stránka, Ceník.

**[FEAT]** Integrated real images from original site
- Retrieved `garuda.png` (site icon/logo) and `bg.jpg` (hero background banner).
- Replaced header text logo with Garuda icon (`60px` height, links to home).
- Replaced Unsplash hero background with the site's actual gold botanical banner.
- Removed dark gradient overlay to let the gold image dominate.
- Added subtle light text-shadow to hero text for readability on bright gold.

**[DOCS]** Created project documentation
- `development log.md` (this file) — tracks all design decisions and version changes.
- `agent.md` — defines the visual-design-helper agent persona for this folder.

---

### April 27, 2026 (fork)

**[FEAT]** Forked alternative design — "jana" variant
- Created `index_jana.html` and `cenik_jana.html` without overwriting the main site.
- **Geometry guide:** `gemini mockup 27. dubna 2026 V1.html`
  - Centered hero layout with cream gradient overlay over background image.
  - Flexbox services row with fixed-width cards (250px), white bg, rounded corners (15px), shadow.
  - Pill-shaped CTA button (50px border-radius).
  - Header with gold bottom border, uppercase navigation (14px).
  - Centered single-column footer (padding 40px).
- **Colors & fonts:** from pre-fork version (current site)
  - Palette: cream `#F9F4F0`, burgundy `#81053D`, gold `#D4AF37`, body `#2D2D2D`.
  - Fonts: Playfair Display (headings) + Roboto Condensed (body).
  - CTA: gold bg with burgundy text; hover: burgundy bg with cream text + lift effect.
- **Background image:** retrieved the Unsplash spa photo from V1 (`bg_jana.jpg`), used with the same gradient-overlay technique.
- **Content:** all Czech text and site structure from the scraped original website (not from V1).
- **Logo:** kept the garuda icon instead of text.

---

### April 27, 2026 (jana iteration)

**[REFACTOR]** Removed all caps and italic from _jana variant
- Navigation: removed `text-transform: uppercase`.
- Hero subtitle: removed `font-style: italic`.
- No other uppercase or italic occurrences remain.

**[REFACTOR]** Reduced top bar height
- Header padding: `20px 50px` → `12px 50px`.
- Garuda icon height: `55px` → `45px`.
- Icon remains anchored on the left side of the header.

**[FEAT]** Body text moved into hero
- Replaced intro paragraph with new text: *"V Penzionu a wellness U Třeboňské madony nabízíme nově také thajské masáže. Náš tým prošel v Thajsku školou tradičních masáží a nabízí celou škálu masáží, od reflexních a jemných relaxačních, přes nejvíce žádané thajské olejové, až po tradiční thajské masáže."*
- Paragraph placed inside the hero section, below the CTA button.
- Reduced hero padding and margins to keep the section compact:
  - Hero padding: `100px 20px` → `50px 20px 40px`
  - H1 margin-bottom: `10px` → `8px`
  - Subtitle margin-bottom: `30px` → `18px`
  - CTA margin-bottom: `18px`

**[REFACTOR]** Pricing page aligned with homepage design
- Removed table-based pricing boxes entirely.
- Replaced with card-based layout matching the homepage service cards:
  - White background, rounded corners (15px), shadow, centered text.
  - Each card contains massage title + two price rows.
  - Price rows use flex space-between with subtle bottom borders.
- Same hero style, header, and footer as the main page.

---

### April 27, 2026 (jana iteration)

**[REFACTOR]** All sans-serif text switched to heading font
- Google Fonts: removed Roboto Condensed; added Playfair Display 400 weight.
- Body font-family changed from `'Roboto Condensed', sans-serif` to `'Playfair Display', serif`.
- All body, nav, card, and footer text now renders in Playfair Display.

**[REFACTOR]** CTA button color
- Text color: `#81053D` (burgundy) → `#fff` (white).
- Background remains gold `#D4AF37`.
- Hover unchanged: burgundy bg with cream text.

---

### April 27, 2026 (jana iteration)

**[FEAT]** Created `_jana2` alternative with Merriweather font
- Duplicated `_jana` files into `index_jana2.html` and `cenik_jana2.html`.
- Replaced all `Playfair Display` occurrences with `Merriweather`.
- Updated Google Fonts import to `family=Merriweather:wght@400;700`.
- All other geometry, colors, and content identical to `_jana`.

**[REFACTOR]** Font weight increase across `_jana` and `_jana2`
- Headings (`h1, h2, h3`): `font-weight: 600` → `700`.
- CTA button: `font-weight: 600` → `700`.
- Applied to both `index_jana.html` / `cenik_jana.html` and their `_jana2` counterparts.

**[FIX]** Phone and email links
- Verified `tel:+420732468022` and `mailto:penzionutrebonskemadony@gmail.com` links exist in the footer of all four files (`_jana` and `_jana2`).

---

### April 27, 2026 (jana iteration)

**[REFACTOR]** CTA placement
- Moved CTA button below the hero body paragraph in both `index_jana.html` and `index_jana2.html`.
- Updated CSS: `.cta-button` `margin-bottom: 18px` → `margin-top: 18px`.

**[DOCS]** Created master design guidelines
- `design-guidelines.md` — comprehensive reference covering palette, typography, layout geometry, components, assets, site structure, version history, and change rules.
- Documents the pre-fork version (`index.html` / `cenik.html`), the current `_jana` fork, and the `_jana2` Merriweather variant.

---

### April 27, 2026 (content update)

**[FIX]** Replaced "klasické" with "tradiční" across all website versions
- `index.html`, `index_jana.html`, `index_jana2.html` — hero intro paragraph updated.
- `development log.md` — historical quote updated to match.

---

### April 27, 2026 (design update)

**[REFACTOR]** Reduced hero overlay opacity
- Overlay: `rgba(249, 244, 240, 0.82)` → `0.68` in all `_jana` and `_jana2` files.
- Background image is now ~15% more visible.
- Updated `design-guidelines.md` to match.

---

### April 27, 2026 (feature)

**[FEAT]** Added font switcher to `_jana` site
- Single `<select>` dropdown in the header of `index_jana.html` and `cenik_jana.html`.
- Switches between Playfair Display, Merriweather, and Georgia.
- Uses CSS custom property `--font-main` + JavaScript `localStorage` for cross-page persistence.
- Google Fonts link updated to load both Playfair Display and Merriweather (400 + 700 weights).
- `_jana2` unchanged as requested.
- Updated `design-guidelines.md` with temporary component section.

---

### April 27, 2026 (_jana2 experiment)

**[FEAT]** Header overlay experiment in `_jana2`
- Header repositioned from normal flow to `position: absolute` over the hero.
- Header background: semi-transparent burgundy `rgba(129, 5, 61, 0.75)` instead of solid cream.
- Image remains faintly visible through the tinted header.
- Hero gradient adjusted: `linear-gradient(to bottom, rgba(249, 244, 240, 0.3) 0%, rgba(249, 244, 240, 0.68) 30%)` so the top of the hero is more transparent, letting the background image show strongly under the burgundy header bar.
- Header text and nav links switched to cream `#F9F4F0`; hover to gold `#D4AF37`.
- Garuda icon inverted to white via `filter: invert(1)` for contrast on burgundy.
- Font switcher restyled with translucent white border/background for the dark header.
- Mobile: increased hero `padding-top` to `130px` to clear the stacked header.
- Applied to both `index_jana2.html` and `cenik_jana2.html`.

---

### April 27, 2026 (_jana2 iteration)

**[REFACTOR]** CTA shape
- `border-radius: 50px` (pill) → `8px` (soft rectangle) — better fits the structured card design.

**[REFACTOR]** Increased vertical whitespace
- Header padding: `12px` → `20px`.
- Hero padding: `80px 20px 40px` → `120px 20px 60px`.
- Hero internal margins increased: h1 `8px` → `16px`, subtitle `18px` → `28px`, CTA `18px` → `28px`, intro `24px` bottom margin.
- Mobile hero top padding: `130px` → `150px`.

**[FEAT]** Footer background image overlay
- Footer now uses the same background image as the hero, with a burgundy overlay (`rgba(129, 5, 61, 0.85)`).
- Footer padding increased: `40px` → `60px`.

**[REFACTOR]** Gold text throughout header and footer
- Header nav links: cream → gold `#D4AF37`; hover: gold → white `#fff`.
- Font switcher: restyled with gold border, background, and text.
- Footer: all text and links changed to gold `#D4AF37`.
- Garuda icon: `filter: invert(1)` → gold tint via `invert(1) sepia(1) saturate(8) brightness(0.85)`.

---

### April 27, 2026 (mobile-first rebuild)

**[REFACTOR]** Deleted old `_jana` desktop-first files
- Removed `index_jana.html` and `cenik_jana.html` (old desktop-first versions).

**[FEAT]** Rebuilt `_jana` from `_jana2` with mobile-first architecture
- New `index_jana.html` and `cenik_jana.html` created from `_jana2` visual design.
- **CSS flipped:** base styles = mobile, desktop enhancements in `@media (min-width: 769px)`.
- **Header:** CSS-only hamburger menu on mobile, horizontal nav on desktop.
- **Hero:** `padding: 80px 16px 40px` mobile → `120px 20px 60px` desktop. H1 `32px` → `48px`.
- **CTA:** Full-width (`width: 100%`) on mobile, auto-width inline-block on desktop. `min-height: 48px` for thumb targets.
- **Cards:** `width: 100%`, stacked on mobile → flex row (`250px`/`280px`) on desktop.
- **Touch targets:** all interactive elements get `min-height: 44px` / `min-width: 44px`.
- **Body font-size:** `17px` on mobile (serif readability) → `16px` on desktop.
- **Removed font switcher** from `_jana` (testing stays in `_jana2`).
- Visual design unchanged: burgundy header overlay, gold text, background image under header and footer, Merriweather, soft-rectangle CTA.

---

### May 18, 2026 (gallery fix)

**[FIX]** Rewrote `gallery.html` — multiple critical issues resolved
- Added missing Google Fonts link (`Merriweather:wght@400;700`).
- Fixed CSS syntax error: `transition: color: 0.3s;` → `transition: color 0.3s;`.
- Fixed invalid flexbox rule: `flex-wrap: repeat(auto-fill, minmax(350px, 1fr))` replaced with proper CSS Grid (`grid-template-columns: repeat(auto-fill, minmax(300px, 1fr))`).
- Added missing gallery CSS: `.gallery-section`, `.gallery-grid`, `.gallery-item`, `.gallery-item picture`, `.gallery-item img` with `aspect-ratio: 4/3` and `object-fit: cover`.
- Fixed nav links: `index.html`/`cenik.html` → `index_jana.html`/`cenik_jana.html`.
- Added `Galerie` link to nav on all three pages (`index_jana.html`, `cenik_jana.html`, `gallery.html`).
- Fixed footer: added missing `class="footer"`, styling now applies correctly.
- Fixed phone `tel:` links: `+420****8022` → `+420732468022` across all pages.
- Refactored JS image data: replaced verbose per-format strings with clean `id`-based srcset generation, added `sizes` attribute for responsive loading.

---

### May 18, 2026 (tasks 4 + 5)

**[FIX]** Task 5 — Hero subtitle visibility
- Changed `.hero .subtitle` color from gold `#D4AF37` to burgundy `#81053D` on `index_jana.html`.
- Gold on light gradient had poor contrast; burgundy matches H1 and maintains brand consistency.

**[FIX]** Task 4 — Decrease footer real estate
- Mobile padding: `48px 16px` → `32px 16px` (-33% vertical space).
- Desktop padding: `60px 20px` → `40px 20px` (-33% vertical space).
- Applied to all three active pages: `index_jana.html`, `cenik_jana.html`, `gallery.html`.

**[FIX]** Phone number correction (follow-up)
- Fixed `tel:+420****8022` → `tel:+420732468022` on `index_jana.html`, `cenik_jana.html`, `gallery.html`.
- Previous patch did not persist; now verified in all files.

**[DOCS]** Updated `design-guidelines.md`
|- Footer padding values updated to `32px 16px` / `40px 20px`.
|- Subtitle color documented as burgundy `#81053D`.

---

### May 19, 2026 (consolidated session)

**[FIX]** Task 4 — Naming consistency
|- Changed "Klasická thajská masáž" → "Tradiční thajská masáž" in `cenik_jana.html` to match `index_jana.html`.

**[FEAT]** Added 6th service card — "Reflexní masáž chodidel"
|- Added to `index_jana.html` and `cenik_jana.html` with placeholder body text.
|- Pricing: 590 Kč/30 m, 830 Kč/45 m (copied from "Masáž obličeje a hlavy").

**[FIX]** Task 5 — Normalized hero sub-heading color across all pages
|- `cenik_jana.html`: `.hero p` color `#4A4A4A` → `#81053D`.
|- `gallery.html`: `.hero .subtitle` color `#D4AF37` → `#81053D`.
|- All three active pages now use burgundy `#81053D` for hero sub-headings.

**[FEAT]** Task 3 + Task 8 — Compact card pricing typography
|- Added `Barlow Condensed:wght@600` to Google Fonts on `index_jana.html`.
|- Changed `.card-price` from Merriweather 700/16px to Barlow Condensed 600/14px with 0.3px letter-spacing.
|- Shortened time labels: `/NN min` → `/NN m` across all 6 cards.
|- Combined effect: ~25-30% more compact price lines, improved visual hierarchy (serif = content, sans = metadata).

**[FEAT]** Task 9 — Bottom-aligned pricing on index cards
|- Made `.card` a flex column (`display: flex; flex-direction: column;`).
|- Added `.card-body` class to description paragraphs with `flex-grow: 1`.
|- `.card-price` uses `margin-top: auto` to anchor to bottom.
|- On desktop: prices align horizontally across cards in the same row.

**[DOCS]** New task added to todo list
|- Task 10: In all body and heading text, replace space with non-breakable space after all single-character words (Czech typography rule).

**[PENDING]** Remaining open tasks
|- Task 2: Add payment/gift card text ("Platit pouze hotově" + "Prodáváme dárkové poukazy").
|- Task 5: Rephrase footer for GDPR compliance and vertical compaction.
|- Task 7 (optional): Remove hero heading from cenik and gallery pages.
|- Task 10: Non-breakable spaces after single-character words.

---
