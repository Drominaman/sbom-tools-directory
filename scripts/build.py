#!/usr/bin/env python3
"""Rebuild the static site and CSV from the canonical data/tools.json."""
import argparse,csv,io,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument("--check", action="store_true")
a=p.parse_args()
data=json.loads((ROOT/"data/tools.json").read_text(encoding="utf-8"))
pattern=r'(window\\.SBOM_TOOLS\\s*=\\s*)\\[[\\s\\S]*?\\](;?\\s*</script>)'
template=(ROOT/"templates/index.html").read_text(encoding="utf-8")
blob=json.dumps(data, ensure_ascii=False, separators=(",",":"))
site,count=re.subn(pattern,lambda m:m.group(1)+blob+m.group(2),template,count=1)
if count!=1:raise SystemExit("Cannot find catalog in site template")
buf=io.StringIO(newline="")
cols=["name","category","model","description","use_case","url","source"]
w=csv.DictWriter(buf,fieldnames=cols,lineterminator="\\n")
w.writeheader()
for record in data:w.writerow({key:record.get(key,"") for key in cols})
outputs={"docs/index.html":site,"docs/tools.csv":buf.getvalue()}
changed=[]
for dest,contents in outputs.items():
    path=ROOT/dest
    if not path.exists() or path.read_text(encoding="utf-8")!=contents:
        changed.append(dest)
        if not a.check:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(contents,encoding="utf-8")
if changed:
    print(("Outdated: " if a.check else "Updated: ")+", ".join(changed))
else:print("Site and CSV match catalog")
if changed and a.check:raise SystemExit(1)
