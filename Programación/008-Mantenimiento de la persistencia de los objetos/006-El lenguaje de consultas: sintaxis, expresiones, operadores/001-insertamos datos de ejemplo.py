from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
basedatos = cliente["miempresa"]
coleccion = basedatos["clientes"]

# Elimina los datos anteriores si los hubiera
coleccion.delete_many({})

# Inserta un bloque de datos
datos = [
    {"nombre": "Jose", "edad": 30, "ciudad": "Valencia", "activo": True},
    {"nombre": "Ana", "edad": 22, "ciudad": "Madrid", "activo": True},
    {"nombre": "Luis", "edad": 45, "ciudad": "Valencia", "activo": False},
    {"nombre": "Lucía", "edad": 33, "ciudad": "Barcelona", "activo": True},
    {"nombre": "Carlos", "edad": 25, "ciudad": "Sevilla", "activo": False},
    {"nombre": "Marta", "edad": 29, "ciudad": "Madrid", "activo": True}
]

coleccion.insert_many(datos)
print("Documentos insertados.")
