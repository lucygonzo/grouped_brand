---
section: accessibility
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial framework created from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Accessibility

Grouped targets **WCAG 2.1 AA** compliance across all product surfaces. This section defines the baseline requirements and documents known gaps to audit.

> **Status:** This is a starter framework. Many sections need testing and validation against live implementations. Items marked "To be audited" require measurement before they can be confirmed.


## Target Standard

| Standard | Level | Status |
|---|---|---|
| WCAG 2.1 | AA | Target for all product surfaces |
| WCAG 2.1 | AAA | Aspirational for text contrast |


## Text Contrast Requirements

Contrast ratios are measured against the default dark mode surface L0 (`#111620`).

### Dark Mode

| Token | Hex | Role | Min Ratio Required | Status |
|---|---|---|---|---|
| `--T1` | `#F0EBE3` | Body copy, headings | 4.5:1 (normal) / 3:1 (large) | To be audited |
| `--T2` | `#67686B` | Supporting text | 4.5:1 (normal) | To be audited |
| `--T3` | `#494B50` | Captions, metadata | 3:1 (large text only, or UI components) | To be audited |
| `--T4` | `#2E3238` | Decorative only | N/A -- decorative, not informational | Exempt |
| `--T5` | `#111620` | Text on light/accent fills | 4.5:1 against fill color | To be audited |

### Light Mode

| Token | Hex | Role | Min Ratio Required | Status |
|---|---|---|---|---|
| `--T1` | `#111620` | Body copy, headings | 4.5:1 (normal) / 3:1 (large) | To be audited |
| `--T2` | `#535862` | Supporting text | 4.5:1 (normal) | To be audited |
| `--T3` | `#7C7E85` | Captions, metadata | 3:1 (large text only) | To be audited |
| `--T4` | `#ABABAF` | Decorative only | N/A -- decorative | Exempt |
| `--T5` | `#FFFFFF` | Text on dark/accent fills | 4.5:1 against fill color | To be audited |

### Bronze on Surfaces

| Combination | Bronze Hex | Surface Hex | Status |
|---|---|---|---|
| Bronze on L0 (dark) | `#C48A3A` | `#111620` | To be audited |
| Bronze on L1 (dark) | `#C48A3A` | `#181E2A` | To be audited |
| Bronze (light) on L0 (light) | `#956A1D` | `#FAFAF8` | To be audited |


## Touch Targets

Per WCAG 2.5.5 (Target Size) and WCAG 2.5.8 (Target Size Minimum):

| Level | Minimum Size | Usage |
|---|---|---|
| **Primary** | 44 x 44px | Buttons, nav items, primary action areas |
| **Secondary** | 36 x 36px | Icon buttons, table rows, filter chips |

- All interactive elements must meet these minimums
- Padding can extend the touch target beyond the visible element
- Adjacent targets must have sufficient spacing to prevent mis-taps


## Focus Ring Specifications

All interactive elements use a consistent global focus ring:

| Property | Value |
|---|---|
| Outline | `2px solid var(--focus)` |
| Offset | `outline-offset: 2px` |
| Focus color (dark) | `#7CBBDF` |
| Focus color (light) | `#2874A6` |
| Scope | All focusable elements -- no per-component overrides |

### Focus Ring + Bronze Borders

The secondary button is the only case where two outlines coexist (bronze border + blue focus ring). This is intentional: bronze says "branded action," blue says "keyboard is here." Do not swap the button border to blue on focus.

```css
/* Global focus ring */
:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
```


## Reduced Motion Support

Respect the `prefers-reduced-motion` media query:

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

- All motion tokens (easing curves, durations) should be bypassed when reduced motion is preferred
- Marketing scroll-driven animations must degrade to static reveals
- Spring easings should fall back to instant state changes
- Loading spinners may continue animating (functional, not decorative)


## Known Gaps to Audit

| Area | Issue | Priority |
|---|---|---|
| **Badge saturation** | Semantic badge colors (success, warning, error, info) may not meet contrast requirements against dark surfaces at small text sizes | High |
| **Color-blind data viz** | Data visualization palette (`--dataviz-blue`, `--dataviz-green`, `--dataviz-yellow`, `--dataviz-orange`) needs testing for deuteranopia and protanopia distinguishability | High |
| **T2/T3 contrast** | `--T2` (`#67686B`) and `--T3` (`#494B50`) on dark surfaces may fall below 4.5:1 for normal text | Medium |
| **Bronze small text** | `--bronze-400` (`#C48A3A`) used at 12px or smaller on dark surfaces | Medium |
| **OLED mode contrast** | OLED true-black surfaces may create different contrast ratios than navy dark mode | Medium |
| **Icon-only buttons** | Ghost buttons with no text label need `aria-label` audit | High |
| **Toast auto-dismiss** | Timed toasts must remain visible long enough for screen reader announcement | Medium |
| **Modal focus trap** | Dialogs need focus trap and Escape key dismissal verification | High |
| **Table keyboard nav** | Data grid needs arrow key navigation and screen reader row/column announcement | Medium |


## Semantic HTML Requirements

- Use `<button>` for interactive controls, not `<div>` with click handlers
- Use `<a>` for navigation, `<button>` for actions
- All images need meaningful `alt` text (or `alt=""` for decorative)
- Form inputs need associated `<label>` elements
- Modals need `role="dialog"` and `aria-modal="true"`
- Toast notifications need `role="alert"` or `aria-live="polite"`


## Cross-Surface Translation

| Surface | Accessibility Requirements |
|---|---|
| **Product (app)** | Full WCAG AA compliance. Keyboard navigation, focus management, screen reader support. |
| **Marketing site** | WCAG AA for all interactive elements. Reduced motion support. Alt text on all imagery. |
| **Mobile** | Touch target enforcement (44px). VoiceOver/TalkBack compatibility. |
| **Print** | Sufficient color contrast for text legibility. Avoid color-only information encoding. |
| **Events/experiential** | Large text sizes for readability at distance. Audio descriptions for visual displays. |
| **Social** | Alt text on all posted images. Captions on all video content. |
| **Email** | Semantic HTML structure. Alt text on images. Plain-text fallback. |
| **Investor materials** | Color contrast on slides. Text alternatives for charts and graphs. |
