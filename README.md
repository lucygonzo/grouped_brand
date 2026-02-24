# Grouped Design System

### Version 1.0 · February 2026
### Dark Mode Primary · Light Mode Secondary

---

## Foundation: Make the Screen Disappear

Grouped is Swiss-minimal with soul. The visual language draws from 70s modernist typography and geometric precision, then layers in warmth through bronze accents, tactile surfaces, and generous spacing. A cool focus blue handles interactive states. Every surface should feel considered, every animation intentional, every interaction like reaching into the screen and touching something real.

The system prioritizes dark mode across the marketing site, web app, and all artist-facing surfaces. Light mode exists as a secondary theme for specific contexts (documentation, print, partner-facing materials).

### Core Principles

**Cyclical.** Music lives in loops. Write, record, release, connect, repeat. Every animation should feel like it's returning to something, building on the last cycle. Rounded corners, circular motifs, spring easings that overshoot and settle. Nothing stops. Everything flows into the next beat.

**Tactile.** Glass has weight. Cards tilt when you reach for them. Stickers resist then follow your hand. Grain gives every surface a texture you can feel through the screen. The experience should remind you of handling vinyl, flipping through a crate, holding something real.

**Vibing.** Timing is feel. Fast UI feels anxious. Slow UI feels confident. Our transitions run 500ms or longer because we're not in a hurry. We're vibing. The cursor glow drifts. Cards lift and settle with weight. Everything breathes at a pace that matches sitting in a listening room, not clicking through a dashboard.

### The Extension Metaphor

Grouped should feel like an extension of the artist, not a tool they log into. When an artist opens Grouped, the screen should dissolve. No chrome, no clutter, no "app" feeling. Just them, their music, and a warm room full of fans. The physical metaphors in this system (glass, grain, warmth, tilt, weight) exist to bridge the gap between pixels and the real relationship happening underneath.

### The Test

If something feels flat, add texture. If something feels sharp, round it. If something feels fast, slow it down. If something feels static, let it breathe. The test is always the same: does this feel like a place you'd want to sit and listen to music in?

**Additional guardrails:**
- Contrast creates hierarchy (not decoration)
- Bronze is the brand voice (headlines, logos, labels, CTAs)
- Focus blue is the interface voice (stickers, badges, focus rings, active indicators)
- Typography does the heavy lifting
- Negative space is a feature

---

## 1. Color System

#### Backgrounds (Deep Blue)

Every surface carries a consistent blue undertone. Cool surfaces make the warm bronze and warm white feel intentional, and give the focus blue room to pop. Three temperature layers: cool navy surfaces, warm bronze brand elements, cool blue interactive accents.

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `--bg-base` | `#111620` | `17, 22, 32` | Page background, app shell |
| `--bg-raised` | `#181E2A` | `24, 30, 42` | Cards, modals, elevated surfaces |
| `--bg-overlay` | `#1F2735` | `31, 39, 53` | Dropdowns, popovers, floating panels |
| `--bg-subtle` | `#262F3F` | `38, 47, 63` | Hover states, selected rows, active areas |
| `--bg-muted` | `#2E3849` | `46, 56, 73` | Input fields, code blocks, inset surfaces |

#### Borders & Dividers

Borders use warm white at low opacity rather than pure white. This keeps edges soft and consistent with the warm text.

| Token | Hex | Opacity | Usage |
|---|---|---|---|
| `--border-default` | `#EBE1D2` | `7%` | Card edges, section dividers |
| `--border-hover` | `#EBE1D2` | `11%` | Hovered card edges, interactive borders |
| `--border-active` | `#EBE1D2` | `16%` | Focused inputs, selected elements |
| `--border-strong` | `#EBE1D2` | `22%` | High-contrast dividers when needed |
| `--border-accent` | `#C48A3A` | `40%` | Bronze-tinted borders for premium surfaces |

#### Text (Warm White)

