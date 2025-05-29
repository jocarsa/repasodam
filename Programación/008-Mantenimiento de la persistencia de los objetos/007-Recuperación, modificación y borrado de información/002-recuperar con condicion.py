for cliente in coleccion.find({"edad": {"$gt": 30}}):
    print(cliente)