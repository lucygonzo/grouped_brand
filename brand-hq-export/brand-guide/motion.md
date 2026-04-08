---
section: motion
last_verified: 2026-04-06
verified_by: Lucy
version: 1.2
status: active
change_log:
  - date: 2026-04-06
    change: Initial extraction from Brand HQ site v1.2
    source: Claude session — Brand HQ reorg
---

# Motion

Motion has mass. Elements enter with intention and settle with confidence. Bronze glows gradually. Stagger creates rhythm. Transitions run 300ms or longer. Spring easings that overshoot and settle. Every motion should feel like music -- cyclical, weighted, intentional.

> **Implementation Priority: Phase 2.** For the initial product launch, motion and animation are deprioritized in favor of shipping correct colors, typography, and layout. The easing curves and duration scale defined here are locked in and correct -- dev picks this up in Phase 2. **Do not introduce motion variables or transitions until the static component states are confirmed working.**


## Easing Curves

| Name | CSS Token | Cubic-Bezier | Character |
|---|---|---|---|
| **Ease Out** | `--ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Fast start, gentle landing. Default for entrances. |
| **Ease In-Out** | `--ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Symmetric acceleration and deceleration. Transitions between states. |
| **Spring** | `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Overshoots and settles. Playful, energetic. Toggles, badges, celebrations. |
| **Smooth** | `--ease-smooth` | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Subtle, barely noticeable. Background transitions, opacity fades. |
| **Snap** | (marketing only) | `cubic-bezier(0.5, 0, 0, 1)` | Quick and decisive. Marketing scroll animations. |

### CSS Token Definitions

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);
}
```


## Duration Scale

| Name | Value | Usage |
|---|---|---|
| **instant** | 100ms | Micro-interactions: checkbox, toggle, hover color |
| **fast** | 200ms | Button press feedback, tooltip show/hide |
| **default** | 300ms | Standard transitions, dropdown open/close |
| **moderate** | 500ms | Panel slide, card expand, stagger base |
| **slow** | 800ms | Page transitions, large surface changes |
| **cinematic** | 1200ms | Hero animations, splash screens, marketing reveals |


## Motion Principles

1. **Scroll drives narrative** -- on marketing surfaces, scroll position controls reveals and transitions
2. **Stagger creates rhythm** -- sequential elements animate in with offset delays, not all at once
3. **Bronze glows gradually** -- gold accent animations use slow/cinematic durations, never instant
4. **Active press is physical** -- buttons scale to 97% on press (`scale(0.97)`)
5. **Spring for celebration** -- use spring easing for positive-feedback moments (new fan, milestone hit)


## Cross-Surface Translation

| Surface | How Motion Shows Up |
|---|---|
| **Product (app)** | Full token system (Phase 2). Default 300ms transitions, spring for celebrations. |
| **Marketing site** | Scroll-driven reveals, cinematic durations, staggered card entrances |
| **Mobile** | Respect `prefers-reduced-motion`. Reduce durations by ~30% for perceived speed. |
| **Print** | N/A -- static medium |
| **Events/experiential** | Looping ambient animations (arc rotations, glow pulses) at cinematic pace |
| **Social** | GIF/video exports of key motion patterns for product demos |
| **Email** | N/A -- no animation support in most email clients |
| **Investor materials** | Slide transitions use ease-out at moderate (500ms) pace |
