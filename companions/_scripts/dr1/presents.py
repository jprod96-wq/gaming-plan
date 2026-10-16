import re,sys,glob,os
for f in sorted(glob.glob(os.path.join(sys.argv[1],'fte_*.txt'))):
    t=open(f,encoding='utf-8').read()
    out=[os.path.basename(f)]
    for k in ('Loves','Likes'):
        m=re.search(r"'''"+k+r":'''\s*\n\|[^|]*\|(.*)",t)
        out.append(k+': '+(m.group(1).strip() if m else 'NONE'))
    m=re.search(r"==Skills Granted==(.*?)\n==",t,re.S)
    if m: out.append('SK: '+' / '.join(re.findall(r"'''(.*?)'''",m.group(1))))
    print('\n'.join(out))
