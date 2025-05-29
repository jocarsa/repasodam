from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]


resultado = coleccion.find({
    "activo": {"$exists": True}
})
for doc in resultado:
    print(doc)