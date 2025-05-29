from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

for cliente in coleccion.find({}, {"_id": 0, "nombre": 1, "ciudad": 1}):
    print(cliente)