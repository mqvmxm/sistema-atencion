import sqlite3

def get_db():
    conn = sqlite3.connect('escuela.db')
    conn.row_factory = sqlite3.Row
    return conn

def obtener_todos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fila ORDER BY id ASC")
    estudiantes = cursor.fetchall()
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
    cursor.execute("SELECT COUNT(*) FROM fila")
    cantidad = cursor.fetchone()[0]
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
    cursor.execute("SELECT id FROM fila ORDER BY id ASC LIMIT 1")
    primero = cursor.fetchone()
    
    if primero:
        cursor.execute("DELETE FROM fila WHERE id = ?", (primero['id'],))
        conn.commit()
    conn.close()

def quitar_estudiante(id_estudiante):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fila WHERE id = ?", (id_estudiante,))
    conn.commit()
    conn.close()