---
section: surfaces-and-cards
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Surfaces & Cards

Every surface in Grouped is designed to elevate whatever sits on top of it. Three surface types create depth and warmth. Three card types handle content presentation across marketing and product contexts.


## Three Surface Types

### 1. Solid
The walls and floor. Structural surfaces for cards, containers, nav backgrounds. The foundation everything else sits on.

```css
.surface-solid {
  background: var(--L1);  /* --bg-raised */
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sm);  /* 8px */
}
```

**When to use:** Default for any container, card, panel, sidebar, or structural element. This is the starting point — use Solid unless you have a reason for Glass or Vinyl.

### 2. Glass
Frosted vinyl sleeve. Transparent, blurred, soft. Like looking through smoked glass. Content behind is present but softened.

```css
.surface-glass {
  background: var(--glass-bg);  /* rgba(17,22,32,0.75) dark / rgba(255,255,255,0.82) light */
  backdrop-filter: blur(24px) saturate(1.2);
  -webkit-backdrop-filter: blur(24px) saturate(1.2);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-sm);
}
```

**Variants:**
- **Glass (default)** — neutral frosted, for callouts and floating elements
- **Glass Light** — lighter opacity, for stacking on raised surfaces
- **Glass Warm** — bronze-tinted, for premium callouts and featured content

**When to use:** Overlays, popovers, floating panels, callout cards, anything that needs to feel "above" the solid surface while still showing depth behind it.

### 3. Vinyl
The premium surface. Warm sheen, subtle gradient with a bronze tint at the trailing edge. For hero moments and featured content.

```css
.surface-vinyl {
  background: linear-gradient(
    135deg,
    rgba(24, 30, 42, 0.7) 0%,
    rgba(31, 39, 53, 0.5) 40%,
    rgba(196, 138, 58, 0.04) 100%
  );
  backdrop-filter: blur(32px) saturate(1.3);
  border: 1px solid rgba(235, 225, 210, 0.08);
  border-radius: var(--radius-sm);
}
```

**When to use:** Hero sections, featured artist content, design principles, key stat callouts. Use sparingly — max 1–2 per page. If everything is premium, nothing is.

### 4. Stickers
Lightweight transparent labels. Like stickers on a record sleeve or tags on a crate of vinyl.

```css
.surface-sticker {
  padding: 5px 14px;
  border-radius: var(--radius-full);  /* pill */
  background: rgba(240,235,227,0.04);
  border: 1px solid var(--border-default);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.02em;
}

/* Accent sticker (uses focus blue, not bronze) */
.sticker-accent {
  background: rgba(124,187,223,0.08);
  border-color: rgba(124,187,223,0.15);
  color: var(--focus);
}
```

**When to use:** Tags, status indicators, metric callouts, filter chips.


## Three Card Types

### 1. Content Card (Product)
Border/outline only, no background fill. Clean, functional, information-first. Used throughout the product for lists, data displays, and navigable items.

**Key traits:**
- 1px border, no fill (transparent background)
- `--border-default` at rest, `--border-hover` on hover
- Subtle `translateY(-2px)` lift on hover
- Content is the hero — the card recedes

**When to use:** Fan directory items, campaign list rows, release cards, any product content that's one of many.

### 2. Showcase Card (Marketing)
Full surface treatment — Solid or Glass background, noise texture, cursor-following glow, 3D tilt on hover. The premium presentation.

**Key traits:**
- Solid or Glass surface background
- Noise grain texture layer
- Cursor-following warm glow (`::before` radial gradient)
- Edge light that follows cursor (`::after` mask trick)
- 3D perspective tilt on hover (max 4° rotation)
- Content lifts with `translateZ(10px)` on hover

**When to use:** Marketing landing pages, feature showcases, pitch deck components, any context where the card IS the selling point.

### 3. Turntable Card (Artist Content)
The artist-elevating card. Designed to make album art and artist content the brightest, warmest thing on screen.

**Key traits:**
- Album art takes the full top half (1:1 aspect ratio)
- Art scales to `1.02` on hover (like picking a record up)
- Warm vignette overlay on art (`radial-gradient` from center)
- Full tilt + glow + edge light treatment
- Sticker label below the art for status/metadata
- Content section below with title + description

**When to use:** Anywhere artist content is the primary focus — release pages, discovery grids, featured drops.


## Surface Rules

### Do
- Use Solid as the default — upgrade to Glass or Vinyl only when there's a reason
- Keep Glass surfaces over warm ambient backgrounds for the best frosted effect
- Use Vinyl for a maximum of 1–2 hero moments per page
- Use Stickers for lightweight metadata, not for primary actions
- Ensure artist content is always the brightest/warmest thing on a card

### Don't
- Don't use gradient fills on product surfaces (deprecated — use L0–L5 solid tokens)
- Don't mix light and dark surface tokens within the same container
- Don't use Glass without `backdrop-filter` — without the blur it's just a semi-transparent box
- Don't put Vinyl on Vinyl — surfaces shouldn't compete for attention
- Don't use Solid fill on product cards — border/outline only in product context


