from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

coleccion.update_one(
    {"nombre": "Jose"},                      # filtro
    {"$set": {"ciudad": "Alicante"}}         # cambio
)