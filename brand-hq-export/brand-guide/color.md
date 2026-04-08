---
section: color
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Color

Three temperature layers. Deep blue surfaces create the room. Warm bronze marks the brand. Cool focus blue handles everything interactive. The temperature contrast between cool navy and warm gold is what gives Grouped its depth.

## The Four Core Colors

| Color | Role | Dark Mode Hex | Light Mode Hex |
|---|---|---|---|
| **Bronze** | Primary brand accent — logos, headlines, CTAs, brand moments | `#C48A3A` | `#956A1D` |
| **Navy** | Foundation — backgrounds, surfaces, print base | `#111620` | `#FAFAF8` (inverts to cream) |
| **Cream** | Warm neutral — body text (dark), backgrounds (light) | `#F0EBE3` | `#111620` (inverts to navy) |
| **Focus Blue** | Interactive accent — focus rings, active states, badges | `#7CBBDF` | `#2874A6` |


## Color Roles (The Rule)

**If the element is part of the brand voice** (something you'd see on a poster), use **bronze**.
**If the element is part of the interface** (something you'd interact with or that tells you a current state), use **focus blue**.

| Bronze (`--bronze-400`) | Focus Blue (`--focus`) |
|---|---|
| Headlines and display type | Input focus rings and borders |
| Logo and wordmark | Accent stickers (metrics, status) |
| Section overline labels | Active/selected state highlights |
| Primary CTA buttons (fill) | Data visualization primary color |
| Concentric arc motif | Interactive hover accents |
| The logo dot in "grouped." | Accent badges |


## Bronze Accent Scale

| Token | Hex | Usage |
|---|---|---|
| `--gold-50` | `#FEF7EC` | Lightest tint |
| `--gold-100` | `#FDE9C8` | Light tint |
| `--gold-200` | `#FAD08E` | Medium tint |
| `--gold-300` | `#F6B44E` | Warm highlight |
| **`--bronze-400`** | **`#C48A3A`** | **Primary brand accent** |
| `--gold-500` | `#B87A2E` | Darker accent |
| `--gold-600` | `#916024` | Deep accent |
| `--gold-700` | `#6B471B` | Darkest accent |
| `--gold-800` | `#4A3114` | Near-black warm |

Bronze 400 is reserved for headlines, logos, section labels, CTAs, and the concentric arc motif. It should never appear on interactive feedback elements like focus rings, stickers, or status badges.

### Bronze Dark Mode Rule
**Bronze must always sit on navy blues (#111620 family).** When browser-forced dark mode or system dark mode is applied, bronze can render as a muddy desaturated brown-green. This is unacceptable. All dark surfaces must use our explicit navy tokens (L0–L5), never browser-default dark backgrounds. If an element shows bronze on a non-navy dark surface, it's a bug.


## Surface Layers

### Dark Mode (Default)

| Layer | Hex | Token | Legacy Alias |
|---|---|---|---|
| L0 | `#111620` | `--L0` | `--bg-base`, `--layer-1` |
| L1 | `#181E2A` | `--L1` | `--bg-raised`, `--layer-2` |
| L2 | `#1F2735` | `--L2` | `--bg-overlay`, `--layer-3` |
| L3 | `#262F3F` | `--L3` | `--bg-subtle`, `--layer-4` |
| L4 | `#2E3849` | `--L4` | `--bg-muted`, `--layer-5` |
| L5 | `#364252` | `--L5` | `--layer-6` |

Each layer gains ~3–3.5 lightness points with a consistent blue undertone. **Use `--L0` through `--L5` in new work.** The `--bg-*` and `--layer-*` aliases are deprecated.

### Light Mode

| Layer | Hex | Token |
|---|---|---|
| L0 | `#FAFAF8` | `--L0` |
| L1 | `#FFFFFF` | `--L1` |
| L2 | `#FFFFFF` | `--L2` |
| L3 | `#F3F3F0` | `--L3` |
| L4 | `#EAEAE6` | `--L4` |
| L5 | `#E0E0DC` | `--L5` |

### OLED Mode

| Layer | Hex | Token |
|---|---|---|
| L0 | `#000000` | `--L0` |
| L1 | `#0A0A0A` | `--L1` |
| L2 | `#111111` | `--L2` |
| L3 | `#1A1A1A` | `--L3` |
| L4 | `#222222` | `--L4` |
| L5 | `#2A2A2A` | `--L5` |

OLED is a functional variant for mobile battery savings. True black with neutral white strokes instead of warm cream. The navy theme is always the primary dark experience.

### Design Principle: Navy, Not Black
Every dark surface carries a cool blue undertone. Never use neutral greys (`#1A1A1A`, `#222`) in the dark theme — they read as dead spots that break the temperature relationship. It's the same reason jewelers display gold on dark blue velvet, not black fabric.


## Text Hierarchy

### Dark Mode

| Level | Hex | Token | Legacy Alias | Usage |
|---|---|---|---|---|
| T1 | `#F0EBE3` | `--T1` | `--text-primary` | Body copy, headings |
| T2 | `#67686B` | `--T2` | `--text-secondary` | Supporting text |
| T3 | `#494B50` | `--T3` | `--text-tertiary` | Captions, metadata |
| T4 | `#2E3238` | `--T4` | `--text-muted` | Decorative, very dim |
| T5 | `#111620` | `--T5` | `--text-inverse` | Text on light/accent fills |

### Light Mode

| Level | Hex | Token | Usage |
|---|---|---|---|
| T1 | `#111620` | `--T1` | Body copy, headings |
| T2 | `#535862` | `--T2` | Supporting text |
| T3 | `#7C7E85` | `--T3` | Captions, metadata |
| T4 | `#ABABAF` | `--T4` | Decorative, very dim |
| T5 | `#FFFFFF` | `--T5` | Text on dark/accent fills |

**Use `--T1` through `--T5` in new work.** The `--text-*` aliases are deprecated.


## Semantic Colors

| Name | Dark Hex | Light Hex | Token | Usage |
|---|---|---|---|---|
| Success | `#4ADE80` | `#1A9A4A` | `--success` | Positive states, live campaigns |
| Warning | `#F0C543` | `#B8941F` | `--warning` | Drafts, caution states |
| Error | `#F07068` | `#C93E36` | `--error` | Paused, error states |
| Info | `#63B3ED` | `#2A7AB5` | `--info` | Scheduled, informational |

Warning yellow (`#F0C543`, ~47° hue) is 12° clear of bronze (`#C48A3A`, ~35° hue) to prevent confusion.

### Error Scale (interactive)
| State | Hex | Token |
|---|---|---|
| Default | `#F07068` | `--error` |
| Hover | `#D85A52` | `--error-hover` |
| Active | `#C04840` | `--error-active` |


## Focus Blue

| Hex | Token | Role |
|---|---|---|
| `#7CBBDF` (dark) | `--focus` | Interactive accent |
| `#2874A6` (light) | `--focus` | Interactive accent |

Used for input focus rings, accent stickers, active state indicators, highlighted data points, and badges. Pops against deep blue without reading as a warning the way bronze does at small sizes.


## Feature Colors

| Feature | Hex | Token |
|---|---|---|
| Community | `#38C3FF` | `--feature-community` |
| Swaps | `#5B61D9` | `--feature-swaps` |
| Broadcasts | `#AD6AD9` | `--feature-broadcasts` |


## Data Visualization

| Name | Hex | Token |
|---|---|---|
| Blue | `#1AB1EA` | `--dataviz-blue` |
| Green | `#6CE9A6` | `--dataviz-green` |
| Yellow | `#FEC84B` | `--dataviz-yellow` |
| Orange | `#FD853A` | `--dataviz-orange` |


## Borders

### Dark Mode
| State | Value | Token |
|---|---|---|
| Default | `rgba(235,225,210,0.07)` | `--border-default` |
| Hover | `rgba(235,225,210,0.11)` | `--border-hover` |
| Active | `rgba(235,225,210,0.16)` | `--border-active` |
| Strong | `rgba(235,225,210,0.22)` | `--border-strong` |
| Input | `rgba(235,225,210,0.14)` | `--border-input` |

### Light Mode
| State | Value | Token |
|---|---|---|
| Default | `rgba(26,26,26,0.15)` | `--border-default` |
| Hover | `rgba(26,26,26,0.22)` | `--border-hover` |
| Active | `rgba(26,26,26,0.28)` | `--border-active` |
| Strong | `rgba(26,26,26,0.35)` | `--border-strong` |
| Input | `rgba(26,26,26,0.25)` | `--border-input` |


## Shadows

| Token | Dark Mode | Light Mode |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.35)` | `0 1px 2px rgba(0,0,0,0.06)` |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.4)` | `0 4px 12px rgba(0,0,0,0.08)` |
| `--shadow-lg` | `0 8px 32px rgba(0,0,0,0.45)` | `0 8px 32px rgba(0,0,0,0.1)` |
| `--shadow-glow-gold` | `0 0 24px rgba(196,138,58,0.15)` | `0 0 24px rgba(149,106,29,0.12)` |
| `--shadow-glow-soft` | `0 0 60px rgba(196,138,58,0.06)` | `0 0 60px rgba(149,106,29,0.06)` |


## Decorative Opacity Scale

| Token | Dark Mode | Light Mode |
|---|---|---|
| `--deco-strong` | `rgba(240,235,227,0.18)` | `rgba(26,26,26,0.2)` |
| `--deco-medium` | `rgba(240,235,227,0.12)` | `rgba(26,26,26,0.14)` |
| `--deco-subtle` | `rgba(240,235,227,0.08)` | `rgba(26,26,26,0.1)` |
| `--deco-faint` | `rgba(240,235,227,0.06)` | `rgba(26,26,26,0.07)` |
| `--deco-ghost` | `rgba(240,235,227,0.04)` | `rgba(26,26,26,0.05)` |


## Glass Tokens

| Token | Dark Mode | Light Mode |
|---|---|---|
| `--glass-bg` | `rgba(17,22,32,0.75)` | `rgba(255,255,255,0.82)` |
| `--glass-border` | `rgba(235,225,210,0.06)` | `rgba(0,0,0,0.1)` |


## Print / Physical

### Dark Mode Primary Palette
| Color | HEX | RGB | CMYK | Pantone |
|---|---|---|---|---|
| Bronze | `#C48A3A` | 196, 138, 58 | 0/30/70/23 | PMS 1245 C/U |
| Navy | `#111620` | 17, 22, 32 | 47/31/0/87 | PMS 533 C/U |
| Cream | `#F0EBE3` | 240, 235, 227 | 0/2/6/6 | PMS 7527 C/U |
| Focus Blue | `#7CBBDF` | 124, 187, 223 | 44/16/0/13 | PMS 2905 C/U |

### Light Mode Palette
| Color | HEX | RGB | CMYK | Pantone |
|---|---|---|---|---|
| Bronze (light) | `#956A1D` | 149, 106, 29 | 0/29/81/42 | PMS 1255 C/U |
| Navy (light body) | `#111620` | 17, 22, 32 | 47/31/0/87 | PMS 533 C/U |
| Cream (light bg) | `#FAF7F2` | 250, 247, 242 | 0/1/3/2 | PMS 7527 C/U |
| Focus Blue (light) | `#2874A6` | 40, 116, 166 | 76/30/0/35 | PMS 7691 C/U |

### Print Rules
- For premium print (business cards, packaging, foil): specify Bronze as **PMS 1245 spot** (dark) or **PMS 1255 spot** (light) rather than CMYK process
- Proof Bronze on press — CMYK process can shift warm tones toward orange
- Black utility: `#000000` / CMYK 0/0/0/100 / Pantone Black C
- White utility: `#FFFFFF` / CMYK 0/0/0/0


## Common Recipes

### "I'm building a product card"
```css
background: transparent;
border: 1px solid var(--border-default);
border-radius: var(--radius-sm);
color: var(--T1);
/* Hover: */
border-color: var(--border-hover);
transform: translateY(-2px);
```

### "I'm building a marketing stat callout"
```css
/* Glass warm surface */
background: rgba(196,138,58,0.04);
border: 1px solid rgba(196,138,58,0.1);
backdrop-filter: blur(28px) saturate(1.3);
/* Stat number in bronze: */
color: var(--bronze-400);
```

### "I'm building a status badge"
```css
/* Use semantic colors, NOT bronze */
/* Success: */ background: rgba(74,222,128,0.12); color: var(--success);
/* Warning: */ background: rgba(240,197,67,0.12); color: var(--warning);
/* Error: */   background: rgba(240,112,104,0.12); color: var(--error);
/* Info: */    background: rgba(99,179,237,0.12); color: var(--info);
/* Accent: */  background: rgba(124,187,223,0.1); color: var(--focus);
```

### "I'm setting up a dark page background"
```css
background: var(--L0);  /* #111620 — navy, never grey */
color: var(--T1);       /* #F0EBE3 — warm cream */
```

### "I need a focus ring"
```css
outline: 2px solid var(--focus);  /* #7CBBDF — NEVER bronze */
outline-offset: 2px;
box-shadow: 0 0 0 4px rgba(124,187,223,0.2);
```


## Never Do This

| Rule | Why |
|---|---|
| Never use `#1A1A1A`, `#222`, or neutral greys for dark backgrounds | Breaks the navy temperature relationship. Bronze looks dead on grey. |
| Never use bronze (`--bronze-400`) for focus rings or active state indicators | Bronze is brand voice, not interface feedback. Use `--focus` blue. |
| Never use `--success` / `--error` / `--warning` for decorative purposes | Semantic colors carry meaning. Using green for decoration dilutes "success." |
| Never put bronze on browser-forced dark backgrounds | Renders as muddy brown-green. Always use our explicit navy L0–L5 tokens. |
| Never use `--gold-300` or lighter for text on dark backgrounds | Too low contrast. Bronze text uses `--bronze-400` minimum. |
| Never hardcode `rgba(255,255,255,0.6)` for secondary text in dark mode | Use `--T2` (`#67686B`) — it's a solid computed value, not an alpha. |


## Figma → Code Mapping

| Figma Variable / Style | CSS Token | Notes |
|---|---|---|
| `color/brand/bronze-400` | `--bronze-400` | Primary accent |
| `color/neutral/900` (dark) | `--T1` | Primary text |
| `color/neutral/400` (dark) | `--T2` | Secondary text |
| `color/focus/500` | `--focus` | Interactive accent |
| `Fill/Core/Base` | `--L0` | Deepest background |
| `Fill/Core/L1` | `--L1` | Raised surface |
| `Fill/Core/L2` | `--L2` | Overlay surface |
| `Stroke/Default` | `--border-default` | Default borders |
| `Stroke/Hover` | `--border-hover` | Hover borders |
| `color/green/500` | `--success` | Positive states |
| `color/red/500` | `--error` | Error states |
| `color/yellow/500` | `--warning` | Warning states |
| `color/blue/500` | `--info` | Informational |


## Cross-Surface Translation

| Surface | How Color Shows Up |
|---|---|
| **Product (app)** | Full token system, dark mode default, light mode optional, OLED for mobile |
| **Marketing site** | Dark mode only for external pages, bronze-heavy for brand moments |
| **Mobile** | Same tokens, OLED mode available for battery savings |
| **Print** | CMYK/Pantone values above, proof bronze before final run |
| **Merch** | Use Pantone spot colors, not CMYK process |
| **Events/experiential** | Navy backdrops, bronze accent lighting, cream for wayfinding text |
| **Social** | Dark mode palette for feed posts, bronze headlines for emphasis |
| **Email** | Dark mode with light mode fallback for clients that force light rendering |
| **Investor materials** | Full brand palette, manifesto-quality polish |
