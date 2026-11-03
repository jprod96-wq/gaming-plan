import sys,re,glob,os
sys.stdout.reconfigure(encoding='utf-8')
for fn in sorted(glob.glob(os.path.join(sys.argv[1],'*.txt'))):
    if len(sys.argv)>2 and not any(a in fn for a in sys.argv[2:]): continue
    t=open(fn,encoding='utf-8').read()
    print('####',os.path.basename(fn))
    m=re.search(r'\{\{\s*Mission.*?\n\}\}',t,re.S|re.I)
    box=m.group(0) if m else t[:600]
    box=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',box); box=re.sub(r'\{\{rarity\|[^}]*text=([^}]*)\}\}',r'\1',box)
    box=re.sub(r'\n\|image.*|\n\|caption.*','',box)
    print(box[:900])
    o=re.search(r'==\s*Obtaining\s*==(.*?)\n==',t,re.S)
    if o: print('OBTAIN:',re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',o.group(1).strip())[:500])
