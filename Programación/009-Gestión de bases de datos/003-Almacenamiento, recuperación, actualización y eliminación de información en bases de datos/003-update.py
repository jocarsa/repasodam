import sqlite3

conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()

cursor.execute('''
UPDATE clientes SET nombre = 'Juan'
               WHERE nombre = 'Jose Vicente' 
''')

conexion.commit()
conexion.close()