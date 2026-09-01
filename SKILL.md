---
name: yq-travel-memory-poster
description: Transform one or more user-supplied travel photos into separate 2:3 vertical YQ travel-memory posters with the real photo above and a coordinated tactile postcard-journal card below. Use for photo-plus-scrapbook split posters, collectible travel cards, or consistent batches in this exact visual system; do not use for sticker-sheet-only or illustration-only requests.
---

# YQ Travel Memory Poster

Create one independent finished poster per source photo. Never combine several source photos into one poster unless the user explicitly asks.

## Fixed deliverable

- Use a vertical 2:3 canvas; default to `1024×1536`.
- Divide it horizontally at exactly 50%.
- Top half: the user's real photo. Do not regenerate, retouch, brighten, recolor, stretch, or distort it unless explicitly requested.
- Bottom half: one complete 4:3 illustrated travel scrapbook card. Never place a photographic patch inside this card.
- Do not create a separate sticker sheet or standalone sticker images.

Read [references/layout-spec.md](references/layout-spec.md) before composing the card. Read [references/art-direction.md](references/art-direction.md) before image generation. Read [references/prompt-template.md](references/prompt-template.md) when drafting or repairing the image-generation prompt.

## Workflow

1. Inspect each source at useful detail. Identify the place when grounded by the photo or user context; otherwise choose a truthful scene title rather than guessing a location.
2. Select one recognition anchor, six visibly distinct source-derived sticker motifs, a short English subtitle, and four postcard-paper items that do not repeat those stickers.
3. Generate only the complete 4:3 bottom card with an image-generation tool. Use the source photo as subject authority and the references above as the design authority.
4. Inspect the generated card for the complete outer border, exact module structure, six stickers, legible text, pale paper color, and four distinct paper keepsakes. Make one targeted repair when a clear defect exists.
5. Prepare the top photo as 4:3 without altering its appearance:
   - A 4:3 landscape photo only needs proportional resizing.
   - For another aspect ratio, prefer natural horizontal or vertical expansion that preserves the whole recognition anchor.
   - Crop only when expansion is unnecessary and the crop preserves every landmark used in the card. Never stretch.
6. Run `scripts/compose_poster.py` to assemble the final 2:3 PNG. Its default strict mode refuses a non-4:3 top input so an accidental destructive crop cannot pass silently.
7. Validate the result at full view and thumbnail view. The photo/card split must be exact, the photo must remain recognizable and undistorted, all borders must be visible, and the footer must read as postcard ephemera rather than an infographic.

## Batch behavior

- Analyze, generate, inspect, and save every image independently.
- Keep the layout, paper tone, typography hierarchy, and material language consistent across the batch.
- Vary titles, subtitles, sticker motifs, postmarks, ticket text, stamp artwork, note copy, and accent colors according to each source.
- Return every final poster separately. Do not offer separate sticker assets.

## User overrides

Honor explicit changes to aspect ratio, split, photo treatment, language, title, or footer content. Preserve all unspecified system rules. If the user asks to revise only one module, lock every other part of the card and edit only that module.

## Quality gate

Reject or repair a result when any of these occurs:

- the top photo is regenerated, stretched, visibly recolored, or cropped away from the card's recognition anchor;
- the card background becomes tan, dark beige, gray, or strongly yellowed;
- the top edge or rounded corners of the card border are missing or covered;
- the illustration becomes painterly, photographic, glossy, densely textured, or filled with small brush marks;
- the right panel has other than six stickers, or sticker labels are missing;
- footer items repeat sticker objects, resemble analytical icons, fill their cells heavily, or use generic camera/map-pin/connection symbols;
- several source photos are merged into one deliverable.
