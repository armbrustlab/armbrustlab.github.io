#!/usr/bin/env python3.10

# Remove file entries from bibtex file, in-place edit

import sys
import shutil
import tempfile

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as fh:
            with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as outfh:
                tmppath = outfh.name
                for line in fh:
                    if line.startswith("\tfile = {"):
                        continue
                    outfh.write(line)
        shutil.move(tmppath, sys.argv[1])
