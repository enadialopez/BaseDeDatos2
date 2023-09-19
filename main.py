from compilador import Compilador
from maquinaVirtual import MaquinaVirtual
from tabla import Tabla
from paginador import Paginador

def correrRepl():
    paginador = Paginador()
    tabla = Tabla(paginador)
    maquinaVirtual = MaquinaVirtual(tabla)
    compilador = Compilador(maquinaVirtual)

    query = input("sql>")
    while query is not None:
        compilador.parsear(query)
        query = input("sql>")

def main():
    paginador.leer_base_de_datos(base_de_datos)
    correrRepl()

if __name__ == "__main__":
    main()