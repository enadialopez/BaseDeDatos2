from maquinaVirtual import MaquinaVirtual

class Compilador:

    maquinaVirtual = MaquinaVirtual()
    
    def parsear(self, query):
        if query.startswith("."):
            self.ejecutarMetacomando(query)
        else:
            self.ejecutarSentenciaSQL(query.upper())
    
    