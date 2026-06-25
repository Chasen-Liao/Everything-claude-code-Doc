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
