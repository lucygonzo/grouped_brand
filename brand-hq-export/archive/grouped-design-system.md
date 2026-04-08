# Grouped Design System

Reference for building websites, apps, and product interfaces.

Last updated: February 2026


## Philosophy

Every decision serves one goal: make the digital experience feel physical.

**Cyclical.** Music lives in loops. Write, record, release, connect, repeat. Animations should feel like they're returning to something, building on the last cycle. Spring easings that overshoot and settle. Nothing stops. Everything flows into the next beat.

**Tactile.** Glass has weight. Cards tilt when you reach for them. Grain gives every surface a texture you can feel through the screen. The experience should remind you of handling vinyl, flipping through a crate, holding something real.

**Vibing.** Timing is feel. Fast UI feels anxious. Slow UI feels confident. Transitions run 500ms or longer. The cursor glow drifts. Cards lift and settle with weight. Everything breathes at the pace of a listening room, not a dashboard.

**The core principle:** Grouped is the room. Artists are the reason people walked in. Every design decision should ask: does this elevate the artist's content, or compete with it?


## Typography

Two typefaces, one system. Grouped Font for the largest display moments, Satoshi for everything else.

### Grouped Font (Custom Display)
- Single weight, OTF, 160 glyphs, full ASCII
- Used for: hero headlines (40px+), marketing section titles (32px+), brand moments in pitch decks, social media graphics (large text), the "grouped." wordmark/logotype
- **Product usage:** D0 (96px) and D1 (40px) display hero moments — onboarding, pricing, celebration states. Max 2 instances per screen.
- Never use for: body copy, navigation, buttons, form labels, anything under 40px, H1-H5 headings (those stay Satoshi)
- Letter-spacing: -0.02em at large display sizes, +0.02em at character set sizes
- Line-height: 0.95 to 1.25 depending on size
- Key traits: rounded geometric, single-storey "a", pill-shaped terminals, monolinear strokes

**Display font stack (locked in):**
```css
font-family: 'Grouped Font', 'Satoshi', sans-serif;
```

**Display font rules:**
- 40px+ only — Grouped Font never appears below 40px
- Maximum 2 instances per screen (hero headline + maybe a section title)
- H1-H5 stay Satoshi — display font is for *moments*, headings are for *structure*
- No inline mixing — Grouped Font and Satoshi don't sit on the same line
- Product: D0 + D1 only — onboarding, pricing, celebration states
- Dark mode tested — verify against #111620 at both D0 and D1 sizes

### Satoshi (System Workhorse)
- Source: `https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap`
- Five weights: Light 300, Regular 400, Medium 500, Bold 700, Black 900
- Fallback stack: `'Satoshi', -apple-system, BlinkMacSystemFont, sans-serif`
- Used for: everything Grouped Font doesn't cover

### Monospace
- JetBrains Mono for code, data values, hex codes
- Source: `https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap`

### Type Scale

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


## Color

Three temperature layers. Deep blue surfaces create the room. Warm bronze marks the brand. Cool focus blue handles everything interactive.

### Bronze Accent Scale

| Step | Hex | Usage |
|---|---|---|
| 50 | `#FEF7EC` | Lightest tint |
| 100 | `#FDE9C8` | Light tint |
| 200 | `#FAD08E` | Medium tint |
| 300 | `#F6B44E` | Warm highlight |
| **400** | **`#C48A3A`** | **Primary brand accent** |
| 500 | `#B87A2E` | Darker accent |
| 600 | `#916024` | Deep accent |
| 700 | `#6B471B` | Darkest accent |
| 800 | `#4A3114` | Near-black warm |

Bronze 400 (`#C48A3A`) is reserved for headlines, logos, section labels, CTAs, and the concentric arc motif. It should never appear on interactive feedback elements like focus rings, stickers, or status badges.

### Background Surfaces (Dark Mode)

| Level | Hex | CSS Variable |
|---|---|---|
| Base | `#111620` | `--bg-base` |
| Raised | `#181E2A` | `--bg-raised` |
| Overlay | `#1F2735` | `--bg-overlay` |
| Subtle | `#262F3F` | `--bg-subtle` |
| Muted | `#2E3849` | `--bg-muted` |

Each level gains ~7 lightness points with a consistent blue undertone.

### Background Surfaces (Light Mode)

