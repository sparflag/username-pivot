#!/usr/bin/env python3
"""Username Pivot — real mini-challenge (username-pivot)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", None)


def main():
    mat = fetch_material()
    key = CHALLENGE_KEY or "pivot-key"
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    profiles = {
        "username": "shadowbyte42",
        "profiles": [
            {"site": "codeforge", "bio": "CTF enjoyer", "posts": 12},
            {"site": "photostream", "bio": f"vault hint: {key}", "posts": 3},
            {"site": "microblog", "bio": "same avatar hash acbd1234", "posts": 88},
        ],
    }
    with open("/challenge/profiles.json", "w") as fh:
        json.dump(profiles, fh, indent=2)
    print("Username Pivot — same handle across profiles.json; bio on photostream has key.")


if __name__ == "__main__":
    main()
