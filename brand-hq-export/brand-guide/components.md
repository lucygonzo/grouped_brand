---
section: components
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Components

Every component shares the same physical DNA. Cards have weight and surface texture. Buttons depress when you press them. Inputs have depth. Rounded corners echo the cyclical nature of the release cycle: write, record, release, connect, repeat. Nothing is sharp because nothing in this experience should feel like it ends.


## Buttons

Five button types: three core levels (Primary, Secondary, Tertiary) plus Link and Destructive. All use pill radius (`--radius-full: 39px`), Satoshi Bold uppercase labels, and three size tiers.

### Shared Sizing

| Size | Height | Padding | Font Size |
|---|---|---|---|
| Small (`btn-sm`) | 36px | 8px 20px | 13px |
| Medium (`btn-md`, default) | 44px | 12px 28px | 14px |
| Large (`btn-lg`) | 52px | 16px 36px | 16px |

All buttons use `--radius-full` (39px) pill radius. Active (press) state on all buttons: `scale(0.97)`.

### Primary

Hero action. One per screen. Solid bronze fill with inverse text. Use for the single most important action: Save, Submit, Confirm.

| Property | Value |
|---|---|
| Fill | `--bronze-400` (`#C48A3A`) |
| Text | `--button-text` (`#111620`) |
| Hover | Subtle transparent-white overlay (~8% opacity) on bronze fill |
| Active | `scale(0.97)` |
| Disabled | `opacity: 0.4` |
| Loading | Spinner replaces label text, fill stays |
| CSS class | `.btn.btn-primary` |

### Secondary

Supporting action and fan-facing engagement. Bronze outline, transparent fill.

| Property | Value |
|---|---|
| Fill | `transparent` |
| Border | `1.5px solid --bronze-400` |
| Text | `--bronze-400` |
| Hover | Subtle bronze wash + glow |
| Active | Deeper wash + `scale(0.97)` |
| CSS class | `.btn.btn-secondary` |

### Tertiary

Minimal treatment -- no fill, no border at rest. Two variants:

**Text variant** -- for inline navigation (View Details, Learn More, See All):

| Property | Value |
|---|---|
| Fill | `transparent` |
| Text | `--bronze-400` |
| Hover text | `--gold-300` |
| CSS class | `.btn.btn-tertiary` |

**Icon-only variant (Ghost)** -- for utility actions (Like, Menu, Settings, Close):

| Property | Value |
|---|---|
| Fill | `transparent` |
| Icon color | `--text-secondary` |
| Hover | Ghost fill appears |
| Sizes | sm 36px, md 44px (default), lg 52px (square hit target) |
| CSS class | `.btn.btn-ghost` |

### Link / URL

Monospace URL display with copy action.

| Property | Value |
|---|---|
| Fill | `--bg-raised` |
| Border | `1px solid --border-default` |
| Font | JetBrains Mono 12px / 500 |
| Hover | `--border-hover` + `--text-primary` |
| CSS class | `.btn.btn-link` |

### Destructive

Irreversible danger action.

| Property | Value |
|---|---|
| Fill | `--error` (`#F07068`) |
| Text | `#FFFFFF` |
| Hover | `#D85A52` + red shadow |
| Active | `#C04840` + `scale(0.97)` |
| CSS class | `.btn.btn-destructive` |

### Button Selection Guide

**Do:**
- One Primary per screen -- it's the hero action
- Use Secondary for all supporting actions (Edit, Share, Unlock, Claim)
- Use Destructive only for irreversible actions (delete, remove)
- Use Tertiary for inline text links and icon-only utility actions

**Don't:**
- Don't stack two Primary buttons -- demote one to Secondary
- Don't use a neutral/white outline -- Secondary is always bronze
- Don't use Destructive for cancel or dismiss -- use Secondary
- Don't mix button sizes in the same row

### When to Use Each Size

| Size | Context |
|---|---|
| sm (36px) | Inline actions, table rows, compact card footers |
| md (44px) | Standard forms, dialogs, cards -- the default choice |
| lg (52px) | Hero actions, onboarding flows, landing pages |

### Focus Ring Behavior on Buttons

All interactive elements use the same global focus ring: `2px solid var(--focus)` at `outline-offset: 2px`. No per-component overrides. The secondary button is the only case where two outlines coexist (bronze border + blue ring). This is intentional and only visible during keyboard navigation.


## Inputs

| Property | Value |
|---|---|
| Background | `--bg-overlay` |
| Border | `1px solid --border-input` |
| Border (focus) | `--bronze-400` |
| Text | `--text-primary` |
| Placeholder | `--text-tertiary` |
| Label | 12px, `--text-secondary`, uppercase |
| Helper text | 12px, `--text-tertiary` |
| Error border | `--error` |
| Error helper | `--error` |
| CSS class | `.input-field` |


## Badges & Tags

| Variant | CSS Class | Color |
|---|---|---|
| Default | `.badge` | Neutral border |
| Accent | `.badge.badge-accent` | Focus blue |
| Success | `.badge.badge-success` | `--success` (`#4ADE80`) |
| Info | `.badge.badge-info` | `--info` (`#63B3ED`) |
| Warning | `.badge.badge-warning` | `--warning` (`#F0C543`) |
| Error | `.badge.badge-error` | `--error` (`#F07068`) |


## Toggles

| State | Track | Thumb |
|---|---|---|
| Off | `--deco-ghost` bg, `--deco-subtle` border | `--bg-subtle` fill, `--deco-subtle` border, left-aligned |
| On | `rgba(196,138,58,0.15)` bg, `rgba(196,138,58,0.2)` border | `--bronze-400` solid fill, right-aligned |

