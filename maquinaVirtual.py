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
            self.obtenerTodosRegistrosDeserializados()
        elif sentencia.startswith("INSERT"):
            self.insertarRegistros(sentencia) 
        else:
            print(sentencia + " no es una sentencia valida")

    def obtenerTodosRegistrosDeserializados(self):
        #Muestra los registro que existe en una tabla
        registros = self.tabla.obtenerTodosLosRegistros()
        registrosDeserializados = ""
        for registro in registros:
            registrosDeserializado = self.deserializar(registro)
            registrosDeserializados += registrosDeserializado
        print(registrosDeserializados)
        return registrosDeserializados
    
    def deserializar(self, registro):
        idEnBytes = registro[:4]
        nombreEnBytes = registro[4:36]
        emailEnBytes = registro[36:]

        id = self.deserializarId(idEnBytes)
        nombre = self.deserializarString(nombreEnBytes)
        email = self.deserializarString(emailEnBytes)
        return id + " " + nombre + " " + email + "\n"

    def deserializarId(self, id):
        numId = int.from_bytes(id, byteorder="big")
        return str(numId)

    def deserializarString(self, bytes):
        posicionFinalDatos = bytes.find(b'\x00')
        datosEnBytes = bytes[:posicionFinalDatos]
        return str(datosEnBytes, 'ascii')

    def insertarRegistros(self, registro):
        #Inseta los nuevos datos a la tabla
        if self.registroEsValido(registro):
            self.tabla.guardarRegistroEnPagina(registro)
            print("INSERT exitoso")
            
    def registroEsValido(self, datosAGuardar):
        dato = datosAGuardar[7:]
        cantidadDeDatos = len(dato.split(" "))
        return (cantidadDeDatos == 3 )
