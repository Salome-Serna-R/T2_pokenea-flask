# Archivo para crear las rutas de la aplicación
# /api/pokenea: retorna JSON con info básica + ID del contenedor.
# /: muestra imagen y frase filosófica + ID del contenedor.
from flask import Blueprint, jsonify, render_template
from .data import pokeneas 

main = Blueprint('main', __name__)

@main.route("/api/pokenea", methods=["GET"])
def get_pokeneas():
    return jsonify(pokeneas)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html", pokeneas=pokeneas)
