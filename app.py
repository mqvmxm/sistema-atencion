import web
import models

# Definir las rutas del sistema
urls = (
    '/', 'Index',
    '/agregar', 'Agregar',
    '/atender', 'Atender',
    r'/quitar/(\d+)', 'Quitar'
)

render = web.template.render('templates/')
app = web.application(urls, globals())

class Index:
    def GET(self):
        estudiantes = models.obtener_todos()
        cantidad = models.obtener_cantidad()
        siguientes = models.obtener_siguientes()
        
        return render.index(estudiantes, cantidad, siguientes)

class Agregar:
    def POST(self):
        # Capturamos los datos, incluyendo el campo opcional 'otro_tramite'
        datos = web.input(tramite='', otro_tramite='')
        
        # Validamos cuál opción de trámite guardar
        tramite_final = datos.otro_tramite if datos.tramite == 'Otro' else datos.tramite
        
        models.agregar_estudiante(datos.matricula, datos.nombre, datos.carrera, tramite_final)
        
        # Redirección manual para entorno web/Codespaces
        web.header('Location', '/') 
        web.ctx.status = '303 See Other'
        return ''

class Atender:
    def POST(self):
        models.atender_estudiante()
        
        web.header('Location', '/') 
        web.ctx.status = '303 See Other'
        return ''

class Quitar:
    def POST(self, id_estudiante):
        models.quitar_estudiante(id_estudiante)
        
        web.header('Location', '/')
        web.ctx.status = '303 See Other'
        return ''

if __name__ == "__main__":
    app.run()