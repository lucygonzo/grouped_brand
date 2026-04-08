---
section: layout
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Layout & Responsive

Four breakpoint ranges, mobile-first. 12-column grid with responsive gutters. Build for the smallest screen first, add complexity at each step up. Minimum 44px touch targets at all sizes.


## Breakpoints

| Name | Range | Description |
|---|---|---|
| **Mobile** | 0 -- 639px | Single column. Fan-facing swap pages, mobile web app. Stacked layouts, full-width actions. |
| **Tablet** | 640 -- 1023px | Two columns where useful. Sidebar collapses to hamburger. Card grids go 2-up. |
| **Desktop** | 1024 -- 1439px | Primary artist dashboard experience. Sidebar always visible. Full data tables and charts. |
| **Wide** | 1440px+ | Max container width 1280px. Extra space becomes margins. Analytics and data-dense views expand. |

### CSS Breakpoints

```css
/* Mobile first — base styles are mobile */

/* Tablet and up */
@media (min-width: 640px) { ... }

/* Desktop and up */
@media (min-width: 1024px) { ... }

/* Wide screens */
@media (min-width: 1440px) { ... }
```


## Grid System

### Grid Specs

| Property | Value |
|---|---|
| Columns | 12 |
| Desktop gutter | 24px (`--space-6`) |
| Mobile gutter | 16px (`--space-4`) |
| Max container width | 1280px |

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

### Common Span Patterns

| Pattern | Usage |
|---|---|
| span 3 + span 9 | Sidebar + main content |
| span 4 + span 4 + span 4 | Three-column card grid |
| span 6 + span 6 | Two-column split |
| span 12 | Full-width content |


## Layout Patterns

| Pattern | Description | Use On |
|---|---|---|
| **Sidebar + Main** | Fixed sidebar (25%) with scrollable main area | Dashboard, campaigns, fan directory |
| **Full Width** | Edge-to-edge content, no sidebar | Swap pages, embeds, shared links |
| **Centered Narrow** | Max 480px centered container | Auth, onboarding, settings |


## Touch Targets

| Level | Minimum Size | Usage |
|---|---|---|
| **Primary** | 44px | Buttons, nav items, action areas |
| **Secondary** | 36px | Icon buttons, table rows, filter chips |


## Responsive Adjustments

### Type Scale

- D0 caps at **48px** on mobile (from 96px desktop)
- D1 caps at **28px** on mobile
- Body stays **14px** everywhere
- Component type (C1-C7) unchanged across breakpoints

### Spacing

Reduce to **75%** of desktop values on mobile for `space-8` and above. Small spacings (`space-1` through `space-6`) stay the same.

### Layout Behavior

- Sidebar collapses at **1024px**
- Card grids collapse from 2-col to **1-col at 640px**
- Tables scroll horizontally on mobile


## Confirmed for Launch

- Two primary breakpoints for v1: mobile narrow and desktop
- Design standard width: **1440px**. Past 1440px, outer margins and gutters scale; content holds max-width
- Column grid: **3-column layout** for main content area on desktop, stacks to single column on mobile

### Phase 2 -- Future Work

Dashboard layout investigation: customizable bento-box layout with drag-to-resize cards, saved dashboard views, and shareable report links. Requires research into responsive bento grid best practices before anything is specced or built. **Do not design this yet.**


## Never Do This

| Rule | Why |
|---|---|
| Never use `10px` for spacing or gutters | Not in the 4px base scale. Use 8px or 12px. |
| Never make touch targets smaller than 36px on any device | Accessibility floor. 44px for primary actions. |
| Never use desktop-first media queries | Mobile-first (`min-width`) only. Base styles = mobile. |
| Never exceed 1280px content width | Container max-width is 1280px. Beyond that, margins grow. |
| Never skip the sidebar collapse at 1024px | Below 1024px, sidebar becomes hamburger. No exceptions. |


## Cross-Surface Translation

| Surface | How Layout Shows Up |
|---|---|
| **Product (app)** | Full 12-column grid, sidebar + main pattern, responsive breakpoints |
| **Marketing site** | Full-width hero sections, centered narrow for forms, max-width containers |
| **Mobile** | Single-column stacked layouts, 16px gutters, 44px touch targets enforced |
| **Print** | N/A -- print layouts use their own grid based on format (A4, letter, etc.) |
| **Events/experiential** | Full-screen single-column, oversized touch targets for kiosk interaction |
| **Social** | Fixed aspect ratios (1:1, 4:5, 16:9) replace responsive grid |
| **Email** | 600px max-width single column, inline styles (no CSS grid support) |
| **Investor materials** | 16:9 slide grid, content centered within safe margins |
