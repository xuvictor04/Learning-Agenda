# tools

Maintenance scripts for this repo.

- `check.py` — consistency check. Run `python3 tools/check.py` after any
  reorganisation: it verifies every internal link and heading anchor, that
  the 44 domains match across the map, the resource files, and the tracker,
  and that no placeholders or ragged tables slipped in. Exit code 1 on
  failure, so it works as a pre-commit hook if you want one.
