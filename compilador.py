from maquinaVirtual import MaquinaVirtual

class Compilador:

    maquinaVirtual = MaquinaVirtual()
    
    def parsear(self, query):
        self.maquinaVirtual.ejecutar(query)