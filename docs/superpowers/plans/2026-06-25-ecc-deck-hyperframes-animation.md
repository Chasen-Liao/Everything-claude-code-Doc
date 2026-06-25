# ECC Deck HyperFrames Animation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a standalone HyperFrames project that turns the existing 10-page ECC guide deck into a 1920x1080 animated video composition.

**Architecture:** Create a new `hyperframes-ecc-deck/` project beside the MkDocs site, leaving `docs/deck.html` untouched. Implement one root composition in `index.html` with shared notebook styling, ten scene sections, GSAP-managed entrances, and timed page transitions. Keep visual identity in `DESIGN.md` so the composition has explicit color, type, and motion rules.

**Tech Stack:** HyperFrames CLI, HTML, CSS, GSAP, Node.js via `npx hyperframes`.

---

### Task 1: Environment and Scaffold

**Files:**
- Create: `hyperframes-ecc-deck/DESIGN.md`
- Create: `hyperframes-ecc-deck/index.html`
- Read: `docs/deck.html`

- [ ] **Step 1: Check HyperFrames runtime**

Run:

```powershell
node --version
npx hyperframes info
```

Expected: Node is available and HyperFrames prints version/environment information. If Node is below 22 or HyperFrames cannot run, run:

```powershell
npx hyperframes doctor
```

Expected: doctor reports the missing runtime dependency clearly.

- [ ] **Step 2: Scaffold a blank project**

Run:

```powershell
npx hyperframes init hyperframes-ecc-deck --non-interactive
```

Expected: `hyperframes-ecc-deck/` exists and contains at least `index.html` or a starter composition.

- [ ] **Step 3: Replace the starter design file**

Create `hyperframes-ecc-deck/DESIGN.md` with:

```markdown
# ECC Deck Visual Identity

## Style Prompt

A polished editorial notebook presentation for developers: cream paper on a dark desk-like background, binder holes on the left, thin ruled paper texture, and colorful index tabs on the right edge. The look should feel like a curated product notebook rather than a generic tech promo.

## Colors

- Outer background: `#2d2d2d`
- Paper background: `#f8f6f1`
- Primary text: `#1a1a1a`
- Secondary text: `#6b6358`
- Rule line: `#d8d2c4`
- Mint tab: `#98d4bb`
- Lavender tab: `#c7b8ea`
- Pink tab: `#f4b8c5`
- Sky tab: `#a8d8ea`
- Yellow tab: `#ffe6a7`

## Typography

- Display: `Bodoni Moda`, `Didot`, serif
- Body: `DM Sans`, `Helvetica Neue`, sans-serif

## Motion

- Use page-cover transitions instead of hard cuts.
- Animate elements in from their final CSS layout using `gsap.from()`.
- Vary entrance direction and easing by content type.
- Keep outgoing scenes fully visible until the page transition starts.
- Only the final scene may fade out.

## What NOT to Do

