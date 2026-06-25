# Refactor Plan — Thai Massage Website

**Created:** 2026-05-31
**Status:** In progress
**Scope:** 3 static HTML pages (`index_jana.html`, `cenik_jana.html`, `gallery.html`)

---

## 1. Rationale

### 1.1 CSS Duplication
All 3 pages carry ~185 identical lines of CSS (header, nav, hero, footer, desktop breakpoints). Changing one element requires editing 3 files. Extracting shared styles into `css/main.css` makes the codebase maintainable and reduces total CSS volume.

### 1.2 File Naming
`index_jana.html` and `cenik_jana.html` carry the `_jana` suffix from an experimental fork. They are now the canonical production files and should be renamed to `index.html` and `cenik.html`.

### 1.3 Inconsistent Background Color
Task 13 specified `#F9F4F0` for all pages, but `index_jana.html` and `gallery.html` still use `#F5EBE1` (old sand color). Only `cenik_jana.html` has the correct value.

### 1.4 Broken Phone Link
The `href="tel:+420****8022"` asterisks render the link non-functional on mobile devices. Intentional masking for repo privacy is moot — the visible text displays the full number anyway. The `href` should match.

### 1.5 First Paint Time (FPT) — Hero Background
The static CSS hero fallback is `gallery/medium/209_medium.jpg` (72KB, 800x533).
On a 375px mobile viewport this is 2.1x over-resolved. Strategy: replace with a
blurred ultra-low-res variant (~2KB, 80px wide) generated from `fotosource/209.jpg`.
The blurred image reads as intentional spa atmosphere, then `hero-carousel.js`
overlays a sharp version within ~500ms. Net FPT saving: ~350ms on 3G mobile.

```
Stack:
  ══════════════════════════════
  h1 / subtitle / CTA         z-index: 2
  .hero-gradient              z-index: 1
  .hero-bg-layer (carousel)   z-index: 0  (opacity 0→1, covers below)
  .hero CSS background        blurred 2KB, visible until carousel paints
  ══════════════════════════════
```

### 1.6 Orphaned Files
The root directory contains deprecated mockups, backup files, test pages, preview files,
and unused JS. These create ambiguity about which files are canonical.

---

## 2. Proposed Changes

### Phase 0: Snapshot (Rollback Safety)
Copy all 3 active HTML files to `project-snapshot-20260531/` before any changes.

### 2.1 Rename Canonical Files (Task A)
| Before | After |
|--------|-------|
| `index_jana.html` | `index.html` |
| `cenik_jana.html` | `cenik.html` |

Update all `<a href="">` references in header/nav across all 3 pages.
Update `scripts/apply_nbsp.py` FILES list.

### 2.2 Extract Shared CSS (Task B)
Create `css/main.css` containing styles shared by 2+ pages:

**Shared (all 3 pages):**
- `*` box-sizing reset
- `body` base (font, color, line-height)
- `h1, h2, h3` defaults
- Header (position, padding, flex, border, background)
- `.logo-img` (height, filter)
- `#menu-toggle`, `.menu-icon`, `.menu-icon span`
- `nav` (position, max-height, overflow, transition)
- `nav a` (display, color, padding, hover)
- Hero base (position, padding, background, overflow)
- `.hero-bg-layer` (position, background-size, opacity, transition)
- `.hero-gradient` (gradient overlay)
- `.hero h1, .hero p, .hero a` (z-index)
- `.hero h1` (font-size, color, margins)
- Footer base (background, color, padding, text-align)
- `.footer p`, `.footer a`, `.footer .hours`
- Desktop breakpoint `@media (min-width: 769px)` — header, nav, hero, footer

**Page-specific (stays inline):**
- `index.html`: card styles (v1–v6), CTA button, `.hero-intro`, `.hero .subtitle`
- `cenik.html`: pricing banner, pricing tiers grid, services list
- `gallery.html`: gallery grid, gallery items, `.hero .subtitle`

Each page gets `<link rel="stylesheet" href="css/main.css">` in `<head>`.
Inline `<style>` blocks remain for page-specific rules only.

**Footer normalization:** `cenik.html` is missing `.footer h2` rule and uses
`font-weight: 700` on `.hours` instead of `600`. Both are unified to match
`index.html`/`gallery.html`.

### 2.3 Fix Bugs + Generate Blur (Task C)
| Bug | Fix |
|-----|-----|
| Body bg `#F5EBE1` on index + gallery | Change to `#F9F4F0` |
| `tel:+420****8022` on all 3 pages | Change to `tel:+420732468022` |

**Blur generation:**
```
Source:  fotosource/209.jpg (6000x4000)
Command: convert fotosource/209.jpg -resize 80x53 -gaussian-blur 6
         -quality 40 gallery/hero-blur.jpg
Output:  gallery/hero-blur.jpg (~2KB)
```

Change `.hero` CSS `background` from `url('gallery/medium/209_medium.jpg')`
to `url('gallery/hero-blur.jpg')` in `css/main.css`.

### 2.4 Extract Gallery JS (Task D)
Move inline gallery `<script>` from `gallery.html` (lines 341-384) to `js/gallery.js`.
Replace with `<script src="js/gallery.js" defer></script>`.