## Light Mode Behavior

Surfaces flip their tinting direction in light mode:
- **Solid:** White background, subtle borders (`rgba(26,26,26,0.15)`)
- **Glass:** Frosted white instead of frosted dark (`rgba(255,255,255,0.55)`)
- **Glass Warm:** Bronze tint uses darker bronze (`rgba(140,90,30,0.04)`)
- **Vinyl:** Inverted gradient (light to bronze-tinted)
- **Stickers:** Dark tint on light background


## Common Recipes

### "I'm building a product list item card"
```css
/* Content Card — border only, no fill */
background: transparent;
border: 1px solid var(--border-default);
border-radius: var(--radius-sm);  /* 8px */
padding: 20px;
transition: border-color 0.3s, transform 0.3s;
/* Hover: */
border-color: var(--border-hover);
transform: translateY(-2px);
```

### "I'm building a marketing feature showcase"
```css
/* Showcase Card — full surface treatment */
background:
  url("data:image/svg+xml,...") /* noise texture */,
  linear-gradient(180deg, rgba(235,225,210,0.02) 0%, transparent 25%),
  var(--L1);
border: 1px solid var(--border-default);
border-top-color: rgba(235,225,210,0.08);
border-radius: var(--radius-sm);
padding: 44px;
/* Add cursor glow + edge light via ::before and ::after */
```

### "I'm building an artist content display"
```css
/* Turntable Card */
.turntable-card {
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-default);
  overflow: hidden;
}
.turntable-card-art {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
}
/* Art scales on hover: transform: scale(1.02) */
/* Warm vignette on art: radial-gradient overlay */
```

### "I'm building a modal or popover"
```css
/* Glass surface */
background: var(--glass-bg);
backdrop-filter: blur(24px) saturate(1.2);
-webkit-backdrop-filter: blur(24px) saturate(1.2);
border: 1px solid var(--glass-border);
border-radius: var(--radius-md);  /* 16px */
box-shadow: var(--shadow-lg);
```

### "I'm building a callout/promo banner"
```css
/* Glass Warm */
background: rgba(196,138,58,0.04);
border: 1px solid rgba(196,138,58,0.1);
border-top-color: rgba(196,138,58,0.18);
backdrop-filter: blur(28px) saturate(1.3);
border-radius: var(--radius-sm);
```


## Never Do This

| Rule | Why |
|---|---|
| Never use fill/background on product cards | Product cards are border-only. Fill is reserved for marketing surfaces. |
| Never stack Vinyl on Vinyl | Surfaces shouldn't compete for attention. Max 1–2 Vinyl per page. |
| Never use Glass without `backdrop-filter` | Without blur it's just a semi-transparent box — defeats the purpose. |
| Never use gradient fills on product surfaces | Deprecated. Use solid L0–L5 tokens instead. |
| Never make the UI surface brighter than artist content | Artist content should always be the warmest, most vivid thing on screen. |
| Never use `border-radius: 10px` | Not in the scale. Use 8px (`--radius-sm`) or 16px (`--radius-md`). |


## Figma → Code Mapping

| Figma Component / Layer | CSS Class | Surface Type |
|---|---|---|
| Any card with `Fill/Core/L1` background | `.surface-solid` | Solid |
| Any card with blur + semi-transparent fill | `.surface-glass` | Glass |
| Any card with bronze gradient tint | `.surface-glass-warm` | Glass Warm |
| Any card with 135° bronze-edge gradient | `.surface-vinyl` | Vinyl |
| Pill-shaped labels with border | `.surface-sticker` | Sticker |
| Artist content frames with vignette | `.turntable-card` | Turntable |
| Product list items with outline only | Content Card pattern | Content Card |

**Radius mapping:**
| Figma | Token | Value |
|---|---|---|
| `radius/none` | `--radius-0` | 0px |
| `radius/sm` | `--radius-sm` | 8px |
| `radius/md` | `--radius-md` | 16px |
| `radius/lg` | `--radius-lg` | 24px |
| `radius/full` | `--radius-full` | 39px (pills) |


## Cross-Surface Translation

| Surface | How Surfaces Show Up |
|---|---|
| **Product (app)** | Content Cards (border-only) for lists/data. Glass for overlays/modals. Solid for containers. |
| **Marketing site** | Showcase Cards and Vinyl for hero moments. Glass for stats/callouts. Stickers for feature tags. |
| **Mobile** | Same surfaces, disable 3D tilt (no hover on touch). Glass blur may need performance fallback. |
| **Print** | Solid surfaces translate to bordered boxes. Glass effect simulated with tinted overlays. |
| **Events** | Navy backdrops (Solid), bronze-lit accent areas (Vinyl equivalent), frosted acrylic panels (Glass). |
| **Social** | Use solid dark backgrounds, bronze highlights. The grain texture can be applied as an image overlay. |
