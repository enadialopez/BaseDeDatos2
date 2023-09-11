from compilador import Compilador
from maquinaVirtual import MaquinaVirtual
from tabla import Tabla

def correrRepl():
    tabla = Tabla()
    maquinaVirtual = MaquinaVirtual(tabla)
    compilador = Compilador(maquinaVirtual)

    query = input("sql>")
    while query is not None:
        compilador.parsear(query)
        query = input("sql>")

def main():
    correrRepl()

if __name__ == "__main__":
    main()