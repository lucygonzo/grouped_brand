# Grouped Design System — Token Reference

> For use with Figma MCP and Claude Code workflows.
> Source of truth: [GDS26R Figma File](https://www.figma.com/design/wValDdxygSxILi49qBBgAW/GDS26R)

---

## Architecture

| Layer | Purpose |
|---|---|
| **Foundation** | Shared DNA — colors, typography, spacing, radius. Cohesive across marketing and product. |
| **Marketing** | Marketing-specific assets, textures, photography, brand moments. Not product-related. |
| **Product** | Product-level discussion, component scale, grid system, implementation patterns. |

---

## Color Tokens (Dark Theme — Default)

### Backgrounds

| Token | Value | Usage |
|---|---|---|
| `--bg-base` | `#111620` | Dark canvas base |
| `--bg-raised` | `#181E2A` | Raised surfaces, cards |
| `--bg-overlay` | `#1F2735` | Modal overlays, dropdowns |
| `--bg-subtle` | `#262F3F` | Subtle hover states |
| `--bg-muted` | `#2E3849` | Muted backgrounds |

### Borders

| Token | Value | Usage |
|---|---|---|
| `--border-default` | `rgba(235,225,210,0.07)` | Default card/divider borders |
| `--border-hover` | `rgba(235,225,210,0.11)` | Hover state borders |
| `--border-active` | `rgba(235,225,210,0.16)` | Active/focus borders |
| `--border-strong` | `rgba(235,225,210,0.22)` | High-contrast borders |

### Text

| Token | Value | Usage |
|---|---|---|
| `--text-primary` | `#F0EBE3` | Main text (warm cream) |
| `--text-secondary` | `#67686B` | Secondary text (solid mid-gray) |
| `--text-tertiary` | `#494B50` | Tertiary text (dim) |
| `--text-muted` | `#2E3238` | Decorative only, very dim |
| `--text-inverse` | `#111620` | Text on light backgrounds |

### Brand — Gold/Bronze Scale

| Token | Value |
|---|---|
| `--gold-50` | `#FEF7EC` |
| `--gold-100` | `#FDE9C8` |
| `--gold-200` | `#FAD08E` |
| `--gold-300` | `#F6B44E` |
| `--bronze-400` | `#C48A3A` **(primary brand accent)** |
| `--gold-500` | `#B87A2E` |
| `--gold-600` | `#916024` |
| `--gold-700` | `#6B471B` |
| `--gold-800` | `#4A3114` |

### Semantic Colors (Warm Vivid)

| Token | Value | Usage |
|---|---|---|
| `--success` | `#4ADE80` | Bright warm green — "live", confirmed |
| `--warning` | `#F0C543` | Bright yellow (~47deg hue, 12deg clear of bronze) |
| `--error` | `#F07068` | Warm coral-red |
| `--info` | `#63B3ED` | Warm sky blue |
| `--focus` | `#7CBBDF` | Ducky blue — interactive focus states |

### Feature Colors

| Token | Value | Usage |
|---|---|---|
| `--feature-community` | `#38C3FF` | Community features |
| `--feature-swaps` | `#5B61D9` | Swaps features |
| `--feature-broadcasts` | `#AD6AD9` | Broadcasts features |

### Data Visualization

| Token | Value |
|---|---|
| `--dataviz-blue` | `#1AB1EA` |
| `--dataviz-green` | `#6CE9A6` |
| `--dataviz-yellow` | `#FEC84B` |
| `--dataviz-orange` | `#FD853A` |

### Glass & Decoration

| Token | Value | Usage |
|---|---|---|
| `--glass-bg` | `rgba(17,22,32,0.75)` | Frosted glass background |
| `--glass-border` | `rgba(235,225,210,0.06)` | Glass border |
| `--deco-strong` | `rgba(240,235,227,0.18)` | Strong decorative overlay |
| `--deco-medium` | `rgba(240,235,227,0.12)` | Medium overlay |
| `--deco-subtle` | `rgba(240,235,227,0.08)` | Subtle overlay |
| `--deco-faint` | `rgba(240,235,227,0.06)` | Faint overlay |
| `--deco-ghost` | `rgba(240,235,227,0.04)` | Ghost overlay |
| `--deco-tint` | `rgba(240,235,227,0.1)` | Tint overlay |

### Shadows

| Token | Value | Usage |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.35)` | Subtle elevation |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.4)` | Cards, dropdowns |
| `--shadow-lg` | `0 8px 32px rgba(0,0,0,0.45)` | Modals, popovers |
| `--shadow-glow-gold` | `0 0 24px rgba(196,138,58,0.15)` | Warm brand glow |
| `--shadow-glow-soft` | `0 0 60px rgba(196,138,58,0.06)` | Subtle ambient glow |

