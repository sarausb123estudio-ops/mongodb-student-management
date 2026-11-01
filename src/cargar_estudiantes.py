
import json
from pathlib import Path
from pymongo import MongoClient

# 1. EXTRACT: Leer los datos del archivo JSON
ruta = Path(__file__).resolve().parent.parent / "data" / "estudiantes.json"

with open(ruta, "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("Datos extraídos:", len(datos))

# 2. TRANSFORM: Convertir las carreras a mayúsculas
estudiantes_limpios = []

for estudiante in datos:
    estudiantes_limpios.append({
        "nombre": estudiante["nombre"],
        "semestre": estudiante["semestre"],
        "carrera": estudiante["carrera"].upper()
    })

print("Datos transformados:", len(estudiantes_limpios))

# 3. LOAD: Cargar los datos transformados en MongoDB
cliente = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=5000
)

try:
    cliente.admin.command("ping")

    base_datos = cliente["universidad"]
    coleccion = base_datos["estudiantes_transformados"]

    # Evitar nombres duplicados en los datos de práctica
    coleccion.create_index("nombre", unique=True)

    insertados = 0
    actualizados = 0

    for estudiante in estudiantes_limpios:
        resultado = coleccion.update_one(
            {"nombre": estudiante["nombre"]},
            {"$set": estudiante},
            upsert=True
        )

        if resultado.upserted_id is not None:
            insertados += 1
        elif resultado.modified_count > 0:
            actualizados += 1

    print("Estudiantes insertados:", insertados)
    print("Estudiantes actualizados:", actualizados)
    print("Total en MongoDB:", coleccion.count_documents({}))

finally:
    cliente.close()
