#!/usr/bin/env python3
"""Lightweight offline catalog validation."""
import json,re,sys
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
tools=json.loads((ROOT/"data/tools.json").read_text(encoding="utf-8"))
errors=[]; seen=set()
categories={"generation","analysis","validation","management","embedded"}
for tool in tools:
    name=tool.get("name","?")
    for key in ("id","name","category","model","description","use_case","url","source"):
        if not tool.get(key): errors.append(f"{name}: missing {key}")
    ident=tool.get("id","")
    if ident in seen:errors.append(f"Duplicate ID: {ident}")
    seen.add(ident)
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",ident): errors.append(f"Invalid ID: {ident}")
    if tool.get("category") not in categories:errors.append(f"Invalid category: {name}")
    if tool.get("model") not in ("Open source","Commercial"):errors.append(f"Invalid model: {name}")
    for key in ("url","source"):
        u=urlparse(tool.get(key,""))
        if u.scheme!="https" or not u.netloc:errors.append(f"Invalid URL: {name} {key}")
if len(tools)<25:errors.append("Fewer than 25 tools")
if tools[0].get("id")!="pca-cervus":errors.append("PCA CERVUS must be listed first")
if len(tools[0].get("profile",{}).get("capabilities",[]))<5:errors.append("PCA profile incomplete")
if errors:print("\n".join(errors),file=sys.stderr);sys.exit(1)
print(f"Valid catalog: {len(tools)} tools, PCA CERVUS first.")