---

## OLED Theme (True Black)

| Token | Dark Default | OLED Override |
|---|---|---|
| `--bg-base` | `#111620` | `#000000` |
| `--bg-raised` | `#181E2A` | `#0A0A0A` |
| `--bg-overlay` | `#1F2735` | `#111111` |
| `--bg-subtle` | `#262F3F` | `#1A1A1A` |
| `--bg-muted` | `#2E3849` | `#222222` |
| `--text-inverse` | `#111620` | `#000000` |
| Borders | `rgba(235,225,210,...)` | `rgba(255,255,255,...)` |

All color, brand, and semantic tokens remain the same.

---

## Typography

### Font Families

| Role | Family | Fallback |
|---|---|---|
| Display (32px+) | Anacrusis | Satoshi, sans-serif |
| Title | Satoshi | sans-serif |
| Body | Satoshi | sans-serif |
| Component | Satoshi | sans-serif |
| Monospace | JetBrains Mono | monospace |

**Key rule:** Anacrusis is reserved for display sizes (32px+) where the custom face is legible. Satoshi handles everything else. Satoshi has **no 600 Semibold** — available weights: 300, 400, 500, 700, 900. All Semibold intent maps to Bold 700.

### Figma Font Variables

| Variable | Value |
|---|---|
| `font/family/display` | Anacrusis |
| `font/family/title` | Satoshi |
| `font/family/body` | Satoshi |
| `font/family/component` | Satoshi |
| `font/weight/Regular` | 400 |
| `font/weight/Medium` | 500 |
| `font/weight/Bold` | 700 |

### Display Scale (D0-D6)

| Token | Size | Weight | Line-Height | Letter-Spacing | Font | Usage |
|---|---|---|---|---|---|---|
| D0 | 96px | 700 Bold | 116px | -4% | Anacrusis | Display Hero |
| D1 | 40px | 700 Bold | 48px | -3% | Anacrusis | Display XXL |
| D2 | 36px | 400 Regular | 48px | -1% | Satoshi | Display XL (data viz) |
| D3 | 28px | 400 Regular | 36px | -1% | Satoshi | Display L |
| D4 | 24px | 500 Medium | 32px | 0% | Satoshi | Display M |
| D5 | 18px | 500 Medium | 24px | -0.5% | Satoshi | Display S (subtitles) |
| D6 | 14px | 500 Medium | 20px | 0.5% | Satoshi | Display XS |

### Heading Scale (H1-H5)

| Token | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---|---|---|---|---|---|
| H1 | 36px | 700 Bold | 44px | -2% | Page titles |
| H2 | 28px | 700 Bold | 36px | -1% | Section titles |
| H3 | 24px | 700 Bold | 32px | 0% | Medium titles |
| H4 | 18px | 700 Bold | 28px | 0% | Small titles |
| H5 | 16px | 700 Bold | 24px | 0% | Smallest titles |

### Body Scale

| Token | Size | Weight | Line-Height | Letter-Spacing |
|---|---|---|---|---|
| Body Default | 14px | 400 Regular | 20px | 0% |
| Body Emphasized | 14px | 700 Bold | 20px | 0% |

### Caption Scale