Track size: 52px wide x 28px tall. Thumb: 20px circle. CSS class: `.toggle-track`, `.toggle-thumb`.


## Navigation Preview

| Element | Spec |
|---|---|
| Default text | `#A09B93` (warm mid-gray from cream palette) |
| Selected icon | `--bronze-400`, background steps up one surface layer |
| Hover | Opacity-based lightening on border and fill |
| Logo | "grouped" in Anacrusis, dot in `--bronze-400` |


## Core Product Components

17 product components are fully specced with interactive states:

| # | Component | Use On |
|---|---|---|
| 1 | Swap Card | Artist profile, campaign detail, shared links, embeds |
| 2 | Campaign Card | Artist dashboard, campaigns list, campaign detail header |
| 3 | Fan Card / Row | Fan directory, campaign detail, group member lists |
| 4 | Feed Item | Fan-facing activity feed, push notification content |
| 5 | Stat Card | Dashboard KPIs, analytics overview, campaign detail stats |
| 6 | Email Composer | Email campaigns, fan messaging, announcement broadcasts |
| 7 | Empty State | Every screen's zero-data state |
| 8 | Toast / Notification | All transient feedback (success, error, warning, info) |
| 9 | Modal / Dialog | Confirmations, destructive actions, focused input flows |
| 10 | Dropdown / Select | Filters, sort controls, audience selectors, settings |
| 11 | Table / Data Grid | Fan directory, campaign list, email history, admin views |
| 12 | Chart Components | Analytics dashboard, campaign performance, fan growth |
| 13 | File Upload | Campaign builder, profile settings, media uploads |
| 14 | Progress Steps | Campaign builder, onboarding, multi-step flows |
| 15 | Tab Bar | Campaign detail sub-views, analytics, settings panels |
| 16 | Search / Filter Bar | Fan directory, campaign listing, any list with 10+ items |
| 17 | Tooltip / Popover | Metric explanations, feature hints, onboarding tips |

### Toast / Notification Variants

| Variant | Background | Border | Icon |
|---|---|---|---|
| Success | `rgba(74,222,128,0.06)` | `rgba(74,222,128,0.15)` | `ph-check-circle` in `--success` |
| Error | `rgba(240,112,104,0.06)` | `rgba(240,112,104,0.15)` | `ph-x-circle` in `--error` |
| Warning | `rgba(240,197,67,0.06)` | `rgba(240,197,67,0.15)` | `ph-warning` in `--warning` |
| Info | `rgba(99,179,237,0.06)` | `rgba(99,179,237,0.15)` | `ph-info` in `--info` |


## Common Recipes

### "I need a primary CTA button"
```css
.btn-primary {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: 'Satoshi', sans-serif; font-weight: 700; font-size: 14px;
  letter-spacing: 0.02em; text-transform: uppercase;
  padding: 12px 28px; height: 44px;
  border-radius: var(--radius-full); /* 39px pill */
  background: var(--bronze-400); color: var(--T5);
  border: none; cursor: pointer;
}
.btn-primary:hover { background: var(--gold-500); transform: scale(1.02); }
.btn-primary:active { background: var(--gold-600); transform: scale(0.98); }
.btn-primary:focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(124,187,223,0.2);
}
```

### "I need a form input"
```css
.input-field {
  width: 100%; height: 44px; padding: 12px 16px;
  font-family: 'Satoshi', sans-serif; font-size: 14px;
  color: var(--T1); background: var(--L4); /* --bg-muted */
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md); /* 16px */
}
.input-field:focus {
  border-color: var(--focus);
  box-shadow: 0 0 0 3px rgba(124,187,223,0.15);
}
.input-field.error {
  border-color: var(--error);
  box-shadow: 0 0 0 3px rgba(240,112,104,0.12);
}
```

### "I need a badge"
```css
.badge {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 4px 12px; height: 28px;
  border-radius: var(--radius-full);
  font-size: 12px; font-weight: 500; letter-spacing: 0.02em;
}
/* Default: */ background: rgba(255,255,255,0.06); border: 1px solid var(--border-default); color: var(--T2);
/* Accent: */ background: rgba(124,187,223,0.1); border-color: rgba(124,187,223,0.2); color: var(--focus);
```


## Never Do This

| Rule | Why |
|---|---|
| Never use sharp corners on buttons | All buttons are pill-shaped (`--radius-full`). Rounded = cyclical = brand. |
| Never use bronze for destructive actions | Destructive = `--error` red. Bronze implies positive/brand. |
| Never make touch targets smaller than 36px | 44px primary, 36px secondary. Accessibility requirement. |
| Never skip the focus ring on interactive elements | `--focus` blue + 2px outline + 2px offset. Non-negotiable for a11y. |
| Never use loading spinners in bronze | Loading spinner inherits from parent button color. Bronze spinner on bronze button = invisible. |
| Never put icons in buttons without text unless using Ghost variant | Icon-only buttons must use `.btn-ghost` pattern (square, transparent). |


## Cross-Surface Translation

| Surface | How Components Show Up |
|---|---|
| **Product (app)** | Full component library with production tokens, dark mode default |
| **Marketing site** | Marketing-specific button showcase (M3), visual language demos only |
| **Mobile** | Same components, touch targets enforced (44px primary, 36px secondary) |
| **Print** | N/A -- components are digital-only |
| **Events/experiential** | Kiosk UIs reuse product components in full-screen mode |
| **Social** | Static renders of key components for product marketing posts |
| **Email** | Simplified button styles (HTML email constraints), badge-style CTAs |
| **Investor materials** | Component screenshots for product demo slides |
