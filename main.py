"""Entry for make.fun bounty 'Sum up 25 November's world news in one image'.

Writes one image to /output/entry.png by copying the image this
repository holds (entry.png). No network access. Deterministic:
every run writes the same bytes.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
