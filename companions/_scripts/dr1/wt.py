import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f,encoding='utf-8'))
    t=d.get('parse',{}).get('wikitext',str(d))
    open(f[:-5]+'.txt','w',encoding='utf-8').write(t)
