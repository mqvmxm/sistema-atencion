import sqlite3

def get_db(): # funcion para cada que se requiera abrir el archivo de la base de datos
    conn = sqlite3.connect('escuela.db') #crea o abre la base de datos
    conn.row_factory = sqlite3.Row  # permite acceder a los datos por columna en lugar de obtener posicion
    return conn 

def obtener_todos(): # recupera la lista completa de alumnos formados
    conn = get_db()
    cursor = conn.cursor() #recibe y ejecuta
    cursor.execute("SELECT * FROM fila ORDER BY id ASC") # asegura a los primeros de la fila
    estudiantes = cursor.fetchall() # toma el resultado completo
    conn.close()
    return estudiantes

def obtener_siguientes():
    conn = get_db()
    cursor = conn.cursor()
    # Traemos hasta 3 estudiantes para mostrar los próximos turnos
    cursor.execute("SELECT * FROM fila ORDER BY id ASC LIMIT 3")
    siguientes = cursor.fetchall()
    conn.close()
    return siguientes

def obtener_cantidad():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM fila") # contar la cantidad de filas que hay en la tabla
    cantidad = cursor.fetchone()[0] # extrae el primer resultado 
    conn.close()
    return cantidad

def agregar_estudiante(matricula, nombre, carrera, tramite):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO fila (matricula, nombre, carrera, tramite) VALUES (?, ?, ?, ?)",
        (matricula, nombre, carrera, tramite)
    )
    conn.commit()
    conn.close()

def atender_estudiante():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM fila ORDER BY id ASC LIMIT 1") # ordena a los alumnos por ID para que traiga al primero
    primero = cursor.fetchone() # guarda esa fila en la variable
    
    if primero: # verificamos si habia alguien en la fila
        cursor.execute("DELETE FROM fila WHERE id = ?", (primero['id'],)) #
        conn.commit()
    conn.close()

def quitar_estudiante(id_estudiante):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fila WHERE id = ?", (id_estudiante,)) # es el numero a eliminar - dato suelto
    conn.commit()
    conn.close()