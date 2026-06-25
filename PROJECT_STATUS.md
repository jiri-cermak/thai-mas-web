# Thai Massage Website — Project Status

**Last updated:** 2026-06-25
**Active files:** `index.html`, `cenik.html`, `gallery.html`
**Directory:** `/home/jiric/data/thai massage web/` (WSL) / `/mnt/d/data/thai massage web/` (Windows)

---

## Completed Tasks

| # | Task | Notes |
|---|------|-------|
| 10 | Non-breakable spaces | 25 replacements across 3 files via `apply_nbsp.py` |
| 11 | Hero bg alignment | `center top` on hero + footer |
| 12 | Rotating hero background | 5-image carousel (156, 192, 209, 233, 175), 8s interval, crossfade + drift, sessionStorage persistence, gradient overlay z-index:1 |
| 13 | Background color | `#F5EBE1` → `#F9F4F0` (off-white) — all 3 pages |
| 14 | Card styling variant 2 | Burgundy top border (6px), cream price bar `#ffdfb7`, Merriweather 700/14px, shadow `0 5px 25px rgba(0,0,0,0.08)` |
| 15 | Restructure cenik page | Universal pricing banner (4 tiers: 30/45/60/90 min) + minimalist service list (6 items, gold dividers, no cards) |
| 17 | CSS extraction | Shared styles (header, nav, hero, footer, desktop) moved to `css/main.css`. Page-specific stays inline. ~55% reduction in total HTML lines. |
| 18 | File rename + cleanup | `index_jana.html` → `index.html`, `cenik_jana.html` → `cenik.html`. Dead files moved to `deprecated files/`. |
| 19 | Broken tel: links | `+420****8022` → `+420732468022` on all 3 pages. |
| 20 | Hero FPT optimization | Static fallback replaced with 4KB blurred version (`gallery/hero-blur.jpg`). Sharp image overlays via carousel within ~500ms. |
| 21 | Gallery JS extraction | Inline script moved to `js/gallery.js`, loaded with `defer`. |
| 22 | SEO meta tags | `description`, `og:*`, `twitter:*` placeholders and favicon added to all 3 pages. |

---

## Open Tasks

| # | Task | Status | Blocker/Note |
|---|------|--------|--------------|
| 2 | Payment/gift card text on cenik | **pending** | Text: "Prodáváme dárkové poukazy na hodnotu, trvání, nebo na konkrétní masáže. Volejte nám na <tel: link>". Placement TBD — ties to pricing grid context, may replace hero subtitle. No commit until decided. |
| 3 | Hero heading on cenik/gallery | **deferred** | Bound to nav redesign exploration — unified top bar (logo left, title center, menu right). Do not execute independently. |
| 16 | Index card footers → duration recommendations | **pending** | Prices removed from index cards (kept only in cenik). Duration text needed per card. |
| 23 | Select card layout | **done** | Final: layered design — border-top burgundy + cream background + white rounded rect body. 2026-06-25. |
| 24 | Re-run `apply_nbsp.py` | **pending** | File list updated; script ready to execute on new filenames. |
| 25 | Footer link tap effect (gold underline) | **pending review** | Implemented on `css/main.css`. Needs master user sign-off before production. |

---

## Proposed Features (Discussion)

### F1 — Multi-Language Versions (CZ, DE, EN, optional TH)

**Goal:** Serve the site in Czech (primary), German (tourist audience in Třeboň), English (international), optionally Thai (brand authenticity).

**Constraint:** Must align with the existing design philosophy — "Thai luxury, local warmth", pure static site (no build tools), burgundy + gold palette, mobile-first.

#### Implementation Option A: Subdirectory Structure ⭐ recommended

```
/                  → CZ (default, redirect from root or serve cz at /)
/cs/index.html
/de/index.html
/en/index.html
/th/index.html
```

Each language gets its own copy of all 3 pages. GitHub Pages serves subdirectory URLs natively.

**Pros:** ✅ SEO best practice (Google hreflang tags + `/de/` > `index-de.html`)  
✅ Works without JavaScript  
✅ Mirror of current codebase — no new dependencies  
✅ Can share `css/`, `js/`, `gallery/` via relative paths  

