import json,sys
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open(sys.argv[1],encoding='utf-8'))
if 'parse' in d: print(d['parse']['wikitext'])
else: print(d)
