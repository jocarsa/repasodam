import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conexion.commit()
conexion.close()