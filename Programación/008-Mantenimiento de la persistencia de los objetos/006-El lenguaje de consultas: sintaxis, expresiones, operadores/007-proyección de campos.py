from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

resultado = coleccion.find(
    {},  # sin filtro
    {"_id": 0, "nombre": 1, "ciudad": 1}
)
for doc in resultado:
    print(doc)