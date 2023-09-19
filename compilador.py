class Compilador:

    def __init__(self, maquinaVirtual):
        self.maquinaVirtual = maquinaVirtual
    
    def parsear(self, query):
        if query.startswith("."):
            self.maquinaVirtual.ejecutarMetacomando(query)
        else:
            self.maquinaVirtual.ejecutarSentenciaSQL(query)
    
    