| Level | Hex | CSS Variable |
|---|---|---|
| Base | `#FAFAF8` | `--bg-base` |
| Raised | `#FFFFFF` | `--bg-raised` |
| Overlay | `#FFFFFF` | `--bg-overlay` |
| Subtle | `#F3F3F0` | `--bg-subtle` |
| Muted | `#EAEAE6` | `--bg-muted` |

### Text Hierarchy (Dark Mode)

| Level | Value | CSS Variable |
|---|---|---|
| Primary | `#F0EBE3` (100%) | `--text-primary` |
| Secondary | `rgba(240,235,227,0.6)` | `--text-secondary` |
| Tertiary | `rgba(240,235,227,0.38)` | `--text-tertiary` |
| Muted | `rgba(240,235,227,0.18)` | `--text-muted` |
| Inverse | `#111620` | `--text-inverse` |

### Text Hierarchy (Light Mode)

| Level | Value | CSS Variable |
|---|---|---|
| Primary | `#1A1A1A` (100%) | `--text-primary` |
| Secondary | `rgba(26,26,26,0.6)` | `--text-secondary` |
| Tertiary | `rgba(26,26,26,0.38)` | `--text-tertiary` |
| Muted | `rgba(26,26,26,0.15)` | `--text-muted` |
| Inverse | `#F0EBE3` | `--text-inverse` |

### Semantic Colors

| Name | Hex | CSS Variable | Usage |
|---|---|---|---|
| Success | `#4ADE80` | `--success` | Positive states, live campaigns |
| Warning | `#F0C543` | `--warning` | Drafts, caution states |
| Error | `#F07068` | `--error` | Paused, error states |
| Info | `#63B3ED` | `--info` | Scheduled, informational |

Warm vivid palette — saturated enough to pop at badge size on dark backgrounds, while keeping warm undertones that belong in the Grouped palette. Warning yellow (`#F0C543`, ~47° hue) is 12° clear of bronze (`#C48A3A`, ~35° hue).

### Focus Blue

| Hex | CSS Variable | Role |
|---|---|---|
| `#7CBBDF` | `--focus` | Interactive accent |

Used for input focus rings, accent stickers, active state indicators, highlighted data points, and badges. Pops against deep blue without reading as a warning the way bronze does at small sizes.

### Color Roles (The Rule)

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

### Borders (Dark Mode)

| State | Value | CSS Variable |
|---|---|---|
| Default | `rgba(235,225,210,0.07)` | `--border-default` |
| Hover | `rgba(235,225,210,0.11)` | `--border-hover` |
| Active | `rgba(235,225,210,0.16)` | `--border-active` |
| Strong | `rgba(235,225,210,0.22)` | `--border-strong` |

### Borders (Light Mode)

| State | Value | CSS Variable |
|---|---|---|
| Default | `rgba(26,26,26,0.08)` | `--border-default` |
| Hover | `rgba(26,26,26,0.12)` | `--border-hover` |
| Active | `rgba(26,26,26,0.16)` | `--border-active` |
| Strong | `rgba(26,26,26,0.24)` | `--border-strong` |


## Surfaces

Three surface types create depth, warmth, and presence.

### Solid
The walls and floor. Structural surfaces for cards, containers, nav backgrounds. The foundation everything else sits on.

```css
.surface-solid {
  background: var(--bg-raised);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sleeve); /* 4px */
}
```

### Glass
Frosted vinyl sleeve. Transparent, blurred, soft. For callouts, overlays, floating elements.

```css
.surface-glass {
  background: var(--glass-bg); /* rgba(17,22,32,0.75) dark / rgba(255,255,255,0.7) light */
  backdrop-filter: blur(24px) saturate(1.2);
  -webkit-backdrop-filter: blur(24px) saturate(1.2);
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-sleeve);
}
```

Glass-warm variant adds a bronze tint: `background: rgba(196,138,58,0.06)`

### Vinyl
The premium surface. Warm sheen, subtle gradient. For hero moments, featured content, things worth spotlighting.

```css
.surface-vinyl {
  background: linear-gradient(135deg, var(--bg-raised) 0%, rgba(196,138,58,0.06) 100%);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-sleeve);
}
```

### Stickers
Lightweight transparent labels. Like stickers on a record sleeve. Used for tags, status indicators, and metric callouts.

```css
.surface-sticker {
  padding: 5px 14px;
  border-radius: 9999px; /* --radius-label */
  background: rgba(240,235,227,0.04);
  border: 1px solid var(--border-default);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.02em;
}

/* Accent sticker (uses focus blue) */
.sticker-accent {
  background: rgba(124,187,223,0.08);
  border-color: rgba(124,187,223,0.15);
  color: var(--focus);
}
```


