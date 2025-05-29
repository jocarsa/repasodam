from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

resultado = coleccion.find({"nombre": "Jose"})
for doc in resultado:
    print(doc)

