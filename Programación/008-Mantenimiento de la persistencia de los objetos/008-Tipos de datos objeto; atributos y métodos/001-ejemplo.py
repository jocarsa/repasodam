from pymongo import MongoClient
from bson.objectid import ObjectId

cliente = MongoClient("mongodb://localhost:27017/")
coleccion = cliente["miempresa"]["clientes"]

# Recuperar un documento y mostrar sus atributos
doc = coleccion.find_one({"nombre": "Lucía"})

if doc:
    print("ID:", doc["_id"])
    print("Nombre:", doc["nombre"])
    print("Edad:", doc["edad"])
    print("Ciudad:", doc.get("ciudad", "No especificada"))

    # Comprobación de tipo
    print("¿Es un ObjectId?", isinstance(doc["_id"], ObjectId))