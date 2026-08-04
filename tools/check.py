#!/usr/bin/env python3
"""Consistency check for this repo.

Run from anywhere:  python3 tools/check.py

Verifies that every internal link and backticked path resolves, that every
heading anchor referenced actually exists, that the 44 domains in the map
match the resource files and the tracker, and that no placeholders or
malformed tables slipped in. Written to be run after any reorganisation --
this repo is meant to be edited for seventy years, and links rot.
"""
import os, re, sys, glob

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
fails, warns = [], []

md = sorted(f for f in glob.glob('**/*.md', recursive=True) if '.git' not in f)

# 1. internal links resolve
for f in md:
    s = open(f).read()
    base = os.path.dirname(f)
    for link in re.findall(r'\]\(([^)\s]+?)(?:#[^)]*)?\)', s):
        # same-file anchors (#foo) are checked by the anchor pass below
        if not link or link.startswith(('http', 'mailto:', '#')): continue
        if re.search(r'log/\d{4}-(review|plan|weekly)\.md', link): continue  # future logs
        target = os.path.normpath(os.path.join(base, link.rstrip('/')))
        if not os.path.exists(target):
            fails.append(f"broken link: {f} -> {link}")

# 2. backticked repo paths resolve
for f in md:
    s = open(f).read()
    for p in re.findall(r'`((?:[a-z0-9-]+/)?[0-9A-Za-z_.-]+\.md)`', s):
        if re.search(r'log/\d{4}-(review|plan|weekly)\.md', p): continue  # future logs
        if '<year>' in p: continue
        cands = [p, os.path.normpath(os.path.join(os.path.dirname(f), p)),
                 os.path.basename(p)]
        cands += glob.glob(f'**/{os.path.basename(p)}', recursive=True)
        if not any(os.path.exists(c) for c in cands):
            fails.append(f"bad path ref: {f} -> {p}")

# 3. the 44 domains, everywhere they should appear
mapf = open('02-map.md').read()
ledger = re.findall(r'^- \[[ x]\] (.+)$', mapf, re.M)
domains = [d for d in ledger if 'language' not in d.lower()]
if len(domains) != 44:
    fails.append(f"map has {len(domains)} domains, expected 44")

# every domain has a long shelf in its cluster file
clusters = ['formal','physical','living','mind','human-social',
            'meaning-expression','made-applied']
tot_h, tot_s = 0, 0
for c in clusters:
    s = open(f'resources/{c}.md').read()
    h = len(re.findall(r'^## ', s, re.M))
    sh = s.count('Beyond T1 — the long shelf')
    tot_h += h; tot_s += sh
    if h != sh:
        fails.append(f"resources/{c}.md: {h} domains but {sh} long shelves")
if tot_h != 44:
    fails.append(f"resource files hold {tot_h} domains, expected 44")

# tracker carries every domain
tr = open('log/tracker.md').read()
missing = [d for d in domains
           if d.split('(')[0].strip().split(' — ')[0][:28] not in tr]
if missing:
    fails.append(f"tracker missing {len(missing)}: {missing[:3]}")

# 4. no age references
AGE = re.compile(r'ages? \d|at (?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\b(?![- ]year|[- ]percent|-(?:one|two|three|four|five|six|seven|eight|nine)| of )'
                 r'|your (?:twenties|thirties|forties|fifties|sixties|seventies|eighties)'
                 r'|half your age|\d+ years old|aged \d')
for f in md:
    for i, line in enumerate(open(f), 1):
        if AGE.search(line) and '$' not in line and 'a month' not in line:
            fails.append(f"age ref: {f}:{i}: {line.strip()[:70]}")

# 4b. anchor links resolve to real headings
def slug(h):
    h = h.strip().lower()
    h = re.sub(r'[`*_]', '', h)
    h = re.sub(r'[^\w\s-]', '', h)
    return re.sub(r'\s', '-', h).strip('-')

heads = {}
for f in md:
    heads[f] = {slug(m) for m in re.findall(r'^#{1,6}\s+(.+)$', open(f).read(), re.M)}

for f in md:
    s2 = open(f).read()
    base = os.path.dirname(f)
    for link, anc in re.findall(r'\]\(([^)#\s]*)#([^)\s]+)\)', s2):
        tgt = f if not link else os.path.normpath(os.path.join(base, link))
        if tgt in heads and anc.lower() not in heads[tgt]:
            fails.append(f"dead anchor: {f} -> {link}#{anc}")

# 5. leftover placeholders
for f in md:
    s = open(f).read()
    if f.endswith(('02-map.md',)) or f.startswith('templates/'):
        continue  # blanks are intentional here
    for tok in ['_TODO_', 'TODO:', 'FIXME', 'XXX', 'Lorem ipsum']:
        if tok in s:
            warns.append(f"placeholder {tok} in {f}")

# 6. mermaid blocks balanced
for f in md:
    s = open(f).read()
    if s.count('```mermaid') and s.count('```') % 2:
        fails.append(f"unbalanced code fence in {f}")

# 7. markdown tables have consistent column counts
for f in md:
    rows, start = [], 0
    for i, line in enumerate(open(f), 1):
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not rows: start = i
            rows.append((i, line.count('|')))
        else:
            if len(rows) >= 2:
                widths = {w for _, w in rows}
                if len(widths) > 1:
                    warns.append(f"ragged table {f}:{start} widths={sorted(widths)}")
            rows = []

print("=" * 60)
print(f"files: {len(md)}   lines: {sum(len(open(f).readlines()) for f in md)}")
print(f"domains in map: {len(domains)}   long shelves: {tot_s}/{tot_h}")
print("=" * 60)
if fails:
    print(f"\nFAIL ({len(fails)}):")
    for x in fails[:40]: print("  ", x)
else:
    print("\nno failures")
if warns:
    print(f"\nwarn ({len(warns)}):")
    for x in warns[:25]: print("  ", x)
sys.exit(1 if fails else 0)
