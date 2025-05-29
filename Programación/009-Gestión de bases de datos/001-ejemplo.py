from pymongo import MongoClient
from datetime import datetime

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["miempresa"]
coleccion = db["clientes"]

documento = {
    "nombre": "Pedro",
    "edad": 38,
    "activo": True,
    "peso": 74.2,
    "fecha_registro": datetime.now(),
    "etiquetas": ["premium", "newsletter"],
    "direccion": {
        "calle": "Mayor",
        "ciudad": "Valencia",
        "cp": "46001"
    },
    "telefono": None
}

coleccion.insert_one(documento)
print("Documento con múltiples tipos insertado.")
