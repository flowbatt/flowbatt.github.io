"""Render FlowBatt's 1200 × 630 social card from official Source Sans 3 assets.

Run with the existing ML Python environment (Pillow and fontTools):
    PYTHONDONTWRITEBYTECODE=1 python webpage/scripts/create_social_card.py

WOFF2 fonts are decoded to TrueType in memory; no temporary fonts, external
images, system font lookup, or writes outside webpage/ are used.
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

WEBPAGE = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1200, 630
SCALE = 2  # Supersample text, then reduce once for clean social-preview edges.
NAVY = "#17365D"
BLACK = "#111111"
MAGENTA = "#C2188B"


def font(face: str, size: int) -> ImageFont.FreeTypeFont:
    """Use the same unmodified static Source Sans 3 face as the website."""
    with TTFont(WEBPAGE / "public/fonts" / f"source-sans-3-{face}.woff2") as source:
        source.flavor = None
        decoded = BytesIO()
        source.save(decoded)
        decoded.seek(0)
        return ImageFont.truetype(decoded, size=size * SCALE)


def main() -> None:
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), "white")
    draw = ImageDraw.Draw(image)

    def text(x: int, y: int, value: str, face: str, size: int, color: str) -> None:
        position = (x * SCALE, y * SCALE)
        selected_font = font(face, size)
        bounds = draw.textbbox(position, value, font=selected_font, anchor="lt")
        # Preserve at least 64 px breathing room on every outer edge.
        assert bounds[0] >= 64 * SCALE and bounds[1] >= 64 * SCALE, (value, bounds)
        assert bounds[2] <= (WIDTH - 64) * SCALE, (value, bounds)
        assert bounds[3] <= (HEIGHT - 64) * SCALE, (value, bounds)
        draw.text(position, value, font=selected_font, fill=color, anchor="lt")

    text(76, 70, "NeurIPS 2026", "semibold", 28, MAGENTA)
    draw.rectangle((76 * SCALE, 126 * SCALE, 148 * SCALE, 131 * SCALE), fill=MAGENTA)

    text(76, 174, "FlowBatt", "bold", 100, NAVY)
    text(76, 309, "Flow Matching for Probabilistic", "semibold", 47, BLACK)
    text(76, 367, "Battery Degradation Prediction", "semibold", 47, BLACK)

    draw.line((76 * SCALE, 500 * SCALE, 1124 * SCALE, 500 * SCALE), fill="#E5EAF0", width=SCALE)
    text(76, 538, "Probabilistic battery degradation prediction", "regular", 26, NAVY)

    image = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    metadata = PngImagePlugin.PngInfo()
    metadata.add_text("Title", "FlowBatt: Flow Matching for Probabilistic Battery Degradation Prediction")
    metadata.add_text("Description", "NeurIPS 2026 — Probabilistic battery degradation prediction")
    metadata.add_text("Font", "Source Sans 3, official Adobe static release 3.052R; see fonts/SOURCE-SANS-3-SOURCE.txt")
    output = WEBPAGE / "public/social-card.png"
    image.save(output, pnginfo=metadata, optimize=True, compress_level=9)
    print(f"Wrote {output.relative_to(WEBPAGE)} ({WIDTH} × {HEIGHT}, {output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
