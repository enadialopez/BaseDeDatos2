class Pagina:
    CANTIDADMAXDEDATO = 291

    def __init__(self):
        self.datos = bytearray()

    def guardarRegistro(self, registro):
        if not self.estaCompleta():
            self.datos += registro

    def estaCompleta(self):
        return len(self.datos) == self.CANTIDADMAXDEDATO
    
    