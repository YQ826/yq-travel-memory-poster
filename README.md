# YQ Travel Memory Poster

A Codex skill that turns travel photos into consistent 2:3 memory posters: the original photo occupies the top half, while a coordinated illustrated postcard-journal card fills the bottom half.

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/YQ826/yq-travel-memory-poster.git ~/.codex/skills/yq-travel-memory-poster
```

Restart Codex if the skill does not appear immediately, then invoke it with `$yq-travel-memory-poster` or attach travel photos and ask for a poster in this style.

## Contents

- `SKILL.md` — skill routing and workflow
- `agents/openai.yaml` — Codex UI metadata
- `references/` — layout, art direction, and prompt guidance
- `scripts/compose_poster.py` — deterministic 50/50 poster assembly

The composition script requires [Pillow](https://pypi.org/project/pillow/).
