"""Parse fandom wikitext tables (with rowspan) from raw JSON files. Usage: parse.py RAWDIR OUTJSON"""
import json, re, sys, os

RAW, OUT = sys.argv[1], sys.argv[2]

def wt(fn):
    with open(os.path.join(RAW, fn), encoding='utf-8', errors='replace') as f:
        return json.load(f)['parse']['wikitext']

def clean(s):
    s = re.sub(r"\[\[(?:File|Image):[^\]]*\]\]", "", s)
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s).replace("'''", "").replace("''", "")
    s = s.replace("�", "'")
    return re.sub(r"\s+", " ", s).strip()

def parse(fn):
    text = wt(fn)
    out = []
    episode = None
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^===\s*(.*?)\s*===\s*$", ln)
        if m:
            episode = clean(m.group(1))
        if ln.startswith("{|"):
            headers, rows, cur = [], [], None
            i += 1
            while i < len(lines) and not lines[i].startswith("|}"):
                l = lines[i]
                if l.startswith("!"):
                    headers.append(clean(l[1:]))
                elif l.startswith("|-"):
                    if cur is not None: rows.append(cur)
                    cur = []
                elif l.startswith("|"):
                    if cur is None: cur = []
                    cur.append(l[1:])
                i += 1
            if cur is not None: rows.append(cur)
            ncol = len(headers)
            carry = {}  # col -> [remaining, value]
            for r in rows:
                vals = {}
                cells = list(r)
                for c in range(ncol):
                    if c in carry and carry[c][0] > 0:
                        vals[headers[c]] = carry[c][1]; carry[c][0] -= 1; continue
                    if not cells: vals[headers[c]] = ""; continue
                    cell = cells.pop(0)
                    rs = 1
                    mm = re.match(r'\s*rowspan="(\d+)"\s*\|(.*)$', cell)
                    if mm:
                        rs = int(mm.group(1)); cell = mm.group(2)
                    v = clean(cell)
                    vals[headers[c]] = v
                    if rs > 1: carry[c] = [rs - 1, v]
                vals["_episode"] = episode
                out.append(vals)
        i += 1
    return out

files = {"pages": "p1.json", "thermos": "p2.json", "clocks": "p3.json", "tv": "p4.json",
         "radio": "p5.json", "chests": "p6.json", "cans": "p7.json", "signs": "p8.json", "nsgames": "p10.json"}
res = {k: parse(v) for k, v in files.items()}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, len(v))
