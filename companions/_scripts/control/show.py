import sys,json
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open(sys.argv[1],encoding='utf-8'))
print(d.get('parse',{}).get('wikitext',d))
