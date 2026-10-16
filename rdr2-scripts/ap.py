import re,sys,json
t=open(sys.argv[1],encoding='utf-8').read()
out={}
for m in re.finditer(r"\|rowspan=\"?\d+\"?\|'''\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'''(.*)",t):
    name=(m.group(2) or m.group(1)).strip()
    desc=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',m.group(3)).replace('<br>',' ')
    out[name]=re.sub(r'\s+',' ',desc).strip()
json.dump(out,open(sys.argv[2],'w',encoding='utf-8'),indent=0,ensure_ascii=False)
for k,v in out.items(): print(k,'::',v[:260])
