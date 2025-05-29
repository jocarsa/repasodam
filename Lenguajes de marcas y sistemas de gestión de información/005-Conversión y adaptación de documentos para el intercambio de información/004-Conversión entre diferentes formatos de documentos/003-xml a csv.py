import csv

# Reutilizamos la lista `posts` del ejemplo anterior
with open("blog.csv", "w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Titulo", "Fecha", "Autor", "Categorias", "Contenido"])
    for post in posts:
        categorias = ", ".join(post["categorias"])
        escritor.writerow([post["titulo"], post["fecha"], post["autor"], categorias, post["contenido"]])