## Spacing

4px base unit. Every spatial value is a multiple of 4.

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


## Radius

Two families. Sleeves are near-square (structural containers). Labels are round (interactive/decorative).

| Token | Value | Usage |
|---|---|---|
| `--radius-sleeve` | 4px | Cards, containers, panels |
| `--radius-label` | 9999px | Buttons, stickers, badges, pills |
| `--radius-sm` | 6px | Small interactive elements |
| `--radius-md` | 10px | Inputs, dropdowns |
| `--radius-lg` | 4px | Cards (intentionally sharp) |
| `--radius-xl` | 4px | Large cards (intentionally sharp) |
| `--radius-full` | 9999px | Pills, toggles |

The radius system uses a vinyl sleeve / label sticker metaphor: sleeve edges are near-square (the container), labels on them are round (the decoration).


## Shadows

| Token | Value (Dark) |
|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.35)` |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.4)` |
| `--shadow-lg` | `0 8px 32px rgba(0,0,0,0.45)` |
| `--shadow-glow-gold` | `0 0 24px rgba(196,138,58,0.15)` |
| `--shadow-glow-soft` | `0 0 60px rgba(196,138,58,0.06)` |

Light mode shadows use lower opacity (`0.06`, `0.08`, `0.1`).


## Motion

Motion has mass. Elements enter with intention and settle with confidence.

| Token | Value | Character |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Fast out, used for entrances |
| `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Smooth both ways |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Overshoot and settle (playful) |
| `--ease-smooth` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Gentle, everyday transitions |

Default transition durations: 500ms or longer for page-level animations. 200ms for micro-interactions (hover, focus). Stagger children by 80-120ms for grouped entrances.

### Interaction Language
Every shape borrows from music: waveform strokes, volume dials, frequency curves. These show up in loading states, hover effects, and progress indicators.

- **Light elements:** Waveforms, flowing lines, frequency curves. Thin, luminous, alive. Progress bars that ripple. Loading states that pulse. Clean strokes, no gradients. Light on dark.
- **Solid elements:** Physical controls, volume dials, badge/patch treatments. Flat Swiss-minimal aesthetic with precise tick marks. Heavy, grounded, tactile.


## Logo Usage

### Logo Types
Three approved logo types, each in three color variants (9 total combinations):

| Type | Description | Use Case |
|------|-------------|----------|
| **Mark** | G icon only (concentric arcs) | Favicons, app icons, tight spaces. Min size: 24px |
| **Horizontal** | Mark + "Grouped" wordmark side by side | Nav bars, headers, footers, email signatures. Min width: 100px |
| **Stacked** | Mark above "Grouped" wordmark | Social profiles, splash screens, hero sections. Min height: 64px |

### Color Variants
| Variant | Color | Usage |
|---------|-------|-------|
| **Brand** | Bronze `#C48A3A` | Default. Primary variant on dark backgrounds |
| **Light** | Cream `#F0EBE3` | On dark backgrounds when bronze isn't appropriate |
| **Dark** | Charcoal `#1A1D26` | On light backgrounds (print, light-mode contexts) |

### Clear Space
Minimum clear space around any logo variant = 1× the height of the G mark. No other elements, text, or edges may intrude into this zone.

