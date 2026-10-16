"""Draws the app icon: four slot-coloured arcs forming a ring on a dark background.
Pure Python (no Pillow). Usage: python -I tools/make_icons.py <output folder>
"""
import math
import struct
import sys
import zlib
from pathlib import Path

BG = (13, 13, 13)
SLOTS = [(57, 135, 229), (217, 89, 38), (25, 158, 112), (201, 133, 0)]  # dark-mode slot colours 1-4
GAP_DEG = 14     # gap between arcs
SAMPLES = 3      # supersampling per axis, for smooth edges


def colour_at(x, y, size):
    """Colour of one sub-pixel. Ring sits inside the maskable safe zone (centre 80%)."""
    cx = cy = size / 2
    dx, dy = x - cx, y - cy
    r = math.hypot(dx, dy) / size
    if 0.20 <= r <= 0.31:
        angle = (math.degrees(math.atan2(dy, dx)) + 90 + 45) % 360  # start at top-left
        quarter, within = divmod(angle, 90)
        if GAP_DEG / 2 <= within <= 90 - GAP_DEG / 2:
            return SLOTS[int(quarter)]
    if r <= 0.075:  # centre dot
        return (240, 239, 236)
    return BG


def render(size):
    rows = []
    step = 1 / SAMPLES
    for py in range(size):
        row = bytearray([0])  # PNG filter byte
        for px in range(size):
            acc = [0, 0, 0]
            for sy in range(SAMPLES):
                for sx in range(SAMPLES):
                    c = colour_at(px + (sx + .5) * step, py + (sy + .5) * step, size)
                    acc[0] += c[0]; acc[1] += c[1]; acc[2] += c[2]
            n = SAMPLES * SAMPLES
            row += bytes(v // n for v in acc)
        rows.append(bytes(row))
    return b"".join(rows)


def png(size, raw):
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    header = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)  # 8-bit RGB
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for size in (192, 512):
        (out / f"icon-{size}.png").write_bytes(png(size, render(size)))
        print(f"icon-{size}.png written")
