---
section: icons
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Iconography

Grouped uses **Phosphor Bold** as its interim icon library. The 2px strokes and rounded terminals mirror the Grouped logo's bold geometric character. Every icon inherits text color by default, making them feel like part of the typography, not decorations bolted on top.

> **Transition in progress:** Bob is building a custom icon set to replace Phosphor Bold. Custom SVGs are pending delivery from Figma. The website may need bolder icon strokes than the product. Until delivery, continue using Phosphor Bold.

> **When the custom set arrives:** Upload SVGs to Google Drive with documented links. Icons should be reviewed for visual cohesion with the new Grouped logo icon (concentric arc DNA, rounded caps, bold weight). Size scale and color inheritance rules will carry over.


## Why Phosphor Bold

| Grouped Logo Character | Phosphor Bold |
|---|---|
| 2.5px strokes | 2px strokes |
| Rounded caps | Rounded terminals |
| Concentric arcs | Bold weight |

The stroke weight and terminal shape of Phosphor Bold are the closest match to the Grouped logo's DNA among available icon libraries.


## Size Scale

| Size | Name | Usage |
|---|---|---|
| **16px** | Inline | Alongside body text, table cells, captions |
| **20px** | Default | Navigation items, list icons, input prefixes |
| **24px** | Buttons | Button icons, toolbar actions, card headers |
| **32px** | Feature | Empty states, onboarding, feature highlights |


## Color Rules

### 1. Inherit Text Color (Default)

Icons take on the text color of their context: `--T1` (primary), `--T2` (secondary), or `--T3` (tertiary). No separate icon color tokens needed.

### 2. Bronze for Accents

Use `var(--bronze-400)` for featured, premium, or highlighted icons. Sparingly. Reserved for brand moments, not routine UI.

### 3. Semantic for Status

Status icons use their semantic color token. These are the only icons that break from text color inheritance:

| State | Color Token | Icon |
|---|---|---|
| Success | `--success` (`#4ADE80`) | `ph-bold ph-check-circle` |
| Warning | `--warning` (`#F0C543`) | `ph-bold ph-warning` |
| Error | `--error` (`#F07068`) | `ph-bold ph-x-circle` |
| Info | `--info` (`#63B3ED`) | `ph-bold ph-info` |
| Loading | `--text-secondary` | `ph-bold ph-spinner` |


## Product Icon Set

### Navigation

| Icon | Class | Label |
|---|---|---|
| Home | `ph-bold ph-house` | Home |
| Analytics | `ph-bold ph-chart-line-up` | Analytics |
| Fans | `ph-bold ph-users` | Fans |
| Email | `ph-bold ph-envelope` | Email |
| Settings | `ph-bold ph-gear` | Settings |
| Alerts | `ph-bold ph-bell` | Alerts |
| Swaps | `ph-bold ph-swap` | Swaps |
| Campaigns | `ph-bold ph-megaphone` | Campaigns |

### Actions

| Icon | Class | Label |
|---|---|---|
| Add | `ph-bold ph-plus` | Add |
| Edit | `ph-bold ph-pencil-simple` | Edit |
| Delete | `ph-bold ph-trash` | Delete |
| Search | `ph-bold ph-magnifying-glass` | Search |
| Filter | `ph-bold ph-funnel` | Filter |
| Export | `ph-bold ph-download-simple` | Export |
| Copy | `ph-bold ph-copy` | Copy |
| Share | `ph-bold ph-share-network` | Share |

### Media & Music

| Icon | Class | Label |
|---|---|---|
| Music | `ph-bold ph-music-notes` | Music |
| Release | `ph-bold ph-vinyl-record` | Release |
| Artist | `ph-bold ph-microphone-stage` | Artist |
| Play | `ph-bold ph-play` | Play |
| Listen | `ph-bold ph-headphones` | Listen |
| Media | `ph-bold ph-image` | Media |
| Link | `ph-bold ph-link` | Link |
| Spotify | `ph-bold ph-spotify-logo` | Spotify |

### Status & Feedback

| Icon | Class | Color | Label |
|---|---|---|---|
| Success | `ph-bold ph-check-circle` | `--success` | Success |
| Warning | `ph-bold ph-warning` | `--warning` | Warning |
| Error | `ph-bold ph-x-circle` | `--error` | Error |
| Info | `ph-bold ph-info` | `--info` | Info |
| Loading | `ph-bold ph-spinner` | `--text-secondary` | Loading |
| View | `ph-bold ph-eye` | `--text-primary` | View |
| Locked | `ph-bold ph-lock` | `--text-primary` | Locked |
| Scheduled | `ph-bold ph-clock` | `--text-primary` | Scheduled |


## Guidelines

**Do:**
- Use Phosphor Bold consistently across all product surfaces
- Keep icons at one of the four standard sizes (16, 20, 24, 32px)
- Let icons inherit text color unless they carry semantic meaning
- Pair icons with text labels in navigation and primary actions

**Don't:**
- Mix icon libraries -- no Lucide, Feather, or Material icons alongside Phosphor
- Use thin or light weights -- they disappear on dark backgrounds and break brand consistency
- Use icons as the only affordance for critical actions -- always pair with a label or tooltip
- Apply custom stroke widths or fills -- Phosphor Bold's 2px strokes are the standard


## Usage (Code)

```html
<!-- CDN -->
<link href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css" rel="stylesheet">

<!-- Basic usage -->
<i class="ph-bold ph-music-notes"></i>

<!-- With size -->
<i class="ph-bold ph-music-notes" style="font-size: 24px;"></i>

<!-- In a button -->
<button class="btn btn-primary">
  <i class="ph-bold ph-plus" style="font-size: 20px;"></i>
  Create Campaign
</button>
```


## Cross-Surface Translation

| Surface | How Icons Show Up |
|---|---|
| **Product (app)** | Full Phosphor Bold set at standard sizes, inheriting text color |
| **Marketing site** | Phosphor Bold for feature icons, bronze accent for highlights |
| **Mobile** | Same icons, 20px minimum for touch contexts |
| **Print** | Static SVG exports at 24px+ for legibility |
| **Events/experiential** | Large-scale icon renders (32px+) for signage and kiosk UIs |
| **Social** | Icon + label lockups for feature callouts in posts |
| **Email** | Inline PNG fallbacks for email clients that strip web fonts |
| **Investor materials** | Icon grid screenshots for product capability slides |