- Do not use blue-purple tech gradients.
- Do not replace the notebook theme with generic cards.
- Do not use hard cuts between pages.
- Do not animate text to unreadable sizes.
- Do not add narration, subtitles, or music.
```

- [ ] **Step 4: Commit scaffold**

Run:

```powershell
git add hyperframes-ecc-deck/DESIGN.md hyperframes-ecc-deck/index.html
git commit -m "feat: scaffold ecc hyperframes deck"
```

Expected: commit succeeds. Do not stage unrelated `Python/` files.

### Task 2: Static Composition Layout

**Files:**
- Modify: `hyperframes-ecc-deck/index.html`
- Read: `docs/deck.html`

- [ ] **Step 1: Replace `index.html` with a static HyperFrames composition**

Write `hyperframes-ecc-deck/index.html` as a standalone root composition, not a `<template>`. Use this structure:

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ECC Deck Animation</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@400;500;700&display=swap');

    :root {
      --bg-outer: #2d2d2d;
      --bg-page: #f8f6f1;
      --text-primary: #1a1a1a;
      --text-secondary: #6b6358;
      --rule: #d8d2c4;
      --tab-1: #98d4bb;
      --tab-2: #c7b8ea;
      --tab-3: #f4b8c5;
      --tab-4: #a8d8ea;
      --tab-5: #ffe6a7;
      --font-display: 'Bodoni Moda', 'Didot', serif;
      --font-body: 'DM Sans', 'Helvetica Neue', sans-serif;
    }

    * { box-sizing: border-box; }
    html, body { margin: 0; width: 100%; height: 100%; background: var(--bg-outer); }

    [data-composition-id="ecc-deck"] {
      position: relative;
      width: 1920px;
      height: 1080px;
      overflow: hidden;
      background: var(--bg-outer);
      color: var(--text-primary);
      font-family: var(--font-body);
    }

    .scene {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      opacity: 1;
    }

    .paper {
      position: absolute;
      top: 56px;
      bottom: 56px;
      left: 120px;
      right: 150px;
      background: var(--bg-page);
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,.25), 0 18px 50px rgba(0,0,0,.45), inset 0 0 0 1px rgba(255,255,255,.35);
      background-image: linear-gradient(rgba(26,26,26,.018) 1px, transparent 1px), linear-gradient(180deg, var(--bg-page), var(--bg-page));
      background-size: 100% 44px, 100% 100%;
    }

    .page {
      position: absolute;
      inset: 0;
      padding: 78px 110px 78px 150px;
      display: flex;
      flex-direction: column;
    }

    .holes {
      position: absolute;
      left: 38px;
      top: 90px;
      bottom: 90px;
      width: 26px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .holes span {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--bg-outer);
      box-shadow: inset 0 2px 4px rgba(0,0,0,.7), 0 1px 0 rgba(255,255,255,.55);
    }

    .margin-rule {
      position: absolute;
      left: 92px;
      top: 0;
      bottom: 0;
      width: 1px;
      background: var(--tab-3);
      opacity: .55;
    }

    .tabs {
      position: absolute;
      right: 106px;
      top: 116px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .tab {
      writing-mode: vertical-rl;
      width: 56px;
      height: 158px;
      border-radius: 0 10px 10px 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 17px;
      font-weight: 700;
      letter-spacing: .3em;
      text-transform: uppercase;
      color: rgba(26,26,26,.78);
      box-shadow: 2px 2px 6px rgba(0,0,0,.3);
      opacity: .82;
    }

    .tab.on { opacity: 1; transform: translateX(8px); }
    .tab-1 { background: var(--tab-1); }
    .tab-2 { background: var(--tab-2); }
    .tab-3 { background: var(--tab-3); }
    .tab-4 { background: var(--tab-4); }
    .tab-5 { background: var(--tab-5); }

    .runhead, .baseline {
      display: flex;
      justify-content: space-between;
      font-size: 17px;
      letter-spacing: .26em;
      text-transform: uppercase;
      color: var(--text-secondary);
    }

    .runhead {
      border-bottom: 1px solid var(--rule);
      padding-bottom: 18px;
      margin-bottom: 40px;
    }

    .baseline {
      margin-top: auto;
      border-top: 1px solid var(--rule);
      padding-top: 16px;
      font-size: 15px;
    }

    .display, .h2, .divider-no, .toc-title, .cmd-name, .gcard h3, .point h3 {
      font-family: var(--font-display);
    }

    .display { font-size: 150px; line-height: .98; font-weight: 700; }
    .h2 { font-size: 84px; line-height: 1.04; font-weight: 700; }
    .lede { font-size: 30px; line-height: 1.5; color: var(--text-secondary); max-width: 980px; }
    .kicker { font-size: 17px; font-weight: 700; letter-spacing: .3em; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 22px; }
    .chip { display: inline-block; width: 30px; height: 12px; border-radius: 3px; margin-right: 12px; }
  </style>
</head>
<body>
  <div data-composition-id="ecc-deck" data-width="1920" data-height="1080">
    <section class="scene" id="scene-01"></section>
    <section class="scene" id="scene-02"></section>
    <section class="scene" id="scene-03"></section>
    <section class="scene" id="scene-04"></section>
    <section class="scene" id="scene-05"></section>
    <section class="scene" id="scene-06"></section>
    <section class="scene" id="scene-07"></section>
    <section class="scene" id="scene-08"></section>
    <section class="scene" id="scene-09"></section>
    <section class="scene" id="scene-10"></section>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
  <script>
    window.__timelines = window.__timelines || {};
    const tl = gsap.timeline({ paused: true });
    window.__timelines["ecc-deck"] = tl;
  </script>
</body>
</html>
```

- [ ] **Step 2: Run lint for structural feedback**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes lint
```

Expected: no missing composition-id or timeline registration errors.

- [ ] **Step 3: Commit static base**

Run:

```powershell
git add hyperframes-ecc-deck/index.html
git commit -m "feat: add ecc deck composition base"
```

### Task 3: Add Ten Scene Markup Blocks

**Files:**
- Modify: `hyperframes-ecc-deck/index.html`

- [ ] **Step 1: Add reusable CSS for slide content**

Inside the existing `<style>` block, add classes for `.close-wrap`, `.cover-meta`, `.toc`, `.divider-wrap`, `.points`, `.stat-wrap`, `.cmd-list`, `.grid4`, and `.notes`, copied and simplified from `docs/deck.html`.

Expected: visual proportions match the original deck at 1920x1080, with no interactive controls.

- [ ] **Step 2: Fill `scene-01` through `scene-10`**

Replace empty scene sections with static scene content copied from `docs/deck.html`, preserving the ten page topics and Chinese text. Each scene must include:

```html
<div class="paper">
  <div class="holes"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
  <div class="margin-rule"></div>
  <div class="page">
    <!-- scene-specific runhead, body, notes, baseline -->
  </div>
</div>
<div class="tabs" aria-hidden="true">
  <!-- five tabs, with the active one using class "on" -->
</div>
```

Expected: every scene is complete as a static frame.

- [ ] **Step 3: Add visibility bootstrap**

At the start of the script, before registering the timeline, add:

```js
const scenes = gsap.utils.toArray(".scene");
gsap.set(scenes, { autoAlpha: 0 });
gsap.set("#scene-01", { autoAlpha: 1 });
```

Expected: only the first scene is visible at page load.

- [ ] **Step 4: Inspect static hero frames**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes inspect --at 1,8,15,22,29,36,43,50,57,64
```

