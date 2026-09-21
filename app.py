import web
import models # importado desde models.py 

# definir el enrutamiento del sistema
urls = (
    '/', 'Index', # representa la clase Index (página principal)
    '/agregar', 'Agregar', # responsable de recibir los datos del formulario
    '/atender', 'Atender', # esta clase ejecuta el codigo para sacar al estudiante de la base de datos
    r'/quitar/(\d+)', 'Quitar' # r - texto crudo, d+ - cualquier numero, saber a que registro eliminar
)

render = web.template.render('templates/') # direccion para buscar la parte visual
app = web.application(urls, globals()) # urls - mapa de rutas, globals- función que entrega las clases

class Index:
    def GET(self): #get - pedir o consultar 
    # llama a la funcion de models.py para consultar informacion
        estudiantes = models.obtener_todos() 
        cantidad = models.obtener_cantidad()
        siguientes = models.obtener_siguientes()
        
        #esta informacion es la que encontramos en el index
        return render.index(estudiantes, cantidad, siguientes)

class Agregar:
    def POST(self): # para enviar datos
        # Capturamos los datos, incluyendo el campo opcional 'otro_tramite'
        datos = web.input(tramite='', otro_tramite='')
        
        # validamos cual opción de trámite guardar
        tramite_final = datos.otro_tramite if datos.tramite == 'Otro' else datos.tramite
        
        models.agregar_estudiante(datos.matricula, datos.nombre, datos.carrera, tramite_final)
        
        # Redirección e instruccion de estado
        web.header('Location', '/') 
        web.ctx.status = '303 See Other'
        return ''

class Atender:
    def POST(self): # cambio 
        models.atender_estudiante() # busca al id mas antiguo
        
        web.header('Location', '/') 
        web.ctx.status = '303 See Other'
        return ''

class Quitar:
    def POST(self, id_estudiante): # toma el id del estudiante a quitar
        models.quitar_estudiante(id_estudiante) # ejecuta el delete
        
        web.header('Location', '/')
        web.ctx.status = '303 See Other'
        return ''

if __name__ == "__main__": # funcion predeterminada, app.py convierte en main
    app.run() 