### Background Placement
- **Dark backgrounds (#111620):** Use Brand (bronze) or Light (cream)
- **Light backgrounds (#F5F3EF):** Use Dark (charcoal)
- **Bronze backgrounds:** Use Dark (charcoal)
- **Photography:** Ensure sufficient contrast; prefer the mark alone over lockups

### Logo Guidelines
**Do:**
- Always use logo files from the Figma source (GDS26R → Logos page, node 18:2)
- Maintain clear space of at least 1× the mark height
- Use the mark alone when space is tight
- Keep the wordmark in Grouped Font — never substitute Satoshi

**Don't:**
- Don't recreate or redraw the G mark — always use the vector source
- Don't rotate, skew, or apply perspective transforms
- Don't place the logo on busy or low-contrast backgrounds
- Don't change the stroke weight or arc proportions
- Don't use gradients, shadows, or effects on the mark
- Don't separate the dot from the "Grouped" wordmark
- Don't lock up the mark with taglines or other icons

### Source Files
All 9 logo variants are available as Figma components: [GDS26R → Logos](https://www.figma.com/design/wValDdxygSxILi49qBBgAW/GDS26R?node-id=18-2). Export as SVG for web, PNG @2x for print.


## Brand Elements

### Concentric Arcs
From the logo DNA. Heavy strokes (32-38px), tight gaps, 2.4-2.7:1 width-to-gap ratio. Used as background textures, section dividers, and brand identity markers. Always in bronze (`--bronze-400`).

### Badge/Patch Treatments
Pulled from 70s patch culture. Circular or rounded-square outlines with centered text. Used for trust badges, certifications, and brand seals. Clean strokes, no fills.

### Background Textures
Subtle grain overlay on surfaces. Every glass surface has a noise layer so no two feel identical. Grain uses `background-image` with a tiny noise PNG or SVG filter at very low opacity (0.03-0.06).


## Photography

Intimate, high-contrast, warm. Artists in their element.

**Color grading:** Deep blacks, warm highlights. Complement the bronze accent. Slightly desaturated to keep the palette cohesive. Think film stock, not phone camera.

**Subject matter:** All genres represented. Hip-hop producers, indie singer-songwriters, DJs, R&B vocalists, bands in rehearsal rooms. Varied, always authentic.

**Color temperature:** Warm shadows (shift toward bronze/amber), cool highlights (shift toward steel/blue). Matches the brand's warm-cool contrast.


## Product Tokens

### Campaign Status Badges

| Status | Color | CSS Variable | Background |
|---|---|---|---|
| Live | `#4ADE80` | `--success` | `rgba(74,222,128,0.12)` |
| Draft | `#F0C543` | `--warning` | `rgba(240,197,67,0.12)` |
| Scheduled | `#63B3ED` | `--info` | `rgba(99,179,237,0.12)` |
| Ended | `var(--text-tertiary)` | neutral | `var(--bg-overlay)` |
| Paused | `#F07068` | `--error` | `rgba(240,112,104,0.12)` |

All badges use `border-radius: 9999px` (pill shape) with a 1px border at 0.2 opacity of their color.

### Fan Engagement Tiers (5-Dot System)

| Tier | Filled Dots | Dot Color | Description |
|---|---|---|---|
| New | 0 of 5 | none | Just swapped. Email only. |
| Interested | 1 of 5 | `--focus` | Returned to feed. 2+ touchpoints. |
| Engaged | 3 of 5 | `--focus` | Multiple swaps. Group member. |
| Core Fan | 4 of 5 | `--focus` | High activity. Email + phone. Shares content. |
| Superfan | 5 of 5 | `--bronze-400` | Paid tier. Quest completions. Top of leaderboard. |

Dots are 6px circles, 4px gap. Fill left to right. Superfan earns bronze dots, connecting to the brand accent as a reward. This is the only place focus blue and bronze appear on the same component.

### Data Visualization Palette

| Order | Hex | Role |
|---|---|---|
| Series 1 | `#7CBBDF` | Primary data (focus blue) |
| Series 2 | `#C48A3A` | Comparison/benchmark (bronze) |
| Series 3 | `#4ADE80` | Success green |
| Series 4 | `#F07068` | Error coral |
| Series 5 | `#63B3ED` | Info sky |
| Series 6 | `#F0C543` | Warning yellow |

Single-metric charts always use focus blue.

### Subscription Tier Indicators

| Tier | Price | Visual | Color |
|---|---|---|---|
| Free | $0/mo | Single gray bar | `--text-tertiary` at 0.3 opacity |
| Starter | $7/mo | Single bar | `--focus` |
| Growth | $19/mo | Double bar | `--focus` |
| Pro | $39/mo | Single bar | `--bronze-400` (earned, premium) |


## Product Architecture

### Artist Dashboard (12 screens)
1. **Dashboard** - overview stats, recent activity, engagement chart
2. **Campaign Builder** - step-by-step swap creation (highest-impact screen)
3. **Campaign Detail** - live performance metrics per campaign
4. **Fan Directory** - searchable fan list with engagement dots
5. **Fan Profile** - individual engagement history
6. **Smart Feed Manager** - connected accounts, auto-population settings
7. **Email Composer** - credit-based builder with audience selector
8. **Analytics** - fan growth, campaign trends, conversion funnels
9. **Group Manager** - community settings
10. **Settings** - account, billing, CRM integrations
11. **Onboarding** - guided first-run experience
12. **Upgrade/Pricing** - tier comparison, feature gates

### Fan Experience (8 screens)
1. **Swap Page** - core conversion surface. Artist-branded, mobile-first. Email input, "Unlock Early Access" CTA, "Powered by grouped." footer
2. **Smart Feed** - auto-populated artist activity stream
3. **Group/Community** - fan-to-fan space
4. **Fan Pass** - iOS/Android wallet badge with push notifications
5. **Listening Party** - real-time synchronized listening
6. **Quest Board** - gamified engagement tasks
7. **Post-Swap Confirmation** - content unlock, feed invitation
8. **Fan Profile/Settings** - notification preferences, data controls

### Dashboard Sidebar Navigation
Icons in order: Dashboard, Campaigns, Swaps, Smart Feed, Groups, Fans, Email, Analytics, Settings. Top-right CTA: "+ New Campaign" button.

### Dashboard Stat Cards
Four key metrics at the top: Total Fans, Active This Week, Live Campaigns, Swap Rate. Each card shows the metric value with a trend indicator.


## Product Components

### Swap Card
Fan-facing conversion unit. Artist-branded with configurable gate type (email, phone, pre-save, follow). Appears on swap pages, embeds, shared links.

### Campaign Card
Artist dashboard view. Status badge (Live/Draft/Ended/Paused), key metrics (Views, Swaps, Rate), conversion progress bar. Used in campaigns list and dashboard.

### Fan Card/Row
Single fan in a list. Contact info, engagement level dots (5-dot system), source campaign. Used in fan directory, campaign detail, group member lists.

### Feed Item
Auto-populated Smart Feed entry. Pulls from connected accounts (Spotify, YouTube, socials). Zero artist effort. Triggers push notifications.

### Stat Card
Single KPI with trend indicator. Configurable for any metric. Used on dashboard and analytics screens.

### Email Composer
Credit-based email builder. Shows remaining credits (e.g. 47/200), audience selector, subject line, template body. Upsell prompt when credits run low.

### Empty State
First-run and zero-data states. Icon, message, primary action button. Should feel inviting, not empty. Each screen needs its own version.

### Toast/Notification
Transient feedback. Success, error, warning, info variants. Top-right positioned, auto-dismiss. Uses semantic colors with Phosphor Bold icons (check-circle, x-circle, warning, info).

### Modal / Dialog
Confirmation and destructive action dialogs. Centered overlay with scrim background. Title bar, body text, action buttons (secondary cancel + primary confirm). Destructive variant uses error-colored confirm button with trash icon.

### Dropdown / Select
Filter and sort controls. Trigger button with caret-down icon, open state shows option list with check icon on selected item. Bronze accent on active selection left-border. Used for audience, campaign, and date filters.

### Table / Data Grid
Sortable data tables for fan directory, campaign list, email history. Header row with sort indicator (caret-up-down), data rows with alternating background. Action menu (dots-three) per row.

### Chart Components
Line charts and donut charts for analytics views. Line charts use bronze stroke with gradient fill. Donut charts use status/data-viz color set (success, bronze, info). Pure CSS/SVG implementation.

### File Upload
Drag-and-drop zone with upload-simple icon. Dashed border at 2px, file type hint text. Uploaded state shows file name with image icon, file size, and x-to-remove. Used in campaign builder and settings.

### Progress Steps
Horizontal stepper for campaign builder, onboarding, multi-step flows. States: completed (green check-circle, success border), current (bronze number, bronze border), upcoming (muted number, default border). Connector lines match state colors.

### Tab Bar
Horizontal tabs using C4 component type (14px, Semibold 600). Active tab has bronze underline (2px bottom border) and primary text color. Inactive tabs use tertiary text. Keyboard accessible.

### Search / Filter Bar
Combined search input with magnifying-glass icon prefix and filter button with funnel icon. Active filters display as removable badge-accent pills with x-to-remove. Clear-all action in bronze text.

### Tooltip / Popover
Small floating card with arrow caret. Positioned relative to trigger element. Dark raised surface with border, 4-16px shadow. Title in primary weight, description in secondary color. Info icon as common trigger.


## Iconography

### Library: Phosphor Bold
Grouped uses **Phosphor Bold** as its icon library. The 2px strokes and rounded terminals match the Grouped logo's bold geometric character (2.5px strokes, `stroke-linecap="round"`).

CDN: `https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css`
Usage: `<i class="ph-bold ph-[name]"></i>`

### Size Scale

| Size | Token | Usage |
|---|---|---|
| 16px | Inline | Alongside body text, table cells, captions |
| 20px | Default | Navigation items, list icons, input prefixes |
| 24px | Buttons | Button icons, toolbar actions, card headers |
| 32px | Feature | Empty states, onboarding, feature highlights |

### Color Rules
- **Default**: Icons inherit text color from context (primary, secondary, tertiary)
- **Bronze accent**: `var(--bronze-400)` for featured, premium, or highlighted icons — use sparingly
- **Semantic**: Status icons (check-circle, warning, x-circle, info) use their semantic color token

### Product Icon Set
- **Navigation**: house, chart-line-up, users, envelope, gear, bell, swap, megaphone
- **Actions**: plus, pencil-simple, trash, magnifying-glass, funnel, download-simple, copy, share-network
- **Media**: music-notes, vinyl-record, microphone-stage, play, headphones, image, link, spotify-logo
- **Status**: check-circle (success), warning (warning), x-circle (error), info (info), spinner (loading), eye, lock, clock

### Guidelines
- ✓ Use Phosphor Bold consistently across all product surfaces
- ✓ Keep icons at one of the four standard sizes (16, 20, 24, 32px)
- ✓ Let icons inherit text color unless they carry semantic meaning
- ✓ Pair icons with text labels in navigation and primary actions
- ✕ Don't mix icon libraries (no Lucide, Feather, or Material alongside Phosphor)
- ✕ Don't use thin or light weights — they disappear on dark backgrounds
- ✕ Don't use icons as the only affordance for critical actions — always add a label or tooltip
- ✕ Don't apply custom stroke widths or fills — Phosphor Bold's 2px strokes are the standard


## Component States

### Button States
| State | Visual Change |
|---|---|
| Default | Bronze background, base text |
| Hover | Lighten 8%, add shadow `0 4px 12px rgba(196,138,58,0.25)` |
| Active | Darken 10%, `scale(0.97)` |
| Disabled | `opacity: 0.4`, no cursor |
| Loading | Spinner icon replaces label text |

### Input States
| State | Visual Change |
|---|---|
| Empty | Placeholder text in tertiary color |
| Focused | Bronze border, focus ring `0 0 0 3px rgba(196,138,58,0.12)` |
| Filled | Primary text color, default border |
| Error | Error-colored border, error message below, subtle error background |
| Disabled | `opacity: 0.4`, no interaction |

### Card States
| State | Visual Change |
|---|---|
| Default | Raised background, default border |
| Hover | Lift -2px (`translateY(-2px)`), border-hover, shadow |
| Selected | Bronze border, focus ring |

### Toggle States
- **Off**: Default track background, thumb at left
- **On**: Bronze track background, thumb at right
- **Disabled**: `opacity: 0.4`, no pointer events

### Transition Specs
- Hover: `transition: all 0.2s ease; transform: translateY(-2px);`
- Active: `transition: all 0.1s ease; transform: scale(0.97);`
- Focus ring: `box-shadow: 0 0 0 3px rgba(196,138,58,0.12); border-color: var(--bronze-400);`


## Responsive Breakpoints

| Breakpoint | Range | Context |
|---|---|---|
| Mobile | 0 — 639px | Fan-facing swap pages, mobile web app, single column |
| Tablet | 640 — 1023px | Two columns, sidebar collapses to hamburger |
| Desktop | 1024 — 1439px | Primary dashboard, sidebar visible, full tables |
| Wide | 1440px+ | Max container 1280px, extra margins |

### Touch Targets
- **44px minimum**: Primary actions (buttons, nav items, CTAs)
- **36px minimum**: Secondary actions (icon buttons, table rows, filter chips)

### Responsive Adjustments
- **Type**: D0 caps at 48px on mobile (from 96px), D1 caps at 28px, body stays 14px
- **Spacing**: Reduce to 75% of desktop values on mobile for space-8 and above
- **Layout**: Sidebar collapses at 1024px, card grids go 1-col at 640px, tables scroll horizontally


## Grid & Layout System

### Grid Specs
- **Columns**: 12
- **Desktop gutter**: 24px (`var(--space-6)`)
- **Mobile gutter**: 16px (`var(--space-4)`)
- **Max container**: 1280px

### Layout Patterns
- **Sidebar + Main**: Dashboard, campaigns, fan directory (sidebar ~220px, main content fills remaining)
- **Full Width**: Swap pages, embeds, shared links (no sidebar, content fills viewport)
- **Centered Narrow**: Auth, onboarding, settings (max-width 480px, centered)

### CSS
```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}
@media (max-width: 639px) {
  .grid { gap: var(--space-4); }
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


## Product Patterns

### The Conversion Funnel
Views > Swaps > Fans > Engaged > Revenue. Proportional-width bars showing progression and drop-off. Consistent treatment across dashboard, campaign detail, and analytics.

### Feature Gates (Upgrade Prompts)
Inline, subtle. Should feel like an invitation, not a wall. Background uses `rgba(196,138,58,0.04)` with a bronze border at 0.12 opacity. Text explains the feature, link says "Upgrade to [Tier] >"

### Validation Moments
Celebration states for key milestones: new fan captured, campaign milestone hit, first paid subscriber, email credit earned. Sound + motion + visual that makes artists feel their progress.

### Artist Theming (Fan-Facing)
Fan-facing surfaces adapt to the artist's brand. Configurable accent color, avatar, cover image. Grouped provides structure, artist identity fills it. Pro tier removes Grouped branding.

### Between-Release Engagement
Every screen needs a nudge toward the next action: send an email, check fan analytics, update Smart Feed, post in Group. The dashboard should never feel "done."

### CRM Sync Status
Consistent indicator across settings, fan directory, and campaign detail. States: connected (success), syncing (info), error (error), last synced timestamp.


## Product Overrides (Rebrand Tokens — GDS26R)

This section documents where the product UI intentionally diverges from the marketing/brand design system. These overrides were audited against the Figma GDS26R rebrand token file.

### Alignment Summary

| Category | Status | Notes |
|---|---|---|
| Base background (#111620) | Aligned | Same across marketing + product |
| Dark mode default | Aligned | Both systems treat dark as primary |
| Primary text color (#F0EBE3) | Aligned | Figma needs update from #f8f8f8 |
| Warm cream base | Aligned | Consistent across all surfaces |
| Bronze accent (#C48A3A) | Aligned | Same token |
| Focus blue (#7CBBDF) | Aligned | Same token |
| Body font (Satoshi) | Override | Figma currently shows Inter (placeholder) — needs swap |
| Body default size | Override | Product uses 14px for density; marketing stays 16px |
| Bold weight for components (700) | Override | Satoshi has no 600; all Semibold remapped to 700 Bold |
| Pill buttons (9999px) | Override | Product commits to full-round interactive elements |
| Component type scale (C1–C7) | Override | New category for product UI elements |
| Display max size (96px D0) | Override | Product hero needs larger than marketing's 80px |
| Display title typeface | Aligned | Grouped Font at D0/D1 in product, Satoshi fallback — locked in |
| Text color (#f8f8f8 vs #F0EBE3) | Aligned | Warm cream #F0EBE3 chosen — Figma needs update from #f8f8f8 |
| Warning/bronze proximity | Aligned | #F0C543 at ~47° hue, 12° clear of bronze — locked in |
| Status color saturation | Aligned | Warm vivid set (#4ADE80, #F0C543, #F07068, #63B3ED) — locked in |

### Product Type Scale

Product uses five type categories rendered in Satoshi (target state).

**Display (D0–D6):**

| Token | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---|---|---|---|---|---|
| D0 | 96px | 700 Bold | 116px | -4% | Display Hero |
| D1 | 40px | 700 Bold | 48px | -3% | Display XXL |
| D2 | 36px | 400 Regular | 48px | -1% | Display XL (data viz) |
| D3 | 28px | 400 Regular | 36px | -1% | Display L |
| D4 | 24px | 500 Medium | 32px | 0% | Display M |
| D5 | 18px | 500 Medium | 24px | -0.5% | Display S (subtitles) |
| D6 | 14px | 500 Medium | 20px | 0.5% | Display XS |

**Heading (H1–H5):**

| Token | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---|---|---|---|---|---|
| H1 | 36px | 700 Bold | 44px | -2% | Page titles |
| H2 | 28px | 700 Bold | 36px | -1% | Section titles |
| H3 | 24px | 700 Bold | 32px | 0% | Medium titles |
| H4 | 18px | 700 Bold | 28px | 0% | Small titles |
| H5 | 16px | 700 Bold | 24px | 0% | Smallest titles |

**Body:**

| Token | Size | Weight | Line-Height | Letter-Spacing |
|---|---|---|---|---|
| Body Default | 14px | 400 Regular | 20px | 0% |
| Body Emphasized | 14px | 700 Bold | 20px | 0% |

**Caption:**

| Token | Size | Weight | Line-Height | Letter-Spacing |
|---|---|---|---|---|
| Caption | 12px | 500 Medium | 20px | 1% |
| Caption Emphasized | 12px | 700 Bold | 20px | 0.5% |

**Component (C1–C7) — product-only category:**

| Token | Size | Weight | Line-Height | Letter-Spacing | Usage |
|---|---|---|---|---|---|
| C1 | 20px | 700 Bold | 24px | 0% | Large buttons |
| C2 | 18px | 700 Bold | 24px | 0% | Buttons |
| C3 | 16px | 700 Bold | 20px | 0% | Buttons |
| C4 | 14px | 700 Bold | 16px | 0.5% | Navigation |
| C5 | 14px | 500 Medium | 16px | 0.5% | Navigation (light) |
| C6 | 11px | 500 Medium | 16px | 0.5% | Badges |
| C7 | 9px | 500 Medium | 12px | 1% | Smallest badges |

### Product-Specific Radius

| Token | Value | Usage |
|---|---|---|
| Sleeve | 4px | Structural containers, cards |
| Small | 6px | Small interactive elements |
| Input | 10px | Inputs, medium containers |
| Pill | 9999px | Buttons, badges, tabs (product default) |

### Status Colors — Warm Vivid (Locked In)

Three approaches were compared: original desaturated set (too muted at badge size), Tailwind stock (too cold/digital for the warm palette), and **warm vivid** (selected). The warm vivid set boosts saturation while preserving the warm character of the Grouped palette.

| Status | Old | **New (Active)** | Rationale |
|---|---|---|---|
| Success | `#8BAF9C` | **`#4ADE80`** | Bright warm green, clearly reads "live" at badge size |
| Warning | `#D4A24B` | **`#F0C543`** | Bright yellow at ~47° hue — 12° clear of bronze (~35°) |
| Error | `#C27A6B` | **`#F07068`** | Warm coral-red, still carries warmth |
| Info | `#8BA4BE` | **`#63B3ED`** | Warm sky blue, friendlier than cobalt |

### Warning/Bronze Proximity — Resolved

Warning `#F0C543` sits at ~47° hue, 12° clear of bronze `#C48A3A` (~35°), with significantly higher lightness. Bronze is "warm amber/gold" (brand voice), warning is "bright yellow" (functional status signal) — impossible to confuse.

- Hue gap: 12° (was 4° with old `#D4A24B`)
- Lightness gap: 18% (was 6%)


## CSS Variables Quick Reference

```css
:root {
  /* Backgrounds */
  --bg-base: #111620;
  --bg-raised: #181E2A;
  --bg-overlay: #1F2735;
  --bg-subtle: #262F3F;
  --bg-muted: #2E3849;

  /* Borders */
  --border-default: rgba(235,225,210,0.07);
  --border-hover: rgba(235,225,210,0.11);
  --border-active: rgba(235,225,210,0.16);
  --border-strong: rgba(235,225,210,0.22);

  /* Text */
  --text-primary: #F0EBE3;
  --text-secondary: rgba(240,235,227,0.6);
  --text-tertiary: rgba(240,235,227,0.38);
  --text-muted: rgba(240,235,227,0.18);
  --text-inverse: #111620;

  /* Brand */
  --bronze-400: #C48A3A;
  --focus: #7CBBDF;

  /* Gold Scale */
  --gold-50: #FEF7EC;
  --gold-100: #FDE9C8;
  --gold-200: #FAD08E;
  --gold-300: #F6B44E;
  --gold-500: #B87A2E;
  --gold-600: #916024;
  --gold-700: #6B471B;
  --gold-800: #4A3114;

  /* Semantic — Warm Vivid */
  --success: #4ADE80;
  --warning: #F0C543;  /* 12° hue clear of bronze #C48A3A */
  --error: #F07068;
  --info: #63B3ED;

  /* Glass */
  --glass-bg: rgba(17,22,32,0.75);
  --glass-border: rgba(235,225,210,0.06);

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.35);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.45);
  --shadow-glow-gold: 0 0 24px rgba(196,138,58,0.15);
  --shadow-glow-soft: 0 0 60px rgba(196,138,58,0.06);

  /* Motion */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);

  /* Radius */
  --radius-sleeve: 4px;
  --radius-label: 9999px;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 4px;
  --radius-xl: 4px;
  --radius-full: 9999px;
}
```


## Selection Color

```css
::selection {
  background: rgba(196,138,58,0.3);
  color: var(--text-primary);
}
```
