# Username Pivot (`username-pivot`)

**Category:** osint · **Difficulty:** easy · **Points:** 200

One reused handle links accounts; a pinned post exposes the flag blob (base64).

## Run it

```bash
docker build -t sparflag/username-pivot .
# `deca-ai start username-pivot` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is base64-encoded. Decode it to recover the flag.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit username-pivot 'sparflag{...}'
```

## Hints

- The same username appears across sites.
- The pinned post's text decodes from base64.