| Token | Size | Weight | Line-Height | Letter-Spacing |
|---|---|---|---|---|
| Caption | 12px | 500 Medium | 20px | 1% |
| Caption Emphasized | 12px | 700 Bold | 20px | 0.5% |

### Component Scale (C1-C7) — Product Only

| Token | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---|---|---|---|---|---|
| C1 | 20px | 700 Bold | 24px | 0% | Large buttons |
| C2 | 18px | 700 Bold | 24px | 0% | Buttons |
| C3 | 16px | 700 Bold | 20px | 0% | Default buttons |
| C4 | 14px | 700 Bold | 16px | 0.5% | Navigation |
| C5 | 14px | 500 Medium | 16px | 0.5% | Navigation (light) |
| C6 | 11px | 500 Medium | 16px | 0.5% | Badges, small elements |
| C7 | 9px | 500 Medium | 12px | 1% | Smallest badges |

### Figma Font Size Variables

| Variable | Value |
|---|---|
| `font/size/6xl` | 96 (should be — currently 64, needs update) |
| `font/size/5xl` | 40 |
| `font/size/4xl` | 36 |
| `font/size/3xl` | 28 |
| `font/size/2xl` | 24 |
| `font/size/xl` | 20 |
| `font/size/lg` | 18 |
| `font/size/base` | 16 |
| `font/size/sm` | 14 |
| `font/size/xs` | 12 |
| `font/size/2xs` | 11 |

### Figma Line-Height Variables

| Variable | Value |
|---|---|
| `font/line-height/6xl` | 116 (should be — currently 72, needs update) |
| `font/line-height/4xl` | 48 |
| `font/line-height/2xl` | 36 |
| `font/line-height/xl` | 32 |
| `font/line-height/lg` | 24 |
| `font/line-height/md` | 20 |
| `font/line-height/sm` | 16 |
| `font/line-height/xs` | 14 |
| `font/line-height/xxs` | 12 |

### Figma Letter-Spacing Variables

| Variable | Value |
|---|---|
| `font/LetterSpacing/4xs` | -1 |
| `font/LetterSpacing/2xs` | -0.4 |
| `font/LetterSpacing/xs` | -0.1 |
| `font/LetterSpacing/sm` | -0.05 |
| `font/LetterSpacing/base` | 0 |
| `font/LetterSpacing/md` | 0.05 |
| `font/LetterSpacing/lg` | 0.1 |

---

## Spacing Scale

4px base unit. Every spatial value is a multiple of 4 (6px is the only exception).

| Token | Value |
|---|---|
| `--space-1` | 4px |
| `--space-2` | 8px |
| `--space-3` | 12px |
| `--space-4` | 16px |
| `--space-6` | 24px |
| `--space-8` | 32px |
| `--space-10` | 40px |
| `--space-12` | 48px |
| `--space-16` | 64px |
| `--space-20` | 80px |
| `--space-24` | 96px |
| `--space-32` | 128px |

### When to Use

| Value | Usage |
|---|---|
| 4px | Inline icon gaps, tight label pairs, chip padding |
| 8px | Related items within a group — badge + label, icon + text |
| 12px | Compact list items, small card internal padding |
| 16px | Standard card padding, form field gaps — the workhorse value |
| 24px | Section content gaps, card-to-card spacing in grids |
| 32-48px | Section breaks within a page, hero inner padding |
| 64-128px | Major section dividers, page-level vertical rhythm |

### Exceptions

- **6px:** Use for micro-spacing between an icon and its adjacent text label, or any context where 4px is too tight and 8px is too loose. Only non-multiple-of-4 value in the scale.
- **10px:** Avoid. Figma defaults to 10px in several auto-layout contexts — remap to 8px or 16px.

---

## Radius Scale

Five stops. No 10px radius.

| Token | Value | Usage |
|---|---|---|
| `--radius-0` | 0px | Sharp edges, dividers, flush containers |
| `--radius-sleeve` | 4px | Cards, containers, panels (vinyl sleeve edges) |
| `--radius-sm` | 8px | Small cards, list items, tight interactive elements |
| `--radius-md` | 16px | Standard cards, inputs, dropdowns, modals |
| `--radius-lg` | 24px | Large cards, hero containers |
| `--radius-full` | 39px | All pills: buttons, badges, tags |

