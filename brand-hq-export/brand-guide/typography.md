---
section: typography
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
  - date: 2026-03-15
    change: Satoshi Semibold 600 remapped to Bold 700 (font doesn't have 600)
    source: Figma audit with Pranesh
  - date: 2026-03-15
    change: D4 confirmed as Medium 500 (Figma's choice over brand guide's Regular 400)
    source: Figma audit with Pranesh
---

# Typography

Two typefaces, one system. Anacrusis is the custom display face for the biggest brand moments. Satoshi handles everything else. Type should feel confident and unhurried.

## Fonts

### Anacrusis (Custom Display)
- Single weight, OTF format, 160 glyphs, full ASCII
- Key traits: rounded geometric, single-storey "a", pill-shaped terminals, monolinear strokes
- Letter-spacing: -0.02em at large display sizes, +0.02em at character set sizes
- Line-height: 0.95 to 1.25 depending on size

**Font stack:**
```css
font-family: 'Anacrusis', 'Satoshi', sans-serif;
```

**Files:**
- OTF: for design tools (Figma, Illustrator, InDesign)
- TTF: for web embedding and CSS @font-face

### Satoshi (System Workhorse)
- Five weights: Light 300, Regular 400, Medium 500, Bold 700, Black 900
- **No Semibold 600** — all Semibold intent maps to Bold 700

**Font stack:**
```css
font-family: 'Satoshi', -apple-system, BlinkMacSystemFont, sans-serif;
```

**Source:** `https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap`

### JetBrains Mono (Code)
- For code, data values, hex codes, token names
- Two weights: Regular 400, Medium 500

**Source:** `https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap`


## Anacrusis Rules

### Where to Use
- Hero headlines (48px+ marketing, 40px+ product)
- Marketing section titles (32px+)
- Brand moments in pitch decks
- Social media graphics (large text)
- Print headers and posters
- The "grouped." wordmark/logotype

### Where NOT to Use
- Body copy at any size
- Product UI (all of it, except D0 and D1)
- Navigation and buttons
- Form labels and inputs
- Any text under 32px (marketing) or 40px (product)
- Anywhere bold/medium/light weights are needed

### Product Usage
- **D0** (96px) and **D1** (40px) display hero moments only — onboarding, pricing, celebration states
- Maximum 2 instances of Anacrusis per screen
- H1–H5 headings stay Satoshi — Anacrusis is for *moments*, headings are for *structure*
- No inline mixing — Anacrusis and Satoshi don't sit on the same text line


## Marketing Type Scale

| Token | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| display-xl | 80px | Black 900 | -0.03em | 0.95 |
| display-lg | 64px | Black 900 | -0.025em | 0.95 |
| display-md | 48px | Bold 700 | -0.02em | 1.0 |
| display-sm | 36px | Bold 700 | -0.015em | 1.1 |
| heading-lg | 28px | Bold 700 | -0.01em | 1.2 |
| heading-md | 24px | Medium 500 | -0.005em | 1.3 |
| body-lg | 18px | Regular 400 | normal | 1.6 |
| body-md | 16px | Regular 400 | normal | 1.6 |
| body-sm | 14px | Regular 400 | normal | 1.5 |
| caption | 12px | Medium 500 | 0.02em | 1.4 |
| overline | 11px | Bold 700 | 0.1em | 1.2 |


## Product Type Scale

### Display (Anacrusis + Satoshi fallback)
| Token | Size | Weight | Letter-spacing | Line-height | Font |
|---|---|---|---|---|---|
| D0 | 96px | Bold 700 | -4% | 1.2 | Anacrusis |
| D1 | 40px | Bold 700 | -3% | 1.15 | Anacrusis |

### Display (Satoshi)
| Token | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| D2 | 36px | Bold 700 | -2.5% | 1.1 |
| D3 | 32px | Bold 700 | -2% | 1.15 |
| D4 | 24px | Medium 500 | -1% | 1.25 |
| D5 | 20px | Bold 700 | -0.5% | 1.3 |
| D6 | 18px | Bold 700 | -0.3% | 1.4 |

### Heading
| Token | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| H1 | 20px | Bold 700 | -0.5% | 1.3 |
| H2 | 18px | Bold 700 | -0.3% | 1.4 |
| H3 | 16px | Bold 700 | -0.2% | 1.4 |
| H4 | 14px | Bold 700 | 0 | 1.5 |
| H5 | 13px | Bold 700 | 0 | 1.45 |

### Body
| Token | Size | Weight | Line-height |
|---|---|---|---|
| Body | 14px | Regular 400 | 1.5 |
| Body Emphasized | 14px | Medium 500 | 1.5 |

### Caption
| Token | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| Caption | 12px | Medium 500 | 0.2% | 1.4 |
| Caption Emphasized | 12px | Bold 700 | 0.2% | 1.4 |

### Component (Product-only override)
| Token | Size | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| C1 | 18px | Bold 700 | 0.5% | 1.0 |
| C2 | 16px | Bold 700 | 0.5% | 1.0 |
| C3 | 14px | Bold 700 | 0.5% | 1.0 |
| C4 | 13px | Bold 700 | 1% | 1.0 |
| C5 | 12px | Bold 700 | 1% | 1.0 |
| C6 | 11px | Bold 700 | 2% | 1.25 |
| C7 | 10px | Bold 700 | 3% | 1.0 |

The Component scale (C1–C7) is the only intentional product override from the marketing type system. Used for buttons, nav items, and badges. All caps with tight line-height. Satoshi only.


## Weight Hierarchy

After the Semibold remap:
```
Light    300  — display accents, decorative
Regular  400  — body copy, default
Medium   500  — emphasis, labels, captions
Bold     700  — headings, buttons, strong emphasis
Black    900  — display headlines (marketing only)
```

No 600 weight exists in Satoshi. All Semibold references in Figma or code should be Bold 700.


## Common Recipes

### "I'm building a product page heading"
```css
/* H1 — Satoshi, never Anacrusis */
font-family: 'Satoshi', -apple-system, sans-serif;
font-size: 20px;
font-weight: 700;
letter-spacing: -0.5%;
line-height: 1.3;
color: var(--T1);
```

### "I'm building a hero section for marketing"
```css
/* Anacrusis display headline */
font-family: 'Anacrusis', 'Satoshi', sans-serif;
font-size: clamp(48px, 8vw, 96px);
font-weight: normal;  /* single weight — NEVER bold */
letter-spacing: -0.03em;
line-height: 0.95;
color: var(--T1);
/* Subtitle below in Satoshi */
font-family: 'Satoshi', sans-serif;
font-size: clamp(16px, 2vw, 20px);
color: var(--T2);
```

### "I'm building a button label"
```css
/* C3 Component — all caps, tight */
font-family: 'Satoshi', sans-serif;
font-size: 14px;
font-weight: 700;
letter-spacing: 0.02em;
text-transform: uppercase;
line-height: 1.0;
```

### "I'm building a caption or metadata line"
```css
font-family: 'Satoshi', sans-serif;
font-size: 12px;
font-weight: 500;
letter-spacing: 0.02em;
line-height: 1.4;
color: var(--T2);
```

### "I'm showing a code value or token name"
```css
font-family: 'JetBrains Mono', monospace;
font-size: 12px;
font-weight: 400;
color: var(--T3);
```


## Never Do This

| Rule | Why |
|---|---|
| Never use Anacrusis below 32px (marketing) or 40px (product) | Single-weight display face — illegible at small sizes |
| Never bold Anacrusis (`font-weight: bold`) | It only has one weight. Bolding distorts the glyphs. |
| Never use Anacrusis for body text, nav, buttons, or form labels | It's for moments, not structure. Satoshi handles all functional text. |
| Never use `font-weight: 600` (Semibold) | Satoshi doesn't have it. Use 700 (Bold) instead. |
| Never put Anacrusis and Satoshi on the same text line | They don't mix inline. Separate by block. |
| Never use more than 2 Anacrusis instances per screen | It loses its impact. Scarcity is what makes it feel earned. |
| Never set body text below 14px in product | 14px is the product body floor for readability. |


## Figma → Code Mapping

| Figma Text Style | CSS Tokens | Font |
|---|---|---|
| `D0 / Display Hero` | 96px, Bold 700, -4% ls, 1.2 lh | Anacrusis |
| `D1 / Display XXL` | 40px, Bold 700, -3% ls, 1.15 lh | Anacrusis |
| `D2 / Display XL` | 36px, Bold 700, -2.5% ls, 1.1 lh | Satoshi |
| `D3 / Display L` | 32px, Bold 700, -2% ls, 1.15 lh | Satoshi |
| `D4 / Display M` | 24px, Medium 500, -1% ls, 1.25 lh | Satoshi |
| `D5 / Display S` | 20px, Bold 700, -0.5% ls, 1.3 lh | Satoshi |
| `D6 / Display XS` | 18px, Bold 700, -0.3% ls, 1.4 lh | Satoshi |
| `H1–H5` | See heading table above | Satoshi |
| `Body` | 14px, Regular 400, 1.5 lh | Satoshi |
| `Body Emphasized` | 14px, Medium 500, 1.5 lh | Satoshi |
| `Caption` | 12px, Medium 500, 0.2% ls, 1.4 lh | Satoshi |
| `C1–C7` | See component table above | Satoshi |

**Variable mapping:**
- `font/size/6xl` → 96px (D0)
- `font/size/5xl` → 40px (D1)
- `font/weight/Bold` → 700
- `font/weight/Medium` → 500
- `font/line-height/6xl` → 116px (D0)


## Cross-Surface Translation

| Surface | How Type Shows Up |
|---|---|
| **Product (app)** | Full D0–C7 scale, Satoshi-dominant, Anacrusis for D0/D1 only |
| **Marketing site** | Anacrusis for display headlines (32px+), Satoshi for everything else |
| **Mobile** | D0 caps at 48px, D1 caps at 28px, body stays 14px |
| **Print** | Anacrusis for headlines, Satoshi for body. Embed OTF for print workflows |
| **Social** | Anacrusis for large text, Satoshi for captions. Bold weight for readability at feed scale |
| **Email** | Satoshi only (Anacrusis won't load in email clients). Use web-safe fallback stack |
| **Investor materials** | Anacrusis headlines, Satoshi body. Same rules as marketing |
