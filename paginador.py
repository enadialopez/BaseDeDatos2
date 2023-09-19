import os

class Paginador:

    def __init__(self):
        self.direccion_base_de_datos = ""
        self.tamanio_base_datos = 0
        self.cache = {}
        self.base_de_dato = open(self.direccion_base_de_datos)

    def leer_base_de_datos(self, base):
        self.tamanio_base_datos