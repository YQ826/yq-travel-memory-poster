#!/usr/bin/env python3
"""Compose an exact 50/50 photo-and-card YQ travel poster."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Pillow is required: python3 -m pip install Pillow") from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Join a 4:3 real photo above a 4:3 scrapbook card into an exact 2:3 PNG."
    )
    parser.add_argument("--photo", required=True, type=Path)
    parser.add_argument("--card", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", type=int, default=1024)
    parser.add_argument("--height", type=int, default=1536)
    parser.add_argument(
        "--photo-fit",
        choices=("strict", "cover"),
        default="strict",
        help="strict refuses non-4:3 photos; cover crops without distortion",
    )
    parser.add_argument("--focal-x", type=float, default=0.5)
    parser.add_argument("--focal-y", type=float, default=0.5)
    return parser.parse_args()


def require_file(path: Path, label: str) -> None:
    if not path.is_file():
        raise SystemExit(f"{label} not found: {path}")


def is_ratio(width: int, height: int, target: float, tolerance: float = 0.005) -> bool:
    return abs((width / height) - target) <= tolerance


def resize_cover(image: Image.Image, size: tuple[int, int], focal_x: float, focal_y: float) -> Image.Image:
    target_w, target_h = size
    scale = max(target_w / image.width, target_h / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    overflow_x = max(0, resized.width - target_w)
    overflow_y = max(0, resized.height - target_h)
    left = round(overflow_x * focal_x)
    top = round(overflow_y * focal_y)
    return resized.crop((left, top, left + target_w, top + target_h))


def main() -> int:
    args = parse_args()
    require_file(args.photo, "Photo")
    require_file(args.card, "Card")

    if args.width <= 0 or args.height <= 0 or args.height % 2:
        raise SystemExit("Width and height must be positive; height must be even.")
    if args.width * 3 != args.height * 2:
        raise SystemExit("The final canvas must have an exact 2:3 aspect ratio.")
    if not (0.0 <= args.focal_x <= 1.0 and 0.0 <= args.focal_y <= 1.0):
        raise SystemExit("Focal coordinates must be between 0 and 1.")

    half_size = (args.width, args.height // 2)
    with Image.open(args.photo) as raw_photo:
        photo = ImageOps.exif_transpose(raw_photo).convert("RGB")
    with Image.open(args.card) as raw_card:
        card = ImageOps.exif_transpose(raw_card).convert("RGB")

    target_ratio = 4 / 3
    if args.photo_fit == "strict" and not is_ratio(photo.width, photo.height, target_ratio):
        raise SystemExit(
            f"Photo is {photo.width}×{photo.height}, not 4:3. Expand it to 4:3 first, "
            "or use --photo-fit cover with deliberate focal coordinates."
        )
    if not is_ratio(card.width, card.height, target_ratio):
        raise SystemExit(f"Card is {card.width}×{card.height}, not 4:3; repair the card before composing.")

    if args.photo_fit == "cover":
        top = resize_cover(photo, half_size, args.focal_x, args.focal_y)
    else:
        top = photo.resize(half_size, Image.Resampling.LANCZOS)
    bottom = card.resize(half_size, Image.Resampling.LANCZOS)

    poster = Image.new("RGB", (args.width, args.height))
    poster.paste(top, (0, 0))
    poster.paste(bottom, (0, half_size[1]))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    poster.save(args.output, format="PNG", optimize=True)

    with Image.open(args.output) as check:
        if check.size != (args.width, args.height):
            raise SystemExit("Output validation failed: unexpected dimensions.")
    print(args.output.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
