from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

coleccion.delete_many({"activo": False})