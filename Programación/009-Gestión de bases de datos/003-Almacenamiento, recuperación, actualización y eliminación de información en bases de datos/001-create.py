import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute('''
 INSERT INTO clientes (nombre, apellido, email) VALUES
 ('Jose Vicente', 'Carratala', 'info@jocarsa.com')
''')
conexion.commit()
conexion.close()