class Consolidado:
    def __init__(self):
        self.datosConsolidado = {}

    def agregar_dato(self,llave,nuevo_dato):
        self.datosConsolidado[llave] = nuevo_dato

    def buscar_dato(self,llave):
        return self.datosConsolidado[llave]