import re,sys,glob
for i in range(1,17):
    t=open(f"{sys.argv[1]}/{i}.txt",encoding='utf-8').read()
    name=re.search(r'\|name\s*=\s*(.*)',t); loc=re.search(r'\|loc\s*=\s*(.*)',t)
    pelt=re.findall(r'\[\[(Legendary [^\]|]*(?:Pelt|Hide|Skin)[^\]|]*)',t)
    ls=re.search(r'==\s*Location\s*==\n(.*?)\n==',t,re.S)
    tr=re.search(r'===\s*\[*Trapper\]*\s*===\n(.*?)\|\}',t,re.S)
    print("#####",i,name and name.group(1)); print("LOC:",loc and loc.group(1)); print("PELT:",set(pelt))
    print("LOCSEC:",ls and ls.group(1).strip()[:600])
    print("TRAP:",tr and re.sub(r'!.*\n','',tr.group(1)).strip())
    m=re.search(r'appears in[^.]*\.|unlock[^.]*\.',t,re.I); print("UNL:",m and m.group(0))
