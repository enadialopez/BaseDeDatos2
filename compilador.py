from maquinaVirtual import MaquinaVirtual

class Compilador:

    maquinaVirtual = MaquinaVirtual()
    
    def parsear(self, query):
        if query.startswith("."):
            self.maquinaVirtual.ejecutarMetacomando(query)
        else:
            self.maquinaVirtual.ejecutarSentenciaSQL(query)
    
    