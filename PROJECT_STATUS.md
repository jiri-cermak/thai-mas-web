# Thai Massage Website — Project Status

**Last updated:** 2026-05-31
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
