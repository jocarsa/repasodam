from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

resultado = coleccion.find({
    "$or": [
        {"ciudad": "Madrid"},
        {"ciudad": "Valencia"}
    ]
})
for doc in resultado:
    print(doc)