from src.Utilidad import *
#definimos un objeto para la clase utilidad
ut = Utilidad()

class Consolidado:
    def __init__(self):
        self.datosConsolidado = {}

    def agregar_dato(self,llave,nuevo_dato):
        nueva_llave = ut.minusculas_sin_espacios(llave)
        self.datosConsolidado[nueva_llave] = nuevo_dato

    def buscar_dato(self,llave):
        try:
            llave_buscar = ut.minusculas_sin_espacios(llave)
            return self.datosConsolidado[llave_buscar]
        except KeyError:
            raise KeyError(f"{llave_buscar} no se encontró en el diccionario")
