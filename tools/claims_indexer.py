#!/usr/bin/env python3
"""
Claims Indexer
- Scans deepresearch outputs and merges any *.jsonl claims into consolidated files
- Cases supported:
  * ledger-rwa-worldwide-ru-cfa -> co-76ca/claims/ledger.claims.jsonl
  * cfa-platforms-ru-2024-2025  -> co-76ca/claims/cfa_ru.claims.jsonl

Usage:
  python3 tools/claims_indexer.py
"""
import os, sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_DIR = ROOT/"memory-bank/Scrum/20251030-jump-into-project/co-76ca/claims"

CASES = {
    'ledger': {
        'match': '00-Ledger-RWA-platforms-worldwide-and-RU-CFA-deepresearches',
        'outfile': OUT_DIR/"ledger.claims.jsonl",
    },
    'cfa_ru': {
        'match': '01-CFA-platforms-RU-2024-2025',
        'outfile': OUT_DIR/"cfa_ru.claims.jsonl",
    }
}

SEARCH_DIRS = [
    ROOT/"memory-bank/Scrum/20251030-jump-into-project/deepresearches",
    ROOT/"memory-bank/Scrum/20251030-jump-into-project/co-76ca/deepresearch-pipelines",
]

def iter_jsonl_files():
    for base in SEARCH_DIRS:
        if not base.exists():
            continue
        for dirpath, _, filenames in os.walk(base):
            for fn in filenames:
                if fn.endswith('.jsonl'):
                    yield pathlib.Path(dirpath)/fn

def classify(path: pathlib.Path):
    sp = str(path)
    for key, meta in CASES.items():
        if meta['match'] in sp:
            return key
    return None

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    buckets = {k: [] for k in CASES}
    for p in iter_jsonl_files():
        key = classify(p)
        if key:
            buckets[key].append(p)
    for key, files in buckets.items():
        if not files:
            continue
        out = CASES[key]['outfile']
        with out.open('w', encoding='utf-8') as w:
            for f in sorted(files):
                for line in f.open('r', encoding='utf-8'):
                    line = line.strip()
                    if not line:
                        continue
                    # Minimal validation: must be JSON object
                    try:
                        obj = json.loads(line)
                    except Exception:
                        continue
                    w.write(json.dumps(obj, ensure_ascii=False)+"\n")
    # Write index file
    index = {
        'ledger': [str(p) for p in buckets['ledger']],
        'cfa_ru': [str(p) for p in buckets['cfa_ru']],
    }
    (OUT_DIR/"claims.index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2))
    print("Indexed:", {k: len(v) for k,v in index.items()})

if __name__ == '__main__':
    sys.exit(main())

