class Pagina:
    CANTIDADMAXDEDATO = 291

    def __init__(self):
        self.datos = bytearray()

    def guardarRegistro(self, registro):
        if not self.estaCompleta():
            self.datos += registro

    def estaCompleta(self):
        return len(self.datos) == self.CANTIDADMAXDEDATO
    
    def obtener_registros(self):
        posicionInicial = 0
        registros = []
        while posicionInicial < len(self.datos):
            registro = self.datos[posicionInicial:posicionInicial+self.CANTIDADMAXDEDATO]
            registros.append(registro)
            posicionInicial += self.CANTIDADMAXDEDATO
        return registros

            
