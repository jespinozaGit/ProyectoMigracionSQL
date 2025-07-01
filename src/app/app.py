#!/usr/bin/env python3
from flask import Flask, jsonify, request
import os
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Carga la URL de la base de datos desde .env (docker-compose env_file)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("La variable DATABASE_URL no está definida")

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, future=True)

@app.route("/compras", methods=["GET"])
def list_compras():
    with engine.connect() as conn:
        # Sólo seleccionamos nombre y fecha_caducidad
        rows = conn.execute(text(
            "SELECT nombre, fecha_caducidad FROM tCompras"
        )).mappings().all()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/compras", methods=["POST"])
def create_compra():
    """Inserta una nueva compra y devuelve su ID."""
    data = request.get_json(force=True)
    # Validación mínima
    if not data.get("nombre") or not data.get("fecha_caducidad"):
        return jsonify({"error": "Campos 'nombre' y 'fecha_caducidad' requeridos"}), 400

    stmt = text(
        "INSERT INTO tCompras (nombre, fecha_caducidad) "
        "VALUES (:n, :f); SELECT SCOPE_IDENTITY() AS id"
    )
    try:
        with engine.begin() as conn:
            result = conn.execute(stmt, {
                "n": data["nombre"],
                "f": data["fecha_caducidad"]
            })
            new_id = result.scalar()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    response = {
        "id": new_id,
        "nombre": data["nombre"],
        "fecha_caducidad": data["fecha_caducidad"]
    }
    return jsonify(response), 201

if __name__ == "__main__":
    # Permite cambiar el puerto vía .env (por defecto 5000)
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
