import sqlite3 # Importa la librería nativa de Python para trabajar con bases de datos SQLite.

# 1. Conexión: Se conecta al archivo de la base de datos llamado 'escuela.db'.
# Si el archivo no existe en la misma carpeta, SQLite lo crea automáticamente.
conn = sqlite3.connect('escuela.db')
cursor = conn.cursor()

# 3. Creación de la tabla 'fila':
# Ejecuta una sentencia SQL para definir la estructura de la tabla si no ha sido creada previamente.
# - id: Clave primaria numérica autoincrementable. Garantiza el orden estricto de llegada (FIFO / Queue).
# - matricula, nombre, carrera, tramite: Campos de texto obligatorios (NOT NULL) para los datos del alumno
cursor.execute('''
CREATE TABLE IF NOT EXISTS fila (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL,
    nombre TEXT NOT NULL,
    carrera TEXT NOT NULL,
    tramite TEXT NOT NULL
)
''')
# 4. Guardar cambios: Aplica permanentemente la creación de la tabla en el archivo 'escuela.db'.
conn.commit()
# 5. Cerrar conexión: Libera la base de datos para evitar bloqueos de archivo.
conn.close()
# Confirmación en la consola del desarrollador
print("Base de datos y tab la 'fila' creadas exitosamente.")