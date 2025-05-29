from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

resultado = coleccion.find({"edad": {"$gt": 30}})
for doc in resultado:
    print(doc)
