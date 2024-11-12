from Utilidad import Utilidad
import Settings as settings

#Definimos un objeto de la clase utilidad para ayudarnos
ut = Utilidad()

class ProgramaAcademico:
    def __innit__(self):
        self.atributos = {}
        self.consolidados = {}

    def agregar_atributo(self, llave, nuevo_dato):
        nueva_llave = ut.minusculas_sin_espacios(llave)
        self.atributos[nueva_llave] = nuevo_dato

    def agregar_consolidado(self, sexo, anio, semestre, nuevo_consolidado):
        nueva_llave = f"{ut.minusculas_sin_espacios(anio)}-"
        nueva_llave += f"{ut.minusculas_sin_espacios(sexo)}-"
        nueva_llave += f"{ut.minusculas_sin_espacios(semestre)}"
        self.consolidados[nueva_llave] = nuevo_consolidado

    def consultar_atributo(self, llave):
        try:
            nueva_llave = ut.minusculas_sin_espacios(llave)
            return self.atributos[nueva_llave]
        except KeyError:
            raise KeyError(f"{nueva_llave} no se encontró en el diccionario")

    def consultar_consolidado(self, sexo, anio, semestre):
        try:
            nueva_llave = f"{ut.minusculas_sin_espacios(anio)}-"
            nueva_llave += f"{ut.minusculas_sin_espacios(sexo)}-"
            nueva_llave += f"{ut.minusculas_sin_espacios(semestre)}"
        except KeyError:
            raise KeyError(f"{nueva_llave} no se encontró en el diccionario")
        else:
            return self.consolidados[nueva_llave]