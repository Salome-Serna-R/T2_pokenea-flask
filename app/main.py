import os, random, socket
from flask import Flask, jsonify, render_template_string
HOSTNAME = socket.gethostname()
BUCKET = os.getenv("S3_BUCKET", "t2-pokeneas")    # <-- tu bucket en S3
REGION = os.getenv("AWS_REGION", "us-east-1")
BASE = f"https://{BUCKET}.s3.{REGION}.amazonaws.com"

POKENEAS = [
    {"nombre":"001","img":f"{BASE}/001.png","frase":"¡Hágale pues!"},
    {"nombre":"002","img":f"{BASE}/002.png","frase":"Con toda."},
    {"nombre":"003","img":f"{BASE}/003.png","frase":"Despacio pero seguro."},
    {"nombre":"004","img":f"{BASE}/004.png","frase":"Berraquera pura."},
    {"nombre":"007","img":f"{BASE}/007.png","frase":"Qué chimba."},
    {"nombre":"010","img":f"{BASE}/010.png","frase":"Se hace y ya."},
    {"nombre":"011","img":f"{BASE}/011.png","frase":"De una."},
    {"nombre":"012","img":f"{BASE}/012.png","frase":"Pues claro."},
]

app = Flask(__name__)

@app.get("/api/pokenea")
def api():
    p = random.choice(POKENEAS)
    return jsonify({"nombre": p["nombre"], "frase": p["frase"], "img": p["img"], "container_id": HOSTNAME})

HTML = """<!doctype html><html><body style='font-family:sans-serif;text-align:center'>
<h1>{{n}}</h1><img src="{{img}}" style="max-height:55vh;border-radius:16px"><p>{{f}}</p>
<small>Container: {{cid}}</small></body></html>"""

@app.get("/ui")
def ui():
    p = random.choice(POKENEAS)
    return render_template_string(HTML, n=p["nombre"], img=p["img"], f=p["frase"], cid=HOSTNAME)

@app.get("/")
def root():
    return jsonify({"ok": True, "routes": ["/api/pokenea","/ui"], "container_id": HOSTNAME})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