Expected: no text overflow outside the canvas. If inspect reports overflow, reduce the local font size or increase the containing width for that exact element.

- [ ] **Step 5: Commit static scenes**

Run:

```powershell
git add hyperframes-ecc-deck/index.html
git commit -m "feat: add ecc deck scene markup"
```

### Task 4: Add GSAP Timeline and Transitions

**Files:**
- Modify: `hyperframes-ecc-deck/index.html`

- [ ] **Step 1: Add timeline constants and helpers**

Replace the empty script timeline body with:

```js
window.__timelines = window.__timelines || {};

const tl = gsap.timeline({ paused: true });
const sceneDuration = 6.6;
const transitionDuration = 0.55;
const scenes = gsap.utils.toArray(".scene");

gsap.set(scenes, { autoAlpha: 0, y: 0, scale: 1 });
gsap.set("#scene-01", { autoAlpha: 1 });

function enterScene(scene, at) {
  const root = `#${scene.id}`;
  tl.set(scene, { autoAlpha: 1, y: 28, scale: 0.992 }, at);
  tl.fromTo(`${root} .paper`, { y: 36, scale: 0.985 }, { y: 0, scale: 1, duration: 0.75, ease: "power3.out" }, at + 0.1);
  tl.from(`${root} .runhead`, { y: 22, opacity: 0, duration: 0.42, ease: "power2.out" }, at + 0.2);
  tl.from(`${root} .anim-main`, { y: 46, opacity: 0, duration: 0.68, stagger: 0.12, ease: "expo.out" }, at + 0.42);
  tl.from(`${root} .tabs .tab`, { x: -20, opacity: 0, duration: 0.42, stagger: 0.04, ease: "back.out(1.4)" }, at + 0.55);
  tl.from(`${root} .baseline`, { y: 16, opacity: 0, duration: 0.38, ease: "power1.out" }, at + 0.9);
}

function transitionScenes(outScene, inScene, at) {
  tl.to(outScene, { y: -34, scale: 0.988, duration: transitionDuration, ease: "power2.inOut" }, at);
  tl.set(inScene, { autoAlpha: 1, y: 42, scale: 0.992 }, at + 0.08);
  tl.to(inScene, { y: 0, scale: 1, duration: transitionDuration, ease: "power3.out" }, at + 0.08);
  tl.set(outScene, { autoAlpha: 0 }, at + transitionDuration + 0.08);
}

scenes.forEach((scene, index) => {
  const at = index * sceneDuration;
  if (index === 0) {
    enterScene(scene, 0);
  } else {
    transitionScenes(scenes[index - 1], scene, at - transitionDuration);
    enterScene(scene, at);
  }
});

tl.to("#scene-10 .paper", { opacity: 0.92, duration: 0.6, ease: "power2.inOut" }, scenes.length * sceneDuration - 0.9);

window.__timelines["ecc-deck"] = tl;
```

- [ ] **Step 2: Mark animating elements**

Add `anim-main` to the visible elements in each scene: kicker, display headings, h2 headings, lede paragraphs, cover metadata, toc rows, divider numbers, divider bars, point rows, command rows, grid cards, close links, and CTA.

Expected: every scene has at least three `.anim-main` elements unless the scene content is intentionally sparse.

- [ ] **Step 3: Run lint and validate**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes lint
npx hyperframes validate
```

Expected: lint and validate complete without structural errors.

- [ ] **Step 4: Commit animation timeline**

Run:

```powershell
git add hyperframes-ecc-deck/index.html
git commit -m "feat: animate ecc deck timeline"
```

### Task 5: Final QA and Preview

**Files:**
- Modify only if QA reports concrete layout or validation issues: `hyperframes-ecc-deck/index.html`

- [ ] **Step 1: Run visual inspection**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes inspect --samples 15
```

Expected: no text overflow, clipping, or off-canvas content. If a decorative transition is flagged, add `data-layout-allow-overflow` only to the scene wrapper involved in that transition.

- [ ] **Step 2: Try draft render**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes render --quality draft --output renders/ecc-deck-draft.mp4
```

Expected: MP4 render succeeds. If FFmpeg or Chrome is missing, run `npx hyperframes doctor` and record the blocker in the final response.

- [ ] **Step 3: Start preview server**

Run:

```powershell
cd hyperframes-ecc-deck
npx hyperframes preview --port 3017
```

Expected: preview server starts. Give the user this URL:

```text
http://localhost:3017/#project/hyperframes-ecc-deck
```

- [ ] **Step 4: Run MkDocs strict build from repository root**

Run:

```powershell
cd D:\MyProjects\Everything-claude-code-Doc
python -m mkdocs build --strict
```

Expected: MkDocs build passes and is unaffected by the new HyperFrames directory.

- [ ] **Step 5: Commit QA fixes**

If any QA fixes were made, run:

```powershell
git add hyperframes-ecc-deck/index.html
git commit -m "fix: polish ecc deck animation qa"
```

If no QA fixes were needed, do not create an empty commit.
