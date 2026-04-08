---
section: patterns
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial framework created from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Patterns

Patterns that repeat across multiple screens. Define them once, apply consistently everywhere. This section captures the recurring UX patterns in the Grouped product.

> **Status:** This is a starter framework. Most patterns are identified but not yet fully documented with specs. Items marked "To be documented" have the structure ready to fill in once designs are finalized.


## The Conversion Funnel

Views -> Swaps -> Fans -> Engaged -> Revenue. Appears on dashboard, campaign detail, analytics. Needs consistent visual treatment showing progression and drop-off.

| Stage | Visual Treatment |
|---|---|
| Views | Neutral background (`--bg-overlay`) |
| Swaps | Focus blue tint (`rgba(124,187,223,0.1)`, border `rgba(124,187,223,0.15)`) |
| Fans | Success tint (`rgba(74,222,128,0.1)`, border `rgba(74,222,128,0.15)`) |

**Status:** Partially specced. Horizontal bar visualization exists. Needs detailed specs for dashboard vs. campaign detail vs. analytics variants.


## Feature Gates (Upgrade Prompts)

Pro tier is hidden until the campaign builder. Feature gates appear inline as contextual upgrade prompts -- not blocking modals.

| Property | Value |
|---|---|
| Background | `rgba(196,138,58,0.04)` |
| Border | `1px solid rgba(196,138,58,0.12)` |
| Title | 12px / 500 weight |
| Description | 11px / `--text-tertiary` |
| CTA | 11px / `--bronze-400` / 500 weight, arrow suffix |

**Status:** Partially specced. Visual treatment defined. Needs: trigger rules per screen, A/B test variants, dismissal behavior.


## Validation Moments

Positive-feedback states that reinforce key actions.

**Triggers:**
- New fan captured
- Milestone hit
- First paid subscriber
- Email credit earned

**Implementation:** Animation + optional sound. Uses spring easing (`--ease-spring`).

**Status:** To be documented. Needs: animation specs, sound design brief, trigger thresholds, cool-down rules.


## Artist Theming (Fan-Facing)

Fan-facing surfaces adapt to the artist's brand. Configurable: accent color, avatar, cover image. Grouped provides the layout shell; the artist's assets override it. Pro tier removes Grouped branding.

**Status:** To be documented. Needs: configurable token list, fallback behavior, color contrast enforcement against custom accent colors, Pro vs. Free tier differences.


## Between-Release Engagement

Month 2-3 churn occurs when artists have nothing to do between releases. Every screen should surface a next action. Dashboard must always show a suggested task.

**Status:** To be documented. Needs: suggested task algorithm, task card component spec, empty-state-to-suggestion flow, engagement metric tracking.


## CRM Sync Status

Fan data flows to connected CRMs. Sync status needs a consistent indicator.

| State | Visual |
|---|---|
| Connected | `--success` indicator dot |
| Syncing | `--info` animated indicator |
| Error | `--error` indicator dot |
| Last synced | Timestamp in `--text-tertiary` |

**Appears on:** Settings, fan directory, campaign detail.

**Status:** To be documented. Needs: sync indicator component spec, error recovery flow, retry behavior, settings panel layout.


## Campaign Creation Flow

Multi-step flow for building a new swap campaign.

**Steps:** Details -> Content -> Gate -> Publish

**Progress indicator:** Horizontal stepper with completed (green check), current (bronze number), and upcoming (muted number) states.

**Status:** To be documented. Needs: full step-by-step wireframes, validation rules per step, save-as-draft behavior, preview mode.


## Fan Pass / Wallet Pattern

Apple Wallet and Google Wallet integration for fan passes.

**Status:** To be documented. Needs: pass design template, data fields, update trigger rules, push notification specs, premium-feel visual treatment.


## Release Card States

Cards representing music releases across the platform.

**Possible states:**
- Draft
- Scheduled
- Live
- Completed
- Archived

**Status:** To be documented. Needs: state badge specs, transition rules, action menus per state, analytics preview per card.


## Empty States

First-run and zero-data states. Each screen needs its own variant.

**Structure:**
1. Icon (56px circle, `rgba(196,138,58,0.08)` background, `rgba(196,138,58,0.15)` border)
2. Title (16px / 500 weight)
3. Description (13px / `--text-tertiary`, max-width 240px)
4. Primary CTA button

**Status:** Partially specced. Generic empty state component exists. Needs: per-screen variants (campaigns, fans, analytics, email), illustration options, onboarding vs. returning-user differentiation.


## Cross-Surface Translation

| Surface | How Patterns Show Up |
|---|---|
| **Product (app)** | All patterns implemented with full interactivity and state management |
| **Marketing site** | Conversion funnel shown as static infographic. Feature gates N/A. |
| **Mobile** | Same patterns, stacked layouts. Validation moments use haptic feedback. |
| **Print** | N/A -- patterns are interactive/digital-only |
| **Events/experiential** | Fan pass pattern for event check-in kiosks |
| **Social** | Milestone validation moments adapted as shareable graphics |
| **Email** | CRM sync status as email notification template. Campaign state as digest content. |
| **Investor materials** | Conversion funnel as data slide. Campaign creation flow as product walkthrough. |
