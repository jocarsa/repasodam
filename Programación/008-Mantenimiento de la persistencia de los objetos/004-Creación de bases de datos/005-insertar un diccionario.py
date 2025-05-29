from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

basedatos = cliente["miempresa"]

coleccion = basedatos["clientes"]

documento = {"nombre": "Jose", "edad": 30}
coleccion.insert_one(documento)