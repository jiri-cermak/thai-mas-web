# Design Guidelines — Thajské masáže Třeboň

## Philosophy
- Mobile-first CSS: base styles are for mobile. Desktop enhancements live inside `@media (min-width: 769px)`.
- Touch targets: minimum `44px` height and width for all interactive elements.
- Two design branches:
  - `_jana` — production-ready mobile-first rebuild (this document).
  - `_jana2` — AB-test variant, frozen. Same visuals + font-switcher experiment.

## Color Palette
| Role | Hex | Usage |
|------|-----|-------|
| Cream | `#ffdfb7` | Page background (V2: darker warm cream) |
| Burgundy | `#81053D` | H1–H3 text, header/footer overlays, hover states |
| Gold | `#D4AF37` | Header/footer text, accents |
| Body | `#2D2D2D` | Body text on light backgrounds |
| Secondary | `#4A4A4A` | Subtitles, secondary text |

## Typography
| Role | Font | Weights |
|------|------|---------|
| Headings | Merriweather, serif | 700 |
| Body | Merriweather, serif | 400 |
| Fallbacks | Georgia, serif | — |

- `font-size: 17px` on mobile (better serif readability), `16px` on desktop `@media (min-width: 769px)`.
- H1: `32px` mobile, `48px` desktop.
- H3: `20px` mobile, `20px` desktop.
- Subtitle: `18px` mobile, `18px` desktop. Color: burgundy `#81053D`.
- Navigation links: `15px`.

## Buttons (CTA)
| State | Background | Text | Border Radius |
|-------|-----------|------|---------------|
| Default | Gold `#D4AF37` | White `#FFFFFF` | `8px` |
| Hover | Burgundy `#81053D` | Cream `#F9F4F0` | `8px` |

- Mobile: full-width (`width: 100%`), `min-height: 48px`.
- Desktop: `inline-block`, auto width, `padding: 12px 40px`.

## Spacing
| Context | Mobile | Desktop |
|---------|--------|---------|
| Header padding | `12px 16px` | `20px 50px` |
| Hero padding | `80px 16px 40px` | `120px 20px 60px` |
| Section padding | `40px 16px` | `50px 20px` |
| Card padding | `24px` | `30px` |
| Footer padding | `32px 16px` | `40px 20px` |

## Header
- `position: absolute` over the hero.
- Background: `rgba(129, 5, 61, 0.85)` (burgundy overlay, V2: more saturated).
- Logo: garuda, gold-tinted via `filter: invert(1) sepia(1) saturate(8) brightness(0.85)`.
- Mobile: CSS-only hamburger (`<input type="checkbox">` + `<label>`). Three gold bars.
- Desktop: horizontal nav, links in gold, `margin-left: 20px`.

## Hero
- Background image (`bg_jana.jpg`) with gradient overlay:
  `linear-gradient(to bottom, rgba(249, 244, 240, 0.3) 0%, rgba(249, 244, 240, 0.68) 30%)`
- H1 + subtitle + body text + CTA button, stacked vertically, centered.

## Cards / Pricing
- Background: white.
- Border: `1px solid #eee`, `border-radius: 15px`.
- Box shadow: `0 5px 15px rgba(0,0,0,0.05)`.
- Mobile: `width: 100%`, stacked vertically, `margin-bottom: 16px`.
- Desktop: `width: 280px` (pricing) or `250px` (services), flex row with `gap: 30px`.

## Footer
- Background image (`bg_jana.jpg`) with burgundy overlay (`rgba(129, 5, 61, 0.85)`).
- Text color: gold `#D4AF37`.
- Contact links: `tel:` and `mailto:`.

## Assets
| File | Description |
|------|-------------|
| `garuda.png` | Gold-tinted Garuda logo |
| `bg_jana.jpg` | Unsplash spa/lotus background |

## Responsive Breakpoint
- `@media (min-width: 769px)` — desktop enhancements.

## Accessibility
- All interactive elements have `min-height: 44px`.
- hamburger has `aria-label="Menu"`.
- Color contrast verified for gold on burgundy (WCAG AA for large text).