Text uses a warm off-white (#F0EBE3) instead of pure white. This removes harshness and creates a reading experience that feels comfortable at any hour. The slight warmth complements the bronze accent while sitting naturally on the cool blue surfaces.

| Token | Hex | Opacity | Usage |
|---|---|---|---|
| `--text-primary` | `#F0EBE3` | `100%` | Headlines, body text, primary content |
| `--text-secondary` | `#F0EBE3` | `60%` | Descriptions, secondary labels, metadata |
| `--text-tertiary` | `#F0EBE3` | `38%` | Placeholders, disabled text, captions |
| `--text-muted` | `#F0EBE3` | `18%` | Watermarks, decorative numbers, ghost text |
| `--text-inverse` | `#111620` | `100%` | Text on light/accent backgrounds |

#### Accent: Bronze (Brand) + Focus Blue (Interactive)

The bronze palette is the brand voice. Use it for headlines, logos, section labels, CTAs, and the concentric arc motif. Never use it for interactive feedback elements like focus rings, stickers, or status badges.

Focus blue (`--focus: #7CBBDF`) handles interactive states: input focus rings, accent stickers, accent badges, active/selected indicators, and data visualization accents. The split keeps bronze feeling earned and intentional.

**The test:** if the element is part of the brand voice (something you'd see on a poster), it's bronze. If the element is part of the interface (something you'd interact with or that tells you a current state), it's focus blue.

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `--bronze-50` | `#FEF7EC` | `254, 247, 236` | Light mode tint, subtle highlights |
| `--bronze-100` | `#FDE9C8` | `253, 233, 200` | Light badges, soft glow |
| `--bronze-200` | `#FAD08E` | `250, 208, 142` | Hover accents, warm highlights |
| `--bronze-300` | `#F6B44E` | `246, 180, 78` | Secondary buttons, tags |
| `--bronze-400` | `#C48A3A` | `212, 148, 58` | **Primary brand accent. Headlines, logos, labels, CTAs.** |
| `--bronze-500` | `#B87A2E` | `184, 122, 46` | Hover state for primary accent |
| `--bronze-600` | `#916024` | `145, 96, 36` | Pressed state, deep accents |
| `--bronze-700` | `#6B471B` | `107, 71, 27` | Dark mode subtle bronze on dark surfaces |
| `--bronze-800` | `#4A3114` | `74, 49, 20` | Ghost bronze, decorative only |

#### Semantic Colors

| Token | Hex | Usage |
|---|---|---|
| `--success` | `#8BAF9C` | Confirmations, positive metrics, connected states |
| `--success-muted` | `#8BAF9C` at `15%` | Success background tint |
| `--warning` | `#D4A24B` | Caution states, approaching limits |
| `--warning-muted` | `#D4A24B` at `15%` | Warning background tint |
| `--error` | `#C27A6B` | Errors, destructive actions, disconnected states |
| `--error-muted` | `#C27A6B` at `15%` | Error background tint |
| `--info` | `#8BA4BE` | Informational, tips, neutral highlights |
| `--info-muted` | `#8BA4BE` at `15%` | Info background tint |

#### Ring System Colors (Brand Graphic)

The concentric ring motif is the core visual identity. These values control the ring animation states used across the site and product.

| Token | Hex | Opacity | State |
|---|---|---|---|
| `--ring-outer-rest` | `#2A3036` | `18%` | Default outer ring |
| `--ring-outer-active` | `#C48A3A` | `22%` | Activated outer ring (bronze glow) |
| `--ring-middle` | `#2A3036` | `28%` | Middle ring, static |
| `--ring-inner` | `#2A3036` | `42%` | Inner ring, static |
| `--ring-g-logo` | `#FFFFFF` | `6%` | G lettermark inside rings |

### 1.2 Light Mode (Secondary)

#### Backgrounds

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `--bg-base` | `#FAFAF8` | `250, 250, 248` | Page background |
| `--bg-raised` | `#FFFFFF` | `255, 255, 255` | Cards, modals |
| `--bg-overlay` | `#FFFFFF` | `255, 255, 255` | Dropdowns, popovers |
| `--bg-subtle` | `#F3F3F0` | `243, 243, 240` | Hover states, selected rows |
| `--bg-muted` | `#EAEAE6` | `234, 234, 230` | Input fields, inset surfaces |

#### Borders & Dividers (Light Mode)

| Token | Hex | Opacity | Usage |
|---|---|---|---|
| `--border-default` | `#111620` | `8%` | Card edges, section dividers |
| `--border-hover` | `#111620` | `12%` | Hovered elements |
| `--border-active` | `#111620` | `18%` | Focused inputs |
| `--border-strong` | `#111620` | `28%` | High-contrast dividers |

#### Text (Light Mode)

| Token | Hex | Opacity | Usage |
|---|---|---|---|
| `--text-primary` | `#111620` | `100%` | Headlines, body text |
| `--text-secondary` | `#111620` | `60%` | Descriptions, metadata |
| `--text-tertiary` | `#111620` | `40%` | Placeholders, captions |
| `--text-muted` | `#111620` | `20%` | Watermarks, decorative |

#### Accent (Light Mode)

Bronze accent stays the same across both modes. The `--bronze-400` primary accent has sufficient contrast on both dark and light backgrounds. On light surfaces, use `--bronze-500` or `--bronze-600` for text to maintain WCAG AA compliance.

---

## 2. Typography

### 2.1 Two Typefaces, One System

Grouped uses two typefaces with clearly separated roles. Grouped Font is the custom display face for marketing headlines and brand-forward moments. Satoshi is the system workhorse that handles everything else.

### 2.2 Grouped Font (Custom Display)

**Role:** Hero headlines, marketing section titles, brand moments, the "grouped." wordmark/logotype.

**Format:** OTF, single weight (Regular), 160 glyphs, full ASCII coverage.

**Minimum size:** 28px. Accessibility takes priority over brand expression. When in doubt, use Satoshi.

| Use Grouped Font for | Use Satoshi instead for |
|---|---|
| Hero headlines (48px+) | Body copy at any size |
| Marketing section titles (32px+) | Product UI (all of it) |
| Brand moments in pitch decks | Navigation and buttons |
| Social media graphics (large text) | Form labels and inputs |
| Print headers and posters | Any text under 28px |
| The "grouped." wordmark/logotype | Anywhere bold/medium/light weights are needed |

**Accessibility rule:** Grouped Font is a single-weight display face. It creates a distinctive brand presence at large sizes but lacks the weight range and optical refinement needed for smaller text or dense UI. Legibility always wins. If a context calls for varying weight, small sizes, or extended reading, Satoshi is the correct choice.

### 2.3 Satoshi (System Workhorse)

**Role:** Body copy, product UI, subheadings, navigation, buttons, captions, and all text under 28px.

**Source:** [Fontshare](https://www.fontshare.com/fonts/satoshi) (free for personal + commercial use)
**Weights available:** Light (300), Regular (400), Medium (500), Bold (700), Black (900), plus italics
**Variable font:** Yes (recommended for web performance)

Satoshi is a Swiss-style modernist sans serif that balances geometric precision with subtle rounded warmth. It reads clean at small sizes for product UI and punches hard at display sizes for marketing when Grouped Font is not available or appropriate. The double-storey 'a' and 'g' give it editorial credibility, while single-storey alternates (via OpenType) can be toggled for a more geometric, 70s-forward feel in display contexts.

#### Why Satoshi over TT Commons

| | TT Commons | Satoshi |
|---|---|---|
| License | Paid, per-seat | Free, open commercial |
| Web performance | Static files only | Variable font available |
| Character | Neutral corporate | Swiss modernist with 70s warmth |
| Product readability | Good | Excellent (optimized for screens) |
| Display impact | Moderate | Strong (Black weight is bold without being aggressive) |

### 2.4 Type Scale

The scale uses a 1.25 ratio (Major Third) for a clean, proportional hierarchy. All sizes assume a 16px base.

#### Marketing / Website

Headlines at `display-xl` through `display-md` use **Grouped Font**. All other sizes use **Satoshi**.

| Token | Size | Weight | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|---|
| `--display-xl` | 80px / 5rem | Black (900) | 0.95 | -0.03em | Hero headlines, section openers |
| `--display-lg` | 64px / 4rem | Black (900) | 0.98 | -0.025em | Secondary heroes, feature headlines |
| `--display-md` | 48px / 3rem | Bold (700) | 1.05 | -0.02em | Section titles |
| `--display-sm` | 36px / 2.25rem | Bold (700) | 1.1 | -0.015em | Card headlines, subsection titles |
| `--heading-lg` | 28px / 1.75rem | Bold (700) | 1.2 | -0.01em | Feature names, list headers |
| `--heading-md` | 24px / 1.5rem | Medium (500) | 1.25 | -0.005em | Subheadings, dialog titles |
| `--heading-sm` | 20px / 1.25rem | Medium (500) | 1.3 | 0 | Small headings, nav items |
| `--body-lg` | 18px / 1.125rem | Regular (400) | 1.6 | 0 | Lead paragraphs, hero subtext |
| `--body-md` | 16px / 1rem | Regular (400) | 1.6 | 0 | Default body copy |
| `--body-sm` | 14px / 0.875rem | Regular (400) | 1.5 | 0.005em | Secondary body, descriptions |
| `--caption` | 12px / 0.75rem | Medium (500) | 1.4 | 0.02em | Labels, badges, metadata |
| `--overline` | 11px / 0.6875rem | Bold (700) | 1.3 | 0.1em | Section labels, all-caps markers |

#### Product / Web App

| Token | Size | Weight | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|---|
| `--app-title` | 24px | Bold (700) | 1.2 | -0.01em | Page titles, panel headers |
| `--app-heading` | 18px | Medium (500) | 1.3 | -0.005em | Section headers, card titles |
| `--app-body` | 14px | Regular (400) | 1.5 | 0 | Default product body text |
| `--app-small` | 13px | Regular (400) | 1.45 | 0.005em | Table content, dense UI |
| `--app-label` | 12px | Medium (500) | 1.3 | 0.02em | Form labels, button text |
| `--app-caption` | 11px | Regular (400) | 1.3 | 0.02em | Timestamps, helper text |
| `--app-mono` | 13px | Regular (400) | 1.45 | 0 | Code, data values, IDs |

#### Monospace Fallback

For data-heavy contexts (metrics, code, IDs), use `JetBrains Mono` or `SF Mono` as the monospace stack:

```
font-family: 'JetBrains Mono', 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
```

### 2.5 Type Rules

**Uppercase is reserved for:**
- Overline labels (section markers like "01 / Capture")
- Button text (when under 3 words)
- Badge text
- Tab labels in the product

**Italics are reserved for:**
- Emphasis within body copy
- Song titles, album names, artistic references
- Placeholder text in editorial contexts

**Never combine** uppercase + italic.

**Headline casing:** Sentence case for all headlines. Title Case only for proper nouns and the Grouped brand name.

**Number formatting:** Use tabular figures (`font-variant-numeric: tabular-nums`) in data tables, metrics displays, and pricing. Proportional figures for body text.

---

## 3. Spacing & Layout

### 3.1 Spacing Scale

Based on 4px base unit. All spacing values are multiples of 4.

| Token | Value | Usage |
|---|---|---|
| `--space-1` | 4px | Tight padding (icon gaps, badge internal) |
| `--space-2` | 8px | Default icon-to-text gap, compact padding |
| `--space-3` | 12px | Small component padding, list item spacing |
| `--space-4` | 16px | Default component padding, form field gaps |
| `--space-5` | 20px | Medium padding, card internal spacing |
| `--space-6` | 24px | Section padding (mobile), comfortable gaps |
| `--space-8` | 32px | Large component spacing, card gaps |
| `--space-10` | 40px | Section spacing (desktop), major gaps |
| `--space-12` | 48px | Large section spacing |
| `--space-16` | 64px | Section top/bottom padding (mobile) |
| `--space-20` | 80px | Section top/bottom padding (small desktop) |
| `--space-24` | 96px | Section top/bottom padding (desktop) |
| `--space-32` | 128px | Hero section vertical padding |
| `--space-40` | 160px | Maximum section padding (wide screens) |

### 3.2 Grid System

| Property | Value |
|---|---|
| Max content width | 1200px |
| Wide content width | 1400px (for full-bleed feature sections) |
| Column count | 12 |
| Gutter (desktop) | 24px |
| Gutter (tablet) | 20px |
| Gutter (mobile) | 16px |
| Margin (desktop) | 80px |
| Margin (tablet) | 40px |
| Margin (mobile) | 20px |

### 3.3 Breakpoints

| Token | Value | Target |
|---|---|---|
| `--bp-sm` | 640px | Large phones, small tablets |
| `--bp-md` | 768px | Tablets |
| `--bp-lg` | 1024px | Small desktops, landscape tablets |
| `--bp-xl` | 1280px | Standard desktops |
| `--bp-2xl` | 1536px | Wide desktops |

### 3.4 Border Radius: Sleeves and Labels

Radius has meaning in this system. Two families, two physical metaphors.

**Sleeves** (4px): Cards, panels, containers, modals. The barely-worn edges of a vinyl sleeve pulled from a crate. Near-square, physical, stackable.

**Labels** (9999px / pill): Buttons, stickers, badges, pills, toggles. The round stickers and labels stuck to the sleeve. Soft, tactile, interactive.

The contrast between sharp containers and soft interactive elements is the system. If it holds content, it's a sleeve. If you tap it, it's a label.

| Token | Value | Family | Usage |
|---|---|---|---|
| `--radius-sleeve` | `4px` | Sleeve | Cards, panels, containers, modals, all surfaces |
| `--radius-label` | `9999px` | Label | Buttons, stickers, badges, pills |
| `--radius-sm` | `6px` | Sleeve | Small containers, thumbnails |
| `--radius-md` | `10px` | Hybrid | Inputs, dropdowns (slightly softer for form affordance) |
| `--radius-lg` | `4px` | Sleeve | Cards (mapped to sleeve) |
| `--radius-xl` | `4px` | Sleeve | Large cards (mapped to sleeve) |
| `--radius-full` | `9999px` | Label | Pills, toggles |

---

## 4. Elevation & Surface System: The Listening Room

### 4.1 Concept

Grouped is the room. Artists are the music playing in it.

Every surface is designed to elevate whatever sits on top of it. The deep blue backgrounds recede. The frosted glass softens. The subtle grain adds organic warmth. Artist content (photos, album art, video) should always be the brightest, warmest, most vivid thing on screen. Grouped never competes with the artist's visual identity.

Think: an upscale listening room with 70s warmth. Vinyl sleeves on a smoked glass coffee table. The warm glow of a tube amplifier. Minimalistic, confident, bold, and built to make the music look good.

### 4.2 Shadow System (Dark Mode)

Shadows on dark backgrounds work differently than light. Rely on border opacity and background lightness shifts rather than traditional box-shadows. When shadows are used, they should be deep and subtle.

| Token | Value | Usage |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.35)` | Subtle lift for small elements |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.4)` | Cards, dropdowns |
| `--shadow-lg` | `0 8px 32px rgba(0,0,0,0.45)` | Modals, popovers |
| `--shadow-xl` | `0 16px 48px rgba(0,0,0,0.5)` | Dialogs, full overlays |
| `--shadow-glow-gold` | `0 0 24px rgba(196,138,58,0.15)` | Bronze accent glow (CTAs, brand elements) |
| `--shadow-glow-soft` | `0 0 40px rgba(196,138,58,0.08)` | Ambient bronze glow (hero elements) |

### 4.3 Surface Types

Four surface types create depth and hierarchy.

#### Solid

The walls and floor. Structural, grounding, opaque. Use for page backgrounds, primary card containers, and navigation backgrounds.

```css
.surface-solid {
  background: var(--bg-raised);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sleeve);
}
```

#### Glass

Real frosted glass, not a CSS trick. Each glass surface is built from four layers: a subtle noise texture (SVG fractalNoise at 3% opacity), a top-edge light gradient simulating refraction, a blurred tinted base, and layered inner shadows that give the glass physical thickness.

**Glass (default):** Cool-toned frosted overlay. Use for callout cards, floating elements, overlays, and secondary containers.

```css
.surface-glass {
  background:
    /* Noise texture: gives glass its frosted grain */
    url("data:image/svg+xml,...") /* fractalNoise */,
    /* Top-edge light: refraction gradient */
    linear-gradient(180deg, rgba(235,225,210,0.04) 0%, transparent 50%),
    /* Base tint */
    rgba(24, 30, 42, 0.5);
  backdrop-filter: blur(28px) saturate(1.25) brightness(1.02);
  border: 1px solid rgba(235, 225, 210, 0.06);
  border-top-color: rgba(235, 225, 210, 0.1); /* brighter top edge */
  box-shadow:
    0 1px 0 0 rgba(235,225,210,0.06) inset,   /* top refraction line */
    1px 0 0 0 rgba(235,225,210,0.02) inset,    /* left refraction */
    0 4px 12px 0 rgba(0,0,0,0.08) inset,       /* inner depth */
    0 8px 32px rgba(0,0,0,0.25),               /* float shadow */
    0 2px 8px rgba(0,0,0,0.15);                /* close shadow */
}
```

The noise texture is critical. Without it, glass surfaces look like CSS `backdrop-filter` demos. With it, each surface has a unique quality, the same way no two panes of real frosted glass catch light identically.

**Glass Light:** Lower opacity for stacking on raised surfaces without getting too heavy.

```css
.surface-glass-light {
  background: rgba(38, 47, 63, 0.45);
  backdrop-filter: blur(16px) saturate(1.15);
  border: 1px solid rgba(235, 225, 210, 0.05);
  border-radius: var(--radius-sleeve);
}
```

**Glass Warm:** Gold-tinted for premium callouts, featured metrics, and important notices.

```css
.surface-glass-warm {
  background: rgba(196, 138, 58, 0.06);
  backdrop-filter: blur(24px) saturate(1.3);
  border: 1px solid rgba(196, 138, 58, 0.1);
  border-radius: var(--radius-sleeve);
}
```

#### Vinyl

The premium surface. A subtle warm gradient with reflective sheen. Use sparingly for hero moments, featured content, design principle callouts, and anything that needs to feel like the most important thing in the room.

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
  border-radius: var(--radius-sleeve);
  box-shadow:
    0 1px 0 0 rgba(235, 225, 210, 0.04) inset,
    0 -1px 0 0 rgba(0, 0, 0, 0.2) inset,
    0 16px 48px rgba(0, 0, 0, 0.3);
}
```

Vinyl surfaces include a 1px warm highlight along the top edge (via `::after` pseudo-element) to simulate light catching the surface.

#### Sticker

Lightweight transparent labels. Like stickers on a record sleeve or tags on a crate of vinyl. Use for badges, tags, metadata, and small interactive elements.

```css
.surface-sticker {
  background: rgba(24, 30, 42, 0.35);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(235, 225, 210, 0.04);
  border-radius: var(--radius-label);
  padding: 12px 20px;
  font-size: 13px;
  font-weight: 500;
}

/* Accent variant for highlighted tags */
.surface-sticker.sticker-bronze {
  border-color: rgba(196, 138, 58, 0.12);
  color: var(--bronze-400);
}
```

### 4.4 Grain Texture

A fixed SVG noise overlay at very low opacity (2.8%, `mix-blend-mode: overlay`) covers the entire viewport. This adds organic warmth to every surface without interfering with readability. The grain is the difference between "digital dark mode" and "a room with texture."

Apply the `grain` class to the `<body>` element. It should be present on all dark-mode pages.

### 4.5 Ambient Glow

Warm radial gradients simulate lamplight in the room. Use behind glass surfaces to create depth and warmth. Keep these subtle, off-center, and never directly behind text.

```css
.ambient-glow::before {
  content: '';
  position: absolute;
  width: 400px; height: 400px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(196, 138, 58, 0.06) 0%, transparent 70%);
  pointer-events: none;
}
```

### 4.6 Artist Content Framing

When displaying artist imagery (album art, photos, video thumbnails), use the `artist-frame` class. It adds a deep shadow and a subtle vignette that blends the image into the deep blue surroundings. Artist content should always be the most vivid, saturated element on screen.

### 4.7 The Turntable Card

A composite pattern for displaying artist releases. Album art sits on top like a record on a turntable. The card beneath is the player. Sticker labels sit over the content area.

Structure:
```
.turntable-card
  .turntable-card-art        → album art / visual (top)
  .turntable-card-content    → release info, stickers (bottom)
```

### 4.8 Surface Selection Guide

| Context | Surface | Why |
|---|---|---|
| Page background | Solid (bg-base) | Foundation layer |
| Standard cards | Solid | Structural, reliable |
| Callout / highlight cards | Glass | Draws attention through transparency |
| Metric displays | Glass Warm | Warm tint signals importance |
| Hero / featured content | Vinyl | Premium feel for top-level moments |
| Tags, badges, metadata | Sticker | Lightweight, non-intrusive |
| Overlays on artist imagery | Glass Light | Lets the art show through |
| Important notices | Glass Warm | Warm border signals "read this" |
| Design principle quotes | Vinyl | Worth the premium treatment |
| Navigation bar | Glass | Transparent, ever-present |

### 4.9 Design Principle

> Grouped is the record player. Artists make the records.
>
> Every design decision should ask: does this elevate the artist's content, or compete with it? The deep blue recedes. The warm grain adds texture without noise. The glass surfaces frame without containing. We are the foundation. They are what people came to hear.

### 4.10 Card Interaction Rules

Cards are the primary interactive surface in the system. Every card follows the same interaction language, scaled to the card's importance.

#### 3D Tilt

Cards rotate subtly toward the cursor on hover, creating a sense of physical depth. Maximum rotation is 4 degrees in any direction. The card also scales to 1.01x, lifting it slightly off the surface.

```
Transform: perspective(1200px) rotateX(±4deg) rotateY(±4deg) scale3d(1.01, 1.01, 1.01)
Timing: continuous on mousemove, no debounce (requestAnimationFrame throttled)
Reset: 800ms spring easing on mouseleave
```

#### Cursor-Following Glow

A warm gold radial gradient (500px radius, 7% opacity) follows the cursor position across the card surface. This simulates lamplight hitting the glass. The glow is applied via CSS custom properties (`--card-glow-x`, `--card-glow-y`) updated on mousemove.

```css
background: radial-gradient(
  500px circle at var(--card-glow-x) var(--card-glow-y),
  rgba(196, 138, 58, 0.07) 0%,
  transparent 55%
);
```

#### Edge Light

A second radial gradient (400px, 25% opacity gold fading to 6% warm white) renders behind the card border using a CSS mask. This creates a glow along the card edge nearest to the cursor. The edge light appears on hover at 500ms ease-in.

#### Shadow Expansion

On hover, shadows deepen and expand. A very faint gold ambient glow (0.03 opacity, 80px blur) is added beneath the card for warmth.

```
Rest:  0 8px 32px rgba(0,0,0,0.25)
Hover: 0 20px 60px rgba(0,0,0,0.35), 0 0 80px rgba(196,138,58,0.03)
```

#### Inner Content Shift

On comp-cards, inner content translates 10px on the Z axis on hover (`translateZ(10px)`), creating a subtle parallax between the card surface and its contents.

#### Sticker Magnetic Pull

Stickers follow the cursor with a 15% offset on both axes, creating a subtle magnetic attraction effect. On mouseleave, they spring back to center over 500ms.

#### Timing Hierarchy

All card interactions use slow, cinematic timing. Nothing should feel snappy or mechanical.

| Element | Enter Duration | Exit Duration | Easing |
|---|---|---|---|
| 3D Tilt | Continuous (rAF) | 800ms | cubic-bezier(0.16, 1, 0.3, 1) |
| Cursor Glow | Continuous (rAF) | 500ms | ease |
| Edge Light | 500ms | 500ms | ease |
| Shadow | 600ms | 600ms | cubic-bezier(0.16, 1, 0.3, 1) |
| Sticker Magnetic | Continuous (rAF) | 500ms | cubic-bezier(0.16, 1, 0.3, 1) |
| Content Shift | 600ms | 600ms | cubic-bezier(0.16, 1, 0.3, 1) |

#### Accessibility

All card interactions respect `prefers-reduced-motion: reduce`. When reduced motion is active, no tilt, no glow tracking, no magnetic pull. Cards still respond with basic hover state changes (border-color, subtle shadow) for interactive feedback.

---

## 5. Components

### 5.1 Buttons

#### Primary (Gold)

```
Background: --bronze-400 (#C48A3A)
Text: --text-inverse (#111620)
Font: Satoshi Bold, 14px, uppercase, 0.04em tracking
Padding: 12px 28px
Border-radius: --radius-label (pill)
Height: 44px (touch target)

Hover: --bronze-500, scale(1.02), transition 200ms ease-out
Active: --bronze-600, scale(0.98)
Disabled: --bronze-400 at 40% opacity, cursor not-allowed
```

#### Secondary (Ghost)

```
Background: transparent
Border: 1px solid rgba(255,255,255,0.12)
Text: --text-primary (#F0EBE3)
Font: Satoshi Medium, 14px
Padding: 12px 28px
Border-radius: --radius-label (pill)

Hover: background rgba(255,255,255,0.04), border rgba(255,255,255,0.18)
Active: background rgba(255,255,255,0.06)
```

#### Tertiary (Text)

```
Background: transparent
Text: --bronze-400
Font: Satoshi Medium, 14px
Padding: 8px 4px

Hover: text --bronze-300, underline offset 4px
Active: text --bronze-500
```

#### Button Sizes

| Size | Height | Padding | Font Size |
|---|---|---|---|
| Small | 36px | 8px 20px | 13px |
| Default | 44px | 12px 28px | 14px |
| Large | 52px | 16px 36px | 16px |

### 5.2 Inputs

```
Background: --bg-muted (#2E3849)
Border: 1px solid rgba(255,255,255,0.08)
Border-radius: --radius-label (pill)
Text: --text-primary
Placeholder: --text-tertiary
Padding: 12px 16px
Height: 44px
Font: Satoshi Regular, 14px

Focus: border --bronze-400 at 60%, box-shadow --shadow-glow-gold at 50% intensity
Error: border --error, box-shadow 0 0 0 3px rgba(248,113,113,0.15)
Disabled: opacity 0.5
```

### 5.3 Cards

```
Background: --bg-raised (#181E2A)
Border: 1px solid rgba(255,255,255,0.06)
Border-radius: --radius-lg (16px)
Padding: 24px (desktop), 20px (mobile)

Hover (interactive): border rgba(255,255,255,0.10),
                     transform translateY(-2px),
                     transition 300ms cubic-bezier(0.16, 1, 0.3, 1)
```

### 5.4 Badges / Tags

```
Background: rgba(255,255,255,0.06)
Border: 1px solid rgba(255,255,255,0.08)
Border-radius: --radius-full (pill)
Text: --text-secondary
Font: Satoshi Medium, 12px, 0.02em tracking
Padding: 4px 12px
Height: 28px

Variant (gold): background rgba(196,138,58,0.12), border rgba(196,138,58,0.2), text --bronze-300
Variant (success): background rgba(52,211,153,0.12), border rgba(52,211,153,0.2), text --success
```

### 5.5 Navigation

#### Top Nav (Marketing)

```
Position: fixed top, full-width
Height: 64px
Background: transparent (scrolled: glass-surface)
Transition: background 300ms ease, backdrop-filter 300ms ease
Border-bottom (scrolled): 1px solid rgba(255,255,255,0.06)
z-index: 100

Logo: Satoshi Bold, 20px, --text-primary
Nav links: Satoshi Medium, 14px, --text-secondary
Nav link hover: --text-primary, transition 150ms
CTA button: Primary small variant
```

#### App Sidebar

```
Width: 240px (expanded), 64px (collapsed)
Background: --bg-raised
Border-right: 1px solid rgba(255,255,255,0.06)
Transition: width 300ms cubic-bezier(0.16, 1, 0.3, 1)

Nav item: 
  Padding: 10px 16px
  Border-radius: --radius-md
  Font: Satoshi Medium, 14px
  Color: --text-secondary
  
Nav item active:
  Background: rgba(196,138,58,0.08)
  Color: --bronze-400
  Border-left: 2px solid --bronze-400 (optional)
```

### 5.6 Metrics / Stats Display

Used for the results section, dashboard, and anywhere numbers need impact.

```
Number: Satoshi Black, --display-lg or --display-md, --text-primary
        font-variant-numeric: tabular-nums
Label: Satoshi Medium, --caption, --text-secondary, uppercase, 0.06em tracking
Container: vertical stack, --space-2 gap

Animation: countUp on scroll-enter, 1200ms, easeOutExpo
```

### 5.7 Section Labels (00 / 01 / 02 / 03)

The numbered section system is a key visual device for the marketing site.

```
Number: Satoshi Bold, 14px, --text-muted (24% white), 0.04em tracking
Divider: " / " in --text-tertiary
Label: Satoshi Bold, 14px, uppercase, --bronze-400, 0.06em tracking

Example output: "01 / Capture"
```

---

## 6. Brand Elements & Textures

### 6.1 The Signature Motif: Concentric Arcs

Sound waves. Vinyl grooves. Ripples expanding outward. The concentric arc is Grouped's signature mark. It represents the core product idea: something starts at the center (the artist, the release) and radiates outward to reach more people.

**Rules:**
- Heavy strokes with tight gaps. Stroke width is always larger than the gap (roughly 2.5:1 ratio)
- All rings in a set use the same stroke weight and color. No variation.
- No gradients. No feathering. No per-ring opacity changes. Solid lines.
- For subtle background use: heavy strokes, reduce group opacity (5-10%)
- For bold use: solid arcs on a colored field (bronze, etc.), darker tone of the field color
- 3 to 6 arcs per group

**Stroke math (for implementation):**
- Period = stroke-width + gap
- Target ratio: stroke 2.5x the gap
- Example: stroke-width 34, gap 14, period 48

**Usage contexts:**
- **Subtle (group opacity 5-10%):** Background texture. Heavy strokes still read at low opacity.
- **Bold (full opacity on colored field):** Bronze background with slightly darker bronze arcs. Poster hero, social assets.
- **Monogram:** Same heavy construction. The crossbar break creates the G.

### 6.2 Physical Controls

Controls borrowed from studio hardware, stripped to their structural essence. No gradients on controls. No metallic effects. No embossing. The shape communicates the function.

**Volume Dial:** Flat-fill circle. Thin track ring around the outside. Indicator line from center to current value. Active arc in bronze at 40% opacity. Tick marks as simple 1-1.5px strokes. Center dot for orientation.

**Mixing Fader:** Thin 2px track line. Flat rectangle handle with 1px border and minimal grip lines. Active fill in bronze at 40% opacity. Tick marks on the side.

**Power Toggle:** Pill-shaped track with flat circle thumb. Off: dark fill, subtle border. On: bronze tinted track (15% opacity), solid bronze thumb. No shadows, no glow.

**Hardware Rule:** Controls are flat and structural. No gradients on controls themselves. Shapes communicate function: circles rotate, rectangles slide, pills toggle. The only warmth comes from bronze as the active/indicator color at 40% opacity. The room provides the atmosphere; the controls stay clean.

### 6.3 Badge & Patch Treatment

Concentric rounded borders in the brand palette create a retro badge feel. Use for special moments: launch announcements, year-in-review, limited drops, artist features.

**Monochrome badge:** Single bronze border with outer shadow ring. Clean, premium.
**Multi-color badge:** Layered borders (bronze outer, burnt orange mid, slate blue inner). The full 70s patch.
**Circle badge:** Round variant for member badges, achievement icons, wallet passes.

Badge borders use `box-shadow` stacking for the concentric ring effect:
```css
box-shadow:
  0 0 0 7px var(--bg-raised),    /* gap */
  0 0 0 10px #B86E3A,             /* middle ring */
  0 0 0 14px var(--bg-raised),    /* gap */
  0 0 0 17px #7B8FAE;             /* outer ring */
```

### 6.4 Texture Patterns

The concentric arc pattern at poster scale. SVG-based, scalable.

**Subtle:** Heavy strokes (38px+ in a 600-unit viewBox), entire SVG group at 5-10% opacity. The weight still reads even at low opacity because the strokes are thick.
**Bold:** Bronze background field. Arcs in a slightly darker tone of the field (rgba black at 12% over bronze). Same heavy strokes.

### 6.5 The Contrast Principle

Controls are flat and structural. The room around them (glass surfaces, grain texture, ambient glow) provides the warmth. This contrast is intentional: crisp UI elements sitting inside a warm, textured environment. The only gradients allowed are the ones mimicking warm studio light on surfaces, never on the controls themselves.

---

## 7. Motion & Animation

### 6.1 Easing Library

| Token | Value | Usage |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Default for entering/appearing elements |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Morphing, layout shifts |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Bouncy micro-interactions (badges, toasts) |
| `--ease-smooth` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Slow, cinematic movements |
| `--ease-snap` | `cubic-bezier(0.5, 0, 0, 1)` | Quick snaps (tabs, toggles) |

### 6.2 Duration Scale

| Token | Value | Usage |
|---|---|---|
| `--duration-instant` | 100ms | Hover color changes, cursor feedback |
| `--duration-fast` | 200ms | Button states, toggle flips |
| `--duration-default` | 300ms | Card hovers, nav transitions |
| `--duration-moderate` | 500ms | Panel slides, modal enter |
| `--duration-slow` | 800ms | Section reveals, scroll-triggered |
| `--duration-cinematic` | 1200ms | Hero entrances, page transitions |

### 6.3 Scroll-Triggered Animations

All scroll animations use IntersectionObserver with a 15% threshold by default. Elements animate once and stay visible (no reverse on scroll-up).

#### Fade Up (Default Entry)

```css
.fade-up {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 800ms var(--ease-out),
              transform 800ms var(--ease-out);
}
.fade-up.visible {
  opacity: 1;
  transform: translateY(0);
}
```

Stagger children by 80ms each for grouped content:
```css
.fade-up.visible:nth-child(1) { transition-delay: 0ms; }
.fade-up.visible:nth-child(2) { transition-delay: 80ms; }
.fade-up.visible:nth-child(3) { transition-delay: 160ms; }
```

#### Fade In (No Movement)

For elements that should appear without vertical displacement:
```css
.fade-in {
  opacity: 0;
  transition: opacity 600ms var(--ease-smooth);
}
```

#### Scale Reveal (Cards, Images)

```css
.scale-reveal {
  opacity: 0;
  transform: scale(0.95);
  transition: opacity 600ms var(--ease-out),
              transform 600ms var(--ease-out);
}
```

#### Counter Animation

Metrics and numbers animate from 0 to their target value using easeOutExpo over 1200ms. Trigger on scroll-enter with IntersectionObserver.

### 6.4 Scroll-Driven Sections (GSAP / ScrollTrigger)

The marketing site uses scroll-driven state machines for immersive sections. These are the patterns from the current site, documented for consistency:

#### Ring Transition (Overview to Discovery)

- 200vh scroll container with sticky 100vh viewport
- Phase 1 (0-50% scroll): Overview text fades out, rings dissolve from inner to outer
- Phase 2 (50-100% scroll): Discovery content fades in
- Outer ring transitions from `--ring-outer-rest` to `--ring-outer-active` (gray to gold)
- Uses smoothstep easing for organic feel

#### Grow Section State Machine

- 400vh scroll container with sticky viewport
- 4 states triggered at scroll quartiles (0%, 25%, 50%, 75%)
- Content panels snap between states
- Ring graphic animates through 5 visual states with slight offset from content transitions
- Ring states lead content by ~10% scroll progress for visual anticipation

#### Feature Cards Horizontal Scroll

- Section height scales with card count
- Cards translate horizontally as user scrolls vertically
- Active card gets full opacity + scale, siblings dim
- Stacking ring counter tracks progress (fills ring by ring)

#### Snake Line Transition

- SVG path-based line between sections
- strokeDashoffset animates from full length to 0 on scroll
- Smoothstep easing applied to progress value

### 6.5 Micro-Interactions

| Element | Trigger | Animation |
|---|---|---|
| Button hover | mouseenter | Scale 1.02, color shift, 200ms ease-out |
| Button press | mousedown | Scale 0.98, 100ms |
| Card hover | mouseenter | TranslateY -2px, border brighten, 300ms ease-out |
| Link hover | mouseenter | Gold underline slides in from left, 200ms |
| Nav scroll | scroll > 60px | Glass blur fades in, 300ms |
| Hero words | 3s interval | Current word fades out (400ms), new word fades in |
| Toast enter | trigger | SlideY -100% to 0, fade in, 300ms spring |
| Modal enter | trigger | Scale 0.95 to 1, fade in, 400ms ease-out |
| Modal backdrop | trigger | Fade in 300ms |

### 6.6 Page Transitions (Future / Barba.js)

When implementing SPA-style page transitions:

```
Exit: current page fades out (300ms) while sliding up slightly (translateY -20px)
Enter: new page fades in (500ms ease-out) from translateY 20px
Duration total: ~600ms
Background: maintain --bg-base continuity (no flash)
```

### 6.7 Motion Principles

1. **Scroll drives narrative.** Major marketing sections are scroll-driven state machines, not decorative parallax. Every scroll increment advances the story.
2. **Motion has mass.** Elements feel like they have weight. Use ease-out curves for entering (decelerating) and ease-in curves for exiting (accelerating). Avoid linear.
3. **Stagger creates rhythm.** Groups of elements enter with 60-100ms stagger. This creates a left-to-right or top-to-bottom reading flow that feels intentional.
4. **Gold glows, never flashes.** When the accent color appears in animation (ring transitions, active states), it fades in gradually. A 400ms+ transition minimum for gold reveals.
5. **Subtlety at rest, confidence in motion.** Resting states are quiet and minimal. Transitions between states are bold and decisive. No halfway animations.

---

## 8. Iconography

### 7.1 Icon Style

Use a consistent outlined icon set with 1.5px stroke weight. Recommended sets that match the Grouped aesthetic:

- **Lucide** (open source, React-ready, 1.5px stroke default)
- **Phosphor** (alternative, slightly rounder, more weights available)

| Property | Value |
|---|---|
| Default size | 20px |
| Small size | 16px |
| Large size | 24px |
| Stroke width | 1.5px |
| Corner radius | Rounded caps and joins |
| Color | Inherits parent text color |

### 7.2 Emoji Usage

The current site uses emoji as feature icons (🔗 🎧 📥 📡 🔔 👤 📣 🎁 💰). This is acceptable for the marketing site in a casual context, but the product UI should use the icon set above. If emoji are used on the marketing site, keep them inside colored badge containers for visual consistency.

---

## 9. Imagery & Graphic Language

### 8.1 The Ring Motif

The concentric ring system (three rings + G lettermark) is the primary brand graphic. It appears in:

- Hero section (large, animated)
- Section transitions (dissolving/reforming)
- Feature section progress indicator (stacking rings)
- Favicon / app icon (simplified)

**Ring proportions:**
- Outer ring: 100% of container
- Middle ring: ~68% of outer
- Inner ring: ~42% of outer
- G lettermark: centered, ~20% of outer

**Ring fill:** Always use low opacity fills (6-42%) with the ring color tokens. Rings are atmospheric, not solid.

### 8.2 Product Mockups

When showing the Grouped product in marketing contexts:

- Dark background mockups only (match the product's native dark mode)
- Rounded corners on device frames (16px radius)
- Subtle shadow beneath (`--shadow-lg`)
- Slight perspective rotation is acceptable (max 5 degrees) for depth
- Never show the product on a light/white device frame

### 8.3 Photography

When photography is used (artist photos, case studies):

- High contrast, slightly desaturated
- Warm color grade that complements the gold accent
- Dark vignetting preferred
- Crop tight, show energy and intimacy
- Never use stock photography with studio lighting

---

## 10. CSS Custom Properties (Implementation Reference)

### 9.1 Dark Mode Root

```css
:root,
[data-theme="dark"] {
  /* Backgrounds (Deep Blue) */
  --bg-base: #111620;
  --bg-raised: #181E2A;
  --bg-overlay: #1F2735;
  --bg-subtle: #262F3F;
  --bg-muted: #2E3849;

  /* Borders (Warm White at Low Opacity) */
  --border-default: rgba(235,225,210,0.07);
  --border-hover: rgba(235,225,210,0.11);
  --border-active: rgba(235,225,210,0.16);
  --border-strong: rgba(235,225,210,0.22);

  /* Text (Warm White) */
  --text-primary: #F0EBE3;
  --text-secondary: rgba(240,235,227,0.6);
  --text-tertiary: rgba(240,235,227,0.38);
  --text-muted: rgba(240,235,227,0.18);
  --text-inverse: #111620;

  /* Gold Accent */
  --bronze-50: #FEF7EC;
  --bronze-100: #FDE9C8;
  --bronze-200: #FAD08E;
  --bronze-300: #F6B44E;
  --bronze-400: #C48A3A;
  --bronze-500: #B87A2E;
  --bronze-600: #916024;
  --bronze-700: #6B471B;
  --bronze-800: #4A3114;

  /* Semantic */
  --success: #8BAF9C;
  --warning: #D4A24B;
  --error: #C27A6B;
  --info: #8BA4BE;

  /* Elevation */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.5);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.6);
  --shadow-xl: 0 16px 48px rgba(0,0,0,0.7);
  --shadow-glow-gold: 0 0 24px rgba(196,138,58,0.15);

  /* Motion */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);

  /* Radius */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-full: 9999px;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
  --space-32: 128px;
}
```

### 9.2 Light Mode Override

```css
[data-theme="light"] {
  --bg-base: #FAFAF8;
  --bg-raised: #FFFFFF;
  --bg-overlay: #FFFFFF;
  --bg-subtle: #F3F3F0;
  --bg-muted: #EAEAE6;

  --border-default: rgba(9,9,11,0.08);
  --border-hover: rgba(9,9,11,0.12);
  --border-active: rgba(9,9,11,0.18);
  --border-strong: rgba(9,9,11,0.28);

  --text-primary: #111620;
  --text-secondary: rgba(9,9,11,0.6);
  --text-tertiary: rgba(9,9,11,0.4);
  --text-muted: rgba(9,9,11,0.2);
  --text-inverse: #F0EBE3;

  --shadow-sm: 0 1px 2px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.1);
  --shadow-xl: 0 16px 48px rgba(0,0,0,0.14);
  --shadow-glow-gold: 0 0 24px rgba(196,138,58,0.1);
}
```

---

## 11. Figma Structure (Component Library)

### 10.1 File Organization

```
Grouped Design System
├── 📐 Foundations
│   ├── Colors (all tokens as Figma variables)
│   ├── Typography (text styles)
│   ├── Spacing (auto layout presets)
│   ├── Grid (frame presets)
│   └── Elevation (effect styles)
├── 🧩 Components
│   ├── Buttons (primary, secondary, tertiary + sizes + states)
│   ├── Inputs (text, select, checkbox, radio, toggle + states)
│   ├── Cards (content card, feature card, metric card, case study)
│   ├── Navigation (top nav, sidebar, mobile menu, breadcrumb)
│   ├── Badges (default, gold, success, info, warning, error)
│   ├── Modals (small, medium, large + overlay)
│   ├── Toasts (success, error, info, warning)
│   ├── Section Labels ("01 / Capture" format)
│   └── Metrics Display (single stat, stat group, stat card)
├── 🎨 Brand
│   ├── Logo (primary, icon, wordmark + lockups)
│   ├── Ring Motif (static + animation states)
│   └── Icon Set (Lucide subset, 20px standard)
├── 📱 Patterns
│   ├── Hero Section (dark, with ring animation frames)
│   ├── Feature Section (horizontal scroll layout)
│   ├── Metrics Bar (social proof row)
│   ├── Case Study Card Grid
│   ├── Pricing Table
│   └── CTA Section
└── 📖 Guidelines
    ├── Usage Rules (do/don't examples)
    ├── Motion Spec (animation reference frames)
    └── Voice & Tone (visual writing style)
```

### 10.2 Figma Variable Modes

Set up two variable modes in Figma:
- **Mode 1: Dark** (default)
- **Mode 2: Light**

All color tokens should be defined as Figma variables with both mode values. This enables instant theme switching on any frame.

### 10.3 Component Naming Convention

```
Category / Component / Variant / State

Examples:
Button / Primary / Default / Rest
Button / Primary / Default / Hover
Button / Primary / Large / Disabled
Card / Feature / With Icon / Rest
Input / Text / Default / Focus
Input / Text / Default / Error
Nav / Top / Marketing / Scrolled
Badge / Default / Gold
```

---

## 12. Accessibility

### 11.1 Contrast Requirements

All text must meet WCAG AA minimum contrast ratios:

| Combination | Ratio | Pass? |
|---|---|---|
| `--text-primary` on `--bg-base` | 18.4:1 | AA + AAA |
| `--text-secondary` on `--bg-base` | 10.8:1 | AA + AAA |
| `--text-tertiary` on `--bg-base` | 7.0:1 | AA |
| `--bronze-400` on `--bg-base` | 6.8:1 | AA (large text) |
| `--bronze-300` on `--bg-base` | 8.9:1 | AA |
| `--text-inverse` on `--bronze-400` | 5.2:1 | AA |

**For gold text on dark backgrounds:** Use `--bronze-300` (#F6B44E) instead of `--bronze-400` for body-size text to ensure AA compliance. `--bronze-400` is acceptable for large text (18px+ or 14px+ bold) and interactive elements where the surrounding context provides additional visual cues.

### 11.2 Focus States

All interactive elements must have visible focus indicators:

```css
:focus-visible {
  outline: 2px solid var(--bronze-400);
  outline-offset: 2px;
}
```

### 11.3 Motion Preferences

Respect `prefers-reduced-motion`:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 13. Voice & Tone (Visual)

The design system's visual voice matches the brand's written voice:

| Written Voice | Visual Expression |
|---|---|
| Confident, not arrogant | Bold type, generous whitespace, no clutter |
| Warm, not soft | Gold accents, rounded radius, warm-white text |
| Direct, not blunt | Clear hierarchy, strong CTAs, simple layouts |
| Ambitious, not hypey | Dark, elevated surfaces. Show quality through restraint. |
| Artist-first, not corporate | Real textures, real photography, no generic SaaS gradients |

### What This System Avoids

- Neon/electric gradients (too SaaS-generic)
- Blue as a primary color (too corporate/tech)
- Sharp 0px radius (too harsh for the warmth we need)
- Thin/hairline fonts (too fragile for the bold message)
- Heavy drop shadows (too dated)
- Decorative illustrations (too playful for the premium positioning)
- Auto-playing video (too aggressive)

---

*Grouped Design System v1.0*
*February 2026*
*Next: Figma component library build, animation prototype file, and campaign extension guide.*