**Cons:** ❌ Content duplicated per language (manual sync or script needed)  
❌ Gallery images & CSS/JS shared — only text and HTML differ

#### Implementation Option B: Separate Files per Language

`index.html`, `index-de.html`, `index-en.html` — language code in filename.

**Pros:** ✅ Simplest possible — no subdirectories  
**Cons:** ❌ Ugly URLs (`/index-de.html`), weaker SEO

#### Implementation Option C: JS-Based i18n (JSON + runtime swap)

Single HTML per page + JSON translation files + JavaScript to replace text.

**Pros:** ✅ Single HTML file per page  
**Cons:** ❌ Breaks without JavaScript ❌ SEO penalty (JS-rendered text) ❌ Adds complexity — not aligned with current zero-framework approach

#### Recommended: Option A (subdirectories) + Python translation sync

```
thai-mas-web/
├── index.html              (CZ)
├── cenik.html
├── gallery.html
├── de/
│   ├── index.html
│   ├── cenik.html
│   └── gallery.html
├── en/  (same)
├── th/  (optional)
├── css/  ← shared
├── js/   ← shared
└── gallery/  ← shared
```

**Language switcher UI** — consistent with design guidelines:
- Small gold text links in the header nav area: `CS · DE · EN · TH`
- Current language highlighted (burgundy bg, gold text, 6px rounded pill)
- Subtle, no flags, no dropdown — just text, consistent with the minimalist approach
- Mobile: appears inside the hamburger menu alongside page links

**Content management:** A Python script (extending `scripts/`) to:
1. Parse source CZ HTML and extract translatable strings
2. Generate skeleton files for DE/EN/TH
3. Apply translations via JSON key-value pairs

**Priority:** Low — scope discussion deferred to pre-production sign-off (see R23).

#### Scope Discussion Required Before Sign-Off

This feature introduces significant content duplication. Key questions to resolve at the review walkthrough (R21):

| Question | Implication |
|----------|-------------|
| Who provides/sources the translations? | Professional translator vs machine + human review |
| Do all 3 pages get translated, or just key pages? | Minimal: index only. Full: all 3 |
| Is TH (Thai) in scope or stretch? | Adding a 4th language triples duplication |
| Language switcher: text links or flags or combined? | Text is design-aligned; flags are more intuitive for tourists |
| Content sync strategy? | Manual copy-paste vs Python generator script |

These decisions affect the rollout path and should be resolved before development starts.

#### Design Alignment Check

| Guideline | How F1 fits |
|-----------|-------------|
| "Thai luxury, local warmth" | CZ primary + DE/EN for tourists; optional TH as brand touch |
| "Restraint with gold" | Language switcher as small gold text, not flags or dropdowns |
| "Readability first" | Full translated pages — no machine-translation disclaimer needed |
| "Mobile-first" | Language links inside hamburger on mobile, visible in nav on desktop |
| "Consistency across pages" | Same layout, same assets — only text changes |
| No build tools | Subdirectories are static HTML — no build step required |

---

## Master User Pre-Production Review

Checklist of items requiring human review and sign-off before the site is considered production-ready. Last pass: **pending**.

### Visual & UI Review

| # | Item | Status | Notes |
|---|------|--------|-------|
| R1 | **Card layout** — all 6 cards render correctly on mobile & desktop | ⬜ | Cream footer aligned to bottom? White body rounded rect reads correctly? |
| R2 | **Footer links** — tap effect (gold underline sweep) | ⬜ | Test on real phone: no blue highlight, gold animates on tap, no layout shift |
| R3 | **Hero carousel** — crossfade, drift, sessionStorage persistence | ⬜ | Verify on fresh load vs returning visitor |
| R4 | **Hero background** — blurred fallback visible before carousel paints | ⬜ | Check on slow connection / 3G throttling |
| R5 | **Cenik page** — pricing tiers grid, service list layout | ⬜ | Mobile stacking, gold dividers visible |
| R6 | **Gallery page** — image grid, lazy loading, WebP fallbacks | ⬜ | All 15 images load? WebP → JPEG fallback works? |
| R7 | **Colours & contrast** — burgundy, gold, cream, white across all pages | ⬜ | Consistent? Gold legible on burgundy footer? White text on gold CTA? |
| R8 | **Typography** — Merriweather loading, fallback, line heights | ⬜ | No FOIT? Body text readable on mobile (17px)? |

