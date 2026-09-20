import sqlite3

# Conectar a la base de datos (se creará automáticamente si no existe)
conn = sqlite3.connect('escuela.db')
cursor = conn.cursor()

# Crear la tabla 'fila'
# El 'id' autoincrementable es clave: nos asegura el principio de Primeras Entradas, Primeras Salidas
cursor.execute('''
CREATE TABLE IF NOT EXISTS fila (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    nombre TEXT NOT NULL,
    carrera TEXT NOT NULL,
    tramite TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Base de datos y tabla 'fila' creadas exitosamente.")