# Image-generation prompt template

Use this template to generate the complete 4:3 bottom card. Replace bracketed fields with source-grounded choices. Keep all exact text short.

```text
Use case: stylized-concept
Asset type: one complete horizontal 4:3 illustrated travel scrapbook card, intended as the bottom 50% of a vertical 2:3 poster.

Input image:
- Image 1 is the source-photo and subject authority. Do not place photography inside the illustrated card.

Create one complete card, straight-on and edge-to-edge:
- bright very pale warm-ivory uncoated paper (#F7F2E8 feeling);
- continuous thin dark-navy rounded outer border with full top edge and both top corners visible;
- clear navy dividers;
- left about 62%: title "[TITLE]", subtitle "[SUBTITLE]", and one large simplified illustration;
- right about 38%: heading "TRAVEL STICKERS", exactly six stickers in 2 columns × 3 rows;
- bottom: exactly four equal footer cells.

Recognition anchor:
[Describe the primary spatial relationship and signature colors that must remain recognizable.]

Exactly six stickers and labels:
1. [MOTIF] — "[LABEL]"
2. [MOTIF] — "[LABEL]"
3. [MOTIF] — "[LABEL]"
4. [MOTIF] — "[LABEL]"
5. [MOTIF] — "[LABEL]"
6. [MOTIF] — "[LABEL]"

Footer travel paper, left to right:
1. Small round navy postmark: curved text "[PLACE]", center text "[SHORT CONTEXT]", two short cancellation lines.
2. Small notched [ACCENT COLOR] and cream ticket: "[ACTIVITY OR ROUTE]", "[PASS TYPE]", tiny serial "[SERIAL]".
3. Small upright perforated stamp: only abstract [SCENE COLOR/SHAPE DESCRIPTION], text "[STAMP NAME]", number "50". Do not depict any sticker object.
4. Small torn cream note with tiny [ACCENT COLOR] tape: exact two-line message "[LINE 1]" / "[LINE 2]".

Material and shape:
opaque matte gouache, chunky cut-paper silhouettes, fine uniform paper tooth, chalky handmade edges, slight risograph misregistration, flat colored shadows, 3–6 oversized masses, quiet negative space.

Footer scale:
each paper keepsake occupies only about 35–50% of its cell height or width, with generous empty ivory space. Text stays inside each paper object; no separate captions.

Avoid:
photorealistic patches, actual photography, painterly brush strokes, marker strokes, watercolor washes, wet blends, gradients, repeated small marks, detailed faces or mechanics, glossy 3D, smooth vector polish, clutter, missing or cropped borders, extra stickers, extra footer cells, camera icons, map pins, analytical icons, the word "CONNECTION", signatures, and watermarks.

Output exactly one complete 4:3 card only, with no surrounding mockup or separate sticker sheet.
```

## Targeted footer repair

When an otherwise-correct card has the wrong footer, use the current card as the edit target. State that only the four footer-cell contents may change. Lock the outer border, dividers, paper color, title, subtitle, main illustration, `TRAVEL STICKERS`, all six stickers, and every sticker label. Repeat the four paper-artifact specifications and the prohibition against object repetition.
