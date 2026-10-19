---
name: cover-maker
description: "用用户提供的真实图片制作中文内容封面，保留原标题与人物主体，完成构图、风格、文字层级和成品图。适用于短视频、图文或系列内容封面。"
---

# Cover Maker

Turn a saved real image into a cover that matches the creator's brief. This is the production stage. If the user still needs image links, use an available image-search tool first.

Use `imagegen` for the final cover render or edit. The saved real image should act as the base subject/reference, while Image 2 handles stylization, composition, text integration, and cover finishing.

## Inputs

Use any of:
- a local image path
- an attached image
- a folder of saved candidate images
- a script plus a chosen saved base image

If no image is provided, ask for the saved image path or switch to `cover-search` to collect source links.

## Cover Thesis

Extract from the script:
- the central conflict
- the person being warned, attacked, or awakened
- the emotional register
- the final judgment sentence

If the script already has an explicit title, treat the title as the first-priority thesis anchor before free interpretation:
- extract the title's concrete keywords first
- prefer the title's people / object / conflict words over broader mood words
- top title and bottom verdict should stay semantically tied to the original title unless the user explicitly asks for a different angle
- do not drift from the concrete people, objects and conflict in the title into a looser adjacent abstraction unless that abstraction is already clearly present in the title

Default title-preservation rule:
- if the user gives an explicit title, use the exact title itself as the main headline by default
- if the title is long, the main headline may be broken into 2-4 lines for layout; keep the original wording and order
- do not summarize, paraphrase, compress, sharpen, or replace the main headline unless the user explicitly asks for a shorter cover line or a different angle
- secondary text such as tag text, bottom verdict, side label, or small supporting copy may be freely developed from the title keywords and script thesis
- secondary text should deepen, sharpen, or complete the meaning of the title, not drift away from it

When the user has not supplied a title, generate:
- `上标题`: usually 4-8 Chinese characters, category-like and memorable
- `下结论`: usually 10-22 Chinese characters, split into 2-4 hard lines

When the user supplies a title, preserve its exact wording as the main headline even when longer than these guides.

Avoid soft self-help, textbook summaries, and vague motivational phrasing.

Priority order for cover wording:
1. exact user title
2. explicit title keywords
3. the script's central conflict
4. the script's final judgment sentence
5. emotional tone / atmosphere

Text role split:
- main headline: default to the exact user title
- secondary text: may use title keywords plus script thesis for sharper payoff wording
- if there is not enough room for the full title as the largest block, keep the title as the dominant text and move the sharper payoff sentence into a smaller lower band or tag

Account-positioning rule for secondary text:
- when the user has an obvious channel positioning, secondary text should not stop at repeating the topic in flatter words
- prefer extracting a reusable channel lens, series label, or diagnostic frame for the tag / subtitle / bottom verdict
- good secondary text often sounds like a column name, worldview lens, or method label rather than a plain restatement
- derive the channel lens from the creator's `7wc` brief or this request; if unavailable, keep supporting text close to the explicit title rather than inventing a worldview
- if both are available, combine them in this order:
  1. main headline = exact title
  2. tag / subtitle = channel-positioning lens
  3. bottom verdict = specific payoff or judgment
- avoid weak support text that merely repeats the title in flatter words

For a long title, keep the exact wording and order in the main headline; break it into lines for layout. Supporting text may draw from the title keywords and the script's judgment, but must stay on the same thesis.

## Visual Style

Choose one style lane. The creator's own cover style or current request takes priority over these presets:
- `Black Orange Figure`: default for named-figure commentary covers; famous face, black/white grading, orange border, cream headline, orange emphasis, dense full-frame typography.
- `Black Gold Authority`: institutions, labor, hierarchy, 学历, 身份, status anxiety.
- `Orange Heat Hustle`: money, self-media, business, internet survival.
- `Blue Impact Epic`: AI, systems, future, overwhelming forces.
- `Cinematic Portrait`: identity, loneliness, beauty, personal growth.
- `White Text Editorial`: text-heavy manifesto covers.

Default for covers using a recognizable public figure: `Black Orange Figure`.
Default for education/labor/status critique without a named figure: `Black Gold Authority`.

## Production Rules

Hard rule for final assets:
- final cover production must use `imagegen` / Image 2.0
- local code, PIL, canvas, or Photoshop-like scripts may be used only for rough layout tests, masks, measurement helpers, or optional internal structure sketches
- do not deliver a code-rendered cover as the final `cover-maker` result unless the user explicitly asks for a code-rendered fallback
- do not default to applying a local font file or manually overlaying final text; the final visible cover should come from `imagegen` unless the user explicitly asks for a code-rendered/text-overlay fallback
- when a real base image is provided, preserve the recognizable identity of the original figure and use Image 2.0 for grading, crop, typography integration, border, texture, and final composition

