import xml.etree.ElementTree as ET
import json

# Cargar XML
arbol = ET.parse("blog.xml")
raiz = arbol.getroot()

# Convertir a estructura Python
posts = []
for post in raiz.findall("post"):
    item = {
        "titulo": post.findtext("titulo"),
        "fecha": post.findtext("fecha"),
        "autor": post.findtext("autor"),
        "categorias": [cat.text for cat in post.find("categorias").findall("categoria")],
        "contenido": post.findtext("contenido")
    }
    posts.append(item)

# Guardar como JSON
with open("blog.json", "w", encoding="utf-8") as f:
    json.dump({"blog": posts}, f, ensure_ascii=False, indent=2)

