from pymongo import MongoClient
from pymongo import DESCENDING

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]



resultado = coleccion.find().sort("edad", DESCENDING)
for doc in resultado:
    print(doc)