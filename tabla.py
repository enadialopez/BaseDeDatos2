from pagina import Pagina

class Tabla:
    
    paginas = []

    def guardarRegistroEnPagina(self, registro):
        #Se guarda el registro en la una pagina con registro serializado
        registroSerializado = self.serializar(registro)
        pagina = self.paginaAEscribir()
        pagina.guardarRegistro(registroSerializado)

    def serializar(self, registro):
        # Devuelve los datos serializados del registro recibido
        elementosDelRegistro = registro.split(" ")
        id = elementosDelRegistro[1]
        nombre = elementosDelRegistro[2]
        email = elementosDelRegistro[3]

        idSerializado = self.serializarId(id)
        nombreSerializado = self.serializarNombre(nombre)
        emailSerializado = self.serializarEmail(email)

        return idSerializado + nombreSerializado + emailSerializado

    def serializarId(self, id):
        # Recibe un ID en string, lo convierte a int, y despues a 4 bytes en formato big endian
        numId = int(id)
        return numId.to_bytes(4, byteorder="big")
    
    def serializarNombre(self, nombre):
        # Recibe un string correspondiente a un nombre y devuelve 32 bytes como sigue:
        # - los primeros bytes representan el nombre ingresado traducido en byte en formato ascii
        # - los siguientes bytes corresponden a caracteres nulos
        nombreEnBytes = bytes(nombre, "ascii")
        cantidadEspaciosNulosNecesarios = 32 - len(nombreEnBytes)
        return nombreEnBytes + bytes(cantidadEspaciosNulosNecesarios)
    
    def serializarEmail(self, email):
        # Recibe un string correspondiente a un email y devuelve 255 bytes como sigue:
        # - los primeros bytes representan el email ingresado traducido en byte en formato ascii
        # - los siguientes bytes corresponden a caracteres nulos
        emailEnBytes = bytes(email, "ascii")
        cantidadEspaciosNulosNecesarios = 255 - len(emailEnBytes)
        return emailEnBytes + bytes(cantidadEspaciosNulosNecesarios)

    def paginaAEscribir(self):
        if (not self.paginas) or (self.ultimaPagina().estaCompleta()):
            paginaNueva = Pagina()
            self.paginas.append(paginaNueva)
            return paginaNueva
        else:
            return self.ultimaPagina()

    def ultimaPagina(self):
        return self.paginas[-1]