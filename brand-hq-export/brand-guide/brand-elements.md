---
section: brand-elements
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Brand Elements & Textures

These are the graphic elements that make Grouped feel like Grouped. Concentric arcs from the logo DNA. Physical controls borrowed from studio hardware. Badge treatments pulled from 70s patch culture. Every element reinforces the tactile philosophy: this is something you can almost reach out and touch.


## Concentric Arcs -- The Signature Motif

Sound waves radiating from a source. Vinyl grooves. Ripples. The concentric arc is the single most recognizable Grouped graphic element. Heavy strokes with tight gaps between them.

### Arc Rule

**Heavy strokes. Tight gaps.** Stroke width is always larger than the gap between arcs (roughly **2.5:1 ratio**). Every ring in a set uses the same weight and color. No opacity variation between individual strokes. When used as background, reduce the **group** opacity, not individual rings.

### Arc Variants

| Variant | Description | Use For |
|---|---|---|
| **Full Rings** | Concentric circles, centered | Background textures, section dividers |
| **Corner Arcs** | Quarter-arc radiating from a corner | Poster layouts, hero sections |
| **G Monogram** | Open concentric arcs with crossbar (the Vinyl G) | Logo mark, watermarks |

### Arc Specifications

| Property | Value |
|---|---|
| Stroke-to-gap ratio | ~2.5:1 (e.g., stroke 32px, gap 12px) |
| Stroke color | `--deco-strong` (neutral) or `--bronze-400` (brand) |
| Ring consistency | All rings in a set use identical weight and color |
| Opacity rule | Reduce group opacity, never per-ring opacity |
| Rendering | SVG paths with `stroke-linecap="round"` |


## Physical Controls

Controls borrowed from studio hardware, stripped to their structural essence. No gradients, no metallic effects, no embossing. The shape itself communicates the function.

### Hardware Rule

**Controls are flat and structural.** No gradients on controls themselves. No metallic effects. No embossing. Shapes communicate function: circles rotate, rectangles slide, pills toggle. The only warmth comes from bronze as the active/indicator color. Think Swiss International Style applied to studio equipment: the grid does the work, not decoration.

### Control Types

| Control | Shape Language | Active Indicator |
|---|---|---|
| **Volume Dial** | Circle with flat fill. Indicator line from center. Thin circle track. | Active arc in `--bronze-400` (opacity 0.4) shows current value |
| **Mixing Fader** | Vertical thin track (2px). Flat rectangular handle with grip lines. | Active fill in `--bronze-400` (opacity 0.4) from bottom to handle position |
| **Power Toggle** | Pill track (52x28px). Circle thumb. | Off: `--deco-ghost` track, `--bg-subtle` thumb. On: bronze-tinted track, solid `--bronze-400` thumb |

### Control Specs

| Property | Value |
|---|---|
| Track stroke | 2px, `--deco-subtle` |
| Tick marks (major) | `--deco-medium`, 1.5px |
| Tick marks (minor) | `--deco-faint`, 1px |
| Knob/handle fill | `--bg-overlay` or `--bg-subtle` |
| Knob border | 1px `--deco-faint` |
| Active color | `--bronze-400` at 0.4-0.7 opacity |
| Center dot | 4px radius, `--deco-medium` |


## Badge & Patch Treatments

Concentric rounded borders in the brand palette create a retro badge feel. Use for special moments: launch announcements, year-in-review, limited drops, artist features. These are the stickers you'd iron onto a denim jacket.

### Badge Styles

| Style | Description | Use For |
|---|---|---|
| **Bronze Monochrome** | Single bronze border with offset shadow ring | Timeless, formal moments (EST. 2026) |
| **Multi-Color** | Layered concentric borders (bronze + secondary + blue-gray) | Celebratory, year markers, milestones |
| **Circle Badge** | Round with concentric inner ring | Membership indicators, achievement badges |

### Badge Specs

| Property | Value |
|---|---|
| Primary border | 3-4px solid `--bronze-400` |
| Outer shadow ring | `box-shadow: 0 0 0 8px var(--bg-raised), 0 0 0 11px rgba(196,138,58,0.3)` |
| Multi-ring inner | `box-shadow` layered: bronze, spacer, blue-gray |
| Border radius | `--radius-md` (rectangular) or 50% (circular) |
| Inner ring | 1px `rgba(196,138,58,0.15)` |
| Typography | Anacrusis for brand name, system for labels |


## Background Textures

The concentric arc pattern at large scale. For subtle use, keep every stroke at full opacity and reduce the opacity of the entire SVG group. For bold use, place solid arcs on a bronze or colored field. The strokes are always the same weight with equal spacing. Scale the group, not individual rings.

### Texture Variants

| Variant | Description | Specs |
|---|---|---|
| **Subtle** | Heavy strokes, low group opacity on dark surface | Stroke: `--text-primary`, stroke-width 38px, group opacity ~0.07 |
| **Bold** | Solid arcs on bronze/colored field | Stroke: `rgba(0,0,0,0.12)`, stroke-width 38px on `--bronze-400` background |

### Texture Rules

- Strokes are always the same weight with equal spacing
- Scale the entire group, not individual rings
- Subtle variant: group opacity 0.05-0.10
- Bold variant: arcs in darker tone of the background color
- Corner placement preferred (top-right or bottom-left origin)


## Element Combinations

The real power of these elements comes from layering them:

1. **Arcs as background** -- subtle opacity, corner placement
2. **Glass cards on top** -- `--glass-bg` with `--glass-border`
3. **Physical controls inside** -- flat, structural, bronze active states
4. **Badge treatments for special moments** -- celebratory overlays


## Cross-Surface Translation

| Surface | How Brand Elements Show Up |
|---|---|
| **Product (app)** | Subtle arc textures on empty states and onboarding. Toggle/fader controls for settings. |
| **Marketing site** | Full arc treatments on hero sections, corner arcs on feature cards, badge lockups for milestones |
| **Mobile** | Simplified arcs (fewer rings) for performance. Badge treatments at smaller scale. |
| **Print** | Arc motif as section dividers and background texture. Badge treatments for business cards, packaging. |
| **Events/experiential** | Large-scale arc projections on stage backdrops. Physical badge/patch merch. Volume dial as wayfinding. |
| **Social** | Corner arc overlays on post templates. Badge lockups for announcements and milestones. |
| **Email** | Subtle arc as header background (static PNG). Badge treatment for special announcement headers. |
| **Investor materials** | Corner arcs on slide backgrounds. Monochrome badge for title slides. |
