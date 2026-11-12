#!/usr/bin/env python3
"""Coolest art entry (make.fun coolest-art-01).

The art is the entry.png bundled beside this file: "Aurora Fox", a white
arctic fox with a huge flowing tail standing on a snowy ridge under a
swirling aurora borealis sky in teal, green and violet.

This program copies those exact bytes to /output/entry.png. It uses only
the Python standard library, touches no network, reads no clock, and
writes the same bytes on every run, so two runs are byte-identical.
"""

import hashlib
import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    with open(source, "rb") as f:
        data = f.read()

    os.makedirs(out_dir, exist_ok=True)
    with open(target, "wb") as f:
        f.write(data)

    # Confirm the copy is complete and byte-for-byte identical: a size
    # check alone would miss a same-length but corrupted write, so hash
    # the file back from disk and compare it with the source bytes.
    # The gate scores the exact bytes written, so a mismatch must fail.
    digest = hashlib.sha256(data).hexdigest()
    with open(target, "rb") as f:
        written_digest = hashlib.sha256(f.read()).hexdigest()
    if written_digest != digest:
        print("entry.png: written bytes differ from source (sha256 "
              "mismatch)", file=sys.stderr)
        return 1
    written = os.path.getsize(target)
    print(f"entry.png: {written} bytes -> {target} "
          f"(sha256 {digest[:12]}...)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
