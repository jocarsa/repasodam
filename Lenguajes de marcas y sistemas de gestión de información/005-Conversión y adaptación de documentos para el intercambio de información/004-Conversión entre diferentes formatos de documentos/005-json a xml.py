from xml.etree.ElementTree import Element, SubElement, ElementTree

raiz = Element("blog")
for post in posts:
    nodo = SubElement(raiz, "post")
    SubElement(nodo, "titulo").text = post["titulo"]
    SubElement(nodo, "fecha").text = post["fecha"]
    SubElement(nodo, "autor").text = post["autor"]
    categorias = SubElement(nodo, "categorias")
    for c in post["categorias"]:
        SubElement(categorias, "categoria").text = c
    SubElement(nodo, "contenido").text = post["contenido"]

arbol = ElementTree(raiz)
arbol.write("blog_convertido.xml", encoding="utf-8", xml_declaration=True)