### 2.5 Housekeeping (Task E)
Move to `deprecated files/`:
```
Root → deprecated files/:
  index_jana2.html
  cenik_jana2.html
  old index.html        (the pre-_jana version)
  old cenik.html        (the pre-_jana version)
  test-gallery.html
  test-js.html
  gallery-test.html
  preview-bg-offwhite.html
  preview-bg-sand.html
  preview-cards.html
  footer_preview.txt
  *.backup_*.html       (all backup files)
  images.js
  server.log

gallery/webp/ → deprecated files/gallery webp backup/
gallery/jpeg/ → delete (empty directory)
```

### 2.6 SEO + Social Meta Tags (Task F)
Add to all 3 pages' `<head>`:
```html
<!-- TODO: Fill in actual values before deployment -->
<meta name="description" content="">
<link rel="icon" href="garuda.png" type="image/png">

<!-- Open Graph -->
<meta property="og:title" content="Thajske masaze Trebon">
<meta property="og:description" content="">
<meta property="og:image" content="">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
```

### 2.7 Update Documentation (post-task)
Update `PROJECT_STATUS.md` with new filenames and completed tasks.
Update `apply_nbsp.py` FILES list to `["index.html", "cenik.html", "gallery.html"]`.

---

## 3. Execution Order

```
Phase 0: Snapshot (copy all 3 active files to project-snapshot-20260531/)
Phase 1: A (rename)                       [sequential]
Phase 2: B (CSS), C (bugs+blur), E (housekeeping), D (gallery JS)  [parallel, 4 agents]
Phase 3: F (SEO)                          [after B verified]
Phase 4: apply_nbsp.py re-run             [after all edits]
```

```
Dependency graph:

0 ── A ──┬── B ── F ── apply_nbsp
          ├── C
          ├── D (independent)
          └── E
```

- **Phase 0 must run first** (rollback safety for the reviewer)
- **A must run before B, C, E** because they touch renamed files
- **D is independent** (only touches gallery.html, which is not renamed)
- **F should run after B** is stable (touches all 3 pages)

---

## 4. Target Structure (post-execution)

```
thai massage web/
├── index.html
├── cenik.html
├── gallery.html
├── css/
│   └── main.css
├── js/
│   ├── hero-carousel.js
│   └── gallery.js
├── garuda.png
├── bg_jana.jpg
├── bg_jana_original.jpg
├── bg.jpg
├── gallery/
│   ├── hero-blur.jpg          ← new (2KB)
│   ├── large/
│   ├── medium/
│   └── thumbs/
├── fotosource/
├── scripts/
│   └── apply_nbsp.py
├── project-snapshot-20260531/   ← rollback point
│   ├── index_jana.html
│   ├── cenik_jana.html
│   └── gallery.html
├── docs/                      ← renamed from root .md files
│   ├── PROJECT_STATUS.md
│   ├── design-guidelines.md
│   ├── development-log.md
│   ├── agent.md
│   └── mobile-first.md
├── deprecated files/          ← historical reference only
│   ├── gemini mockups/
│   ├── gallery webp backup/
│   ├── index_jana2.html
│   ├── cenik_jana2.html
│   ├── pre-_jana index.html
│   ├── pre-_jana cenik.html
│   ├── test files/
│   ├── preview files/
│   ├── backups/
│   ├── images.js
│   └── server.log
├── REFACTOR_PLAN.md
├── .gitignore
└── README.md
```

---

## 5. Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| CSS extraction breaks visuals | Medium | Exact copy-paste of selectors + values; page-specific stays inline; compare pages after |
| Broken nav links after rename | Medium | Global grep for `index_jana` and `cenik_jana` in all HTML/MD/PY files |
| Blur looks too soft on retina | Low | 80px at quality 40 with gauss blur 6 tested; fades to sharp in <1s |
| `apply_nbsp.py` targets wrong files | Low | FILES list updated atomically with rename |
| Deprecated folder bloat | Low | All moves are within repo; nothing deleted |
| Catastrophic regression | Medium | Phase 0 snapshot preserves pre-change copies |

---

## 6. Questions Resolved

| # | Question | Answer |
|---|----------|--------|
| 1 | Background color | `#F9F4F0` for all 3 pages |
| 2 | Phone tel: link | Fix `href` to `+420732468022`; visible text unchanged |
| 3 | Missing image variants | All variants exist on disk (no generation needed beyond hero-blur.jpg) |
| 4 | CSS extraction scope | Extract shared 2+ pages into `css/main.css`; page-specific stays inline |
| 5 | Dead files | Move to `deprecated files/`, do not delete |
| 6 | Canonical filenames | Rename `_jana` → drop suffix |
| 7 | Pricing grid layout | Keep current; visual validation deferred |
| 8 | Unused gallery dirs | `gallery/jpeg/` (empty) → delete; `gallery/webp/` → move to deprecated |
| 9 | SEO | Add generic tags; mark for data fill-in |
| 10 | Contact page | Not needed; 3-page layout is intentional |
