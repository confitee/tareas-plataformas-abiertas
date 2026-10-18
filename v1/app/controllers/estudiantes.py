from flask import Blueprint, jsonify, request

estudiantes_endpoints = Blueprint("estudiantes_endpoints", __name__)


@estudiantes_endpoints.get("/")
def bienvenida_api():
    """Endpoint adicional de bienvenida general para completar los tres pedidos."""
    return jsonify({"mensaje": "Bienvenido a la API de estudiantes"}), 200


@estudiantes_endpoints.get("/hola")
def hola():
    return jsonify({"mensaje": "Hola, bienvenido a la API de estudiantes"}), 200


@estudiantes_endpoints.get("/saludo")
def saludar():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre") or request.args.get("nombre")

    if not nombre or not str(nombre).strip():
        return jsonify({"mensaje": "Debe de ingresar el nombre del estudiante."}), 400

    return jsonify({"saludo": f"Hola {str(nombre).strip()}"}), 200
