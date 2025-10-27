import os, random, socket
from flask import Flask, jsonify, render_template_string
from data import pokeneas as POKENEAS_ORIG

HOSTNAME = socket.gethostname()
BUCKET = os.getenv("S3_BUCKET", "t2-pokeneas")
REGION = os.getenv("AWS_REGION", "us-east-1")
BASE = f"https://{BUCKET}.s3.{REGION}.amazonaws.com"

app = Flask(__name__)

def _normalize(item):
    img = item.get("imagen", "")
    if not img.startswith("http"):
        img = f"{BASE}/{img.lstrip('/')}"
    return {**item, "imagen": img}

POKENEAS = [_normalize(p) for p in POKENEAS_ORIG]

@app.get("/api/pokenea")
def api():
    p = random.choice(POKENEAS)
    return jsonify({**p, "container_id": HOSTNAME})

HTML = """<!doctype html>
<html><body style='font-family:sans-serif;text-align:center'>
<h1>{{nombre}} <small style="font-weight:400;color:#666">#{{id}}</small></h1>
<img src="{{imagen}}" style="max-height:55vh;border-radius:16px"><p><b>Altura:</b> {{altura}}
<br><b>Habilidad:</b> {{habilidad}}</p>
<p style="font-style:italic">“{{frase}}”</p>
<small>Container: {{cid}}</small></body></html>"""

@app.get("/ui")
def ui():
    p = random.choice(POKENEAS)
    return render_template_string(HTML, cid=HOSTNAME, **p)

@app.get("/")
def root():
    return jsonify({"ok": True, "routes": ["/api/pokenea","/ui"], "container_id": HOSTNAME})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
