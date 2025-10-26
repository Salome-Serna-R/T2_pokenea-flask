import os
import random
from flask import Blueprint, jsonify, render_template
from .data import pokeneas

main = Blueprint('main', __name__)

# Ruta que devuelve un Pokenea aleatorio en JSON
@main.route("/api/pokenea", methods=["GET"])
def get_pokenea():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")  # Docker setea HOSTNAME automáticamente
    response = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": container_id
    }
    return jsonify(response)

# Ruta que muestra la imagen y frase aleatoria
@main.route("/", methods=["GET"])
def index():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")
    return render_template("index.html", pokenea=pokenea, container_id=container_id)