Structure-first workflow:
- `cover-maker` must first determine the cover structure internally, then automatically pass that locked structure to `imagegen`; do not stop to ask whether the user wants a sketch or a final image.
- The internal structure is a production blueprint, not the final deliverable. Include: output ratio, style lane, subject placement, exact text blocks, text hierarchy, emphasis words, top/middle/bottom bands, border, color plan, and avoid list.
- The `imagegen` prompt must include a clearly labeled `LOCKED STRUCTURE` section plus an `EXACT TEXT` section. Do not rely on a loose visual-style prompt after the structure has been decided.
- The locked structure should specify where each text block sits, how large it is relative to other text, which words dominate, and which parts of the face must remain unobstructed.
- If the user gives an explicit title, lock the main headline wording and line breaks before calling `imagegen`. The prompt should tell `imagegen` to keep that exact text and the specified layout.
- If direct `imagegen` text rendering produces wrong Chinese characters, first retry with a more constrained prompt and fewer text blocks. Only use a local manual text overlay if the user explicitly approves that fallback.
- If the user explicitly asks for "只要结构/草图/方案", then stop at the structure output. Otherwise, always produce final image assets.

Output folder rule:
- Save final cover files under the user's chosen output folder. If none is given, use a clearly named folder under the current workspace.
- At the first new visual output in a conversation/topic, create one folder for that conversation or topic.
- Reuse that same folder for every later cover, background, variant, or related visual produced in the same conversation/topic.
- Do not default to separate top-level `covers\` or `backgrounds\` folders.
- Name cover files by type and ratio, for example `<topic-slug>-cover-3x4.png` and `<topic-slug>-cover-4x3.png`, so they can sit beside background files in the same folder.
- If the user explicitly names an output folder, use that folder and keep all related assets there.

For a saved image, specify:
- output both versions by default unless the user asks for only one:
  - vertical `3:4`
  - horizontal `4:3`
- crop ratio, usually vertical `3:4` and horizontal `4:3`
- subject placement: face upper third or center-left/right
- top text zone and bottom text zone
- border color and thickness
- shadow/contrast/grain treatment
- title color: cream, faded gold, orange, blue, or white
- emphasis plan: choose 1-3 key words in the bottom conclusion for color emphasis or weight contrast
- whether `imagegen` should render text directly or whether the user has explicitly approved a manual text-overlay fallback
- top title and bottom verdict should visually span the available width; avoid leaving dead zones in the top or bottom text bands
- subtitle/tag text such as `版权实验` should be legible and materially present, not a tiny corner note
- for named-figure covers, use dense full-frame composition: top headline fills the top band, bottom verdict fills the lower band, and the face remains recognizable behind or between them
- avoid minimalist negative space; empty right-side or bottom-side blocks are a failure unless the user explicitly asks for sparse editorial style
- for horizontal `4:3`, do not put all typography on the left and leave the right side unused; extend headline/verdict/large emphasis text across the width
- for vertical `3:4`, keep the same packed logic: top title nearly spans the width, bottom verdict nearly spans the width, with no tiny tag text

Do not replace the real photo with a different generated person. Keep the original person or scene identity recognizable, and use Image 2 to adjust grading, crop, border, texture, layout, and text.

## Default Image 2.0 Prompt Pattern

When making a named-figure cover, adapt this prompt instead of starting from scratch:

```text
Use the provided [FIGURE] image as the base/reference. Preserve [FIGURE]'s recognizable face and identity; do not replace them with another person.

Create a bold Chinese commentary cover in a black-orange-gold viral style. Full-bleed portrait, high-contrast black-and-white grading, gritty film grain, worn print texture, thick vivid orange border.

Top headline: "[TOP_TITLE]" must horizontally fill the top text band, huge cream/gold Chinese display type, heavy black shadow/stroke, no empty right-side dead space.

Middle label: "[TAG]" should be clearly visible and medium-large, orange-gold, not a tiny corner note.

Bottom verdict: "[BOTTOM_LINE_1]" and "[BOTTOM_LINE_2]" should fill the lower text band horizontally. White base text with orange highlights on [HIGHLIGHT_WORDS]. Dense, aggressive, like a viral Chinese commentary thumbnail.

Keep the layout packed across the full frame: top band filled, bottom band filled, face still recognizable in the background/center. Add subtle halftone, duplicated-line, or photocopy texture when relevant.
```

## Output Format

Internal structure blueprint before image generation:

```markdown
1. 方向名
2. 上标题
3. 下结论
4. 适配原因
5. 底图处理
6. 排版方案
7. 制作步骤
```

Use this blueprint to build the `imagegen` prompt. Do not deliver only the blueprint unless the user explicitly asks for a structure-only answer.

When asked to make the actual asset:
- inspect the image if needed
- determine the internal structure blueprint
- create or edit the image with `imagegen`
- by default return both output paths:
  - one `3:4`
  - one `4:3`
- return the exact requested cover text and saved output path when a file is produced

Read [references/cover-style.md](references/cover-style.md) for the account's visual grammar.