### Content Review

| # | Item | Status | Notes |
|---|------|--------|-------|
| R9 | **All text is final** — descriptions, pricing, business info | ⬜ | Reflexní masáž text approved? Gift card text still pending (#2) |
| R10 | **Phone number** — correct format, functional on tap | ⬜ | `tel:+420732468022` dials the right number |
| R11 | **Email** — correct address, opens mail app | ⬜ | `penzionutrebonskemadony@gmail.com` |
| R12 | **SEO meta tags** — fill in real description, og:image, Twitter card | ⬜ | Currently placeholders (empty strings) |
| R13 | **Czech typography** — non-breaking spaces after single-letter words | ⬜ | `apply_nbsp.py` not yet re-run (#24) |

### Technical Review

| # | Item | Status | Notes |
|---|------|--------|-------|
| R14 | **Mobile responsiveness** — test at 375px, 768px, 1024px+ | ⬜ | Menu toggle, card rows, hero height, footer wrapping |
| R15 | **Touch targets** — all interactive elements ≥ 44×44px | ⬜ | Buttons, links, nav items, gallery |
| R16 | **Page speed** — Lighthouse mobile audit | ⬜ | FPT, LCP, CLS targets |
| R17 | **GitHub Pages** — deployment verified, auto-deploy working | ⬜ | Current URL: `https://jiri-cermak.github.io/thai-mas-web/` |
| R18 | **No broken links** — internal nav, gallery images, external | ⬜ | `index.html`, `cenik.html`, `gallery.html` cross-references |
| R19 | **Assets** — all images load (garuda.png, bg_jana.jpg, hero-blur, gallery) | ⬜ | Missing logo, background paths verified |
| R20 | **No Jekyll processing** — `.nojekyll` file present in repo | ⬜ | Prevents GH Pages from treating files as Jekyll |

### Deployment Sign-Off

| # | Item | Status | Notes |
|---|------|--------|-------|
| R21 | **Master user walkthrough** — end-to-end on real phone | ⬜ | Tap through all pages, all interactions |
| R22 | **Final approval** | ⬜ | Go / No-go for production |
| R23 | **Custom domain** (future) | ⬜ | DNS not set up yet — deferred

---

## Design System

| Element | Value |
|---------|-------|
| Font | Merriweather 400/700 (Google Fonts) |
| Body bg | `#F9F4F0` |
| Primary | `#81053D` (burgundy) |
| Accent | `#D4AF37` (gold) |
| Cream | `#ffdfb7` |
| Text | `#2D2D2D` / `#4A4A4A` |
| Card radius | 15px |
| Hero gradient | `linear-gradient(to bottom, rgba(249, 244, 240, 0.3) 0%, rgba(249, 244, 240, 0.68) 30%)` |

---

## Files

| File | Role |
|------|------|
| `index.html` | Homepage — 6 service cards with carousel hero |
| `cenik.html` | Pricing — universal banner + service list |
| `gallery.html` | Gallery — image grid |
| `css/main.css` | Shared styles (header, nav, hero, footer, desktop) |
| `js/hero-carousel.js` | Carousel engine (sessionStorage, crossfade, drift) |
| `js/gallery.js` | Gallery image grid builder |
| `scripts/apply_nbsp.py` | Czech typography script (idempotent, placeholder-safe) |
| `PROJECT_STATUS.md` | This file |

---

## Backups

- `project-snapshot-20260531/` — pre-refactor copies of all 3 active files
- Pre-nbsp backups moved to `deprecated files/`
- Original source photos in `fotosource/`

---

## Session Notes

- User prefers iterative, visual-first approach — test one change before applying globally
- Values consistency across pages
- FPT minimalization principle active — base image loads from CSS, no JS dependency for first paint
- Review agent workflow: structured JSON output, iterative bug-fixing
- Czech typography: `&nbsp;` after all single-character words (a, i, o, u, s, k, v, z)
