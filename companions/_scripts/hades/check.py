import json,sys
s=open(sys.argv[1],encoding="utf-8").read()
assert s.startswith("const COMPANION = ") and s.rstrip().endswith(";") and s.count("const ")==1
d=json.loads(s[len("const COMPANION = "):].rstrip().rstrip(";"))
print("parsed ok", [ (x["id"],len(x["items"])) for x in d["sections"]])
