from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

resultados = coleccion.find({"edad": {"$gt": 25}})  # edad > 25
for doc in resultados:
    print(doc)