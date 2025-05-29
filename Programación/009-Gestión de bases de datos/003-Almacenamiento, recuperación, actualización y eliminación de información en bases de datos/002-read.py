import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute('''
SELECT * FROM clientes
''')
registros = cursor.fetchall()
for registro in registros:
    print(f'ID: {registro[0]}, Nombre: {registro[1]}, Apellido: {registro[2]}, Email: {registro[3]}')
conexion.commit()
conexion.close()