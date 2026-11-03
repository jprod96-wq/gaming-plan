import sys,json,urllib.request,urllib.parse,time,re,os
sys.stdout.reconfigure(encoding='utf-8')
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
out=sys.argv[1]
for t in sys.argv[2:]:
    fn=os.path.join(out,re.sub(r'[^A-Za-z0-9]+','_',t)+'.txt')
    if os.path.exists(fn): continue
    u="https://control.fandom.com/api.php?action=parse&format=json&formatversion=2&prop=wikitext&redirects=1&page="+urllib.parse.quote(t)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30))
        open(fn,'w',encoding='utf-8').write(d['parse']['wikitext'])
        print('ok',t)
    except Exception as e: print('ERR',t,e)
    time.sleep(1.5)
