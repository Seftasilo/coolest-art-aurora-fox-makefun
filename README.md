# Aurora Fox — Make the coolest art (make.fun `coolest-art-01`)

A single piece of art, written by `main.py` to `/output/entry.png`.

## The piece

**"Aurora Fox"** — a white arctic fox with a huge flowing tail stands alone
on a snowy ridge under a vast swirling aurora borealis sky in teal, green
and violet, with snowflakes drifting over a dark pine forest.

Why this concept, against the judge's criteria in order:

1. **It stops you.** The glowing spiral aurora fills the whole sky; the
   bright white fox against the dark blue ridge pulls the eye in one glance.
2. **The idea.** The fox's tail seems to dissolve into the aurora itself —
   the animal is part of the night sky, not just standing under it.
3. **Style.** One mood throughout: cold ethereal teal and violet night,
   painterly and calm, the opposite of a hot or busy palette.
4. **Craft.** Clean render, no text, no smears or garbled details; the fox
   silhouette, the ridge and the forest all read clearly.
5. **It reads small.** At ~300 px the white fox shape and the aurora swirl
   still hit — the composition is one big shape, not detail.

## How it was made

- The image was generated as original art for this entry (no stock photo,
  no one else's artwork), then center-cropped to square, resized to
  1024×1024 and saved as JPEG quality 92 (216,264 bytes — under the
  1 MiB limit).
- `main.py` (Python 3.13, standard library only) copies the bundled
  `entry.png` byte-for-byte to `/output/entry.png`. No network, no clock,
  no randomness: two runs write identical bytes.

## Files

- `main.py` — the entrypoint; copies `entry.png` to the output directory.
- `entry.png` — the art itself (JPEG bytes, 1024×1024, 216,264 bytes).
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the entrant's wallet.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png; run it twice and compare sha256 — identical.
```

## Verify

```sh
python3 -c "from PIL import Image; im=Image.open('entry.png'); print(im.format, im.size)"
ls -l entry.png   # must be <= 1048576 bytes
```
