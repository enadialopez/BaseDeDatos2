class MaquinaVirtual:

    def __init__(self, tabla):
        self.tabla = tabla
    
    def ejecutarMetacomando(self, query):
        #Eejecuta metacomando de sql
        match query:
            case ".exit":
                print("Terminado")
                exit()
            case ".table-metadata":
                print("Paginas")
            case default:
                print(query + " no es un comando valido")

    def ejecutarSentenciaSQL(self, query):
        #Ejecuta las sentencias SELECT E INSERT de sql
        sentencia = query.upper()
        if sentencia.startswith("SELECT"):
            self.obtenerTodosRegistros()
        elif sentencia.startswith("INSERT"):
            self.insertarRegistros(sentencia) 
        else:
            print(sentencia + " no es una sentencia valida")

    def obtenerTodosRegistros(self):
        #Muestra los registro que existe en una tabla
        return self.tabla.obtenerTodosLosRegistros()

    def insertarRegistros(self, registro):
        #Inseta los nuevos datos a la tabla
        if self.registroEsValido(registro):
            self.tabla.guardarRegistroEnPagina(registro)
            print("INSERT exitoso")
            
    def registroEsValido(self, datosAGuardar):
        dato = datosAGuardar[7:]
        cantidadDeDatos = len(dato.split(" "))
        return (cantidadDeDatos == 3 )