**Note:** `--radius-label` (39px) is a legacy alias for `--radius-full`. No 10px radius — not enough visual difference from 8px to justify a separate token. Remap Figma's 10px defaults to `--radius-sm` (8px) or `--radius-md` (16px) depending on context.

---

## Motion

| Token | Value | Usage |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Quick entrance, emphasis |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetrical, polished |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Bouncy, playful |
| `--ease-smooth` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Calm, subtle |

---

## Iconography

**Library:** Phosphor Bold — https://phosphoricons.com/

### Stroke Properties

- Width: 2px
- Caps: Rounded
- Linejoin: Rounded

### Size Scale

| Size | Usage |
|---|---|
| 16px | Inline — alongside body text, table cells, captions |
| 20px | Default — navigation items, list icons, input prefixes |
| 24px | Buttons — button icons, toolbar actions, card headers |
| 32px | Feature — empty states, onboarding, feature highlights |

### Color Rules

- **Default:** Inherit text color from context (primary, secondary, tertiary)
- **Accent:** `var(--bronze-400)` for featured/premium icons (use sparingly)
- **Semantic:** Use `--success`, `--warning`, `--error`, `--info` for status icons

---

## Grid & Layout

### Container

| Property | Desktop | Mobile (<640px) |
|---|---|---|
| Max-width | 1280px | 100% |
| Side padding | `--space-6` (24px) | `--space-4` (16px) |
| Columns | 12 | 12 |
| Gutter | `--space-6` (24px) | `--space-4` (16px) |

### Responsive Breakpoints

| Name | Range |
|---|---|
| Mobile | < 640px |
| Tablet | 640px - 1024px |
| Desktop | 1024px+ |
| Wide | 1440px+ |

### Grid CSS

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6); /* 24px desktop */
}
@media (max-width: 639px) {
  .grid { gap: var(--space-4); /* 16px mobile */ }
}
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 var(--space-6);
}
@media (max-width: 639px) {
  .container { padding: 0 var(--space-4); }
}
```

---

## Figma Update Tasks (Pending)

These are the exact changes needed in the GDS26R Figma file:

1. **Typography Variables** — Fix `font/size/6xl`: 64 -> 96. Fix `font/line-height/6xl`: 72 -> 116.
2. **Line-Height Bindings** — Rebind D6 (sm->md), H4 (lg->xl), H5 (md->lg), Caption (sm->md), C6 (xs->sm).
3. **Letter-Spacing** — D0: set to -4% (currently -1%). D1: set to -3% (currently -0.05%).
4. **Font Weights** — Remap all Semibold -> Bold 700 (D0, D1, C1-C4). Set D4 to Medium 500.
5. **Naming** — Rename "Fine Print" -> "Caption", "Fine Print Emphasized" -> "Caption Emphasized".
6. **Global Cleanup** — Replace all Inter with Satoshi. Sweep #f8f8f8 -> #F0EBE3.
7. **Nav Menu Colors** — Remap legacy nav palette to global tokens: Nav-menu #f8f8f8 -> Text/Core/Primary #F0EBE3, Nav-menu-secondary #d2d3d6 -> Text/Core/Muted #A09B93, color/blue/400 #4f96d0 -> Brand/Focus Blue #7CBBDF, Menu Link Active #101323 -> Fill/Core/Base #111620, Fill/Interactive/Nav-menu #181e2a -> Fill/Core/L1 #181E2A.

---

## Intentional Product Override

| Override | Detail |
|---|---|
| Component Type Scale (C1-C7) + Satoshi body | Product-only scale for buttons, nav, and badges. Body defaults to 14px Satoshi. Anacrusis reserved for display 32px+. Not in the marketing type system. |

---

## Selection Color

```css
::selection {
  background: rgba(196,138,58,0.3);
  color: var(--text-primary);
}
```
