class ProgramaAcademico:
    def __innit__(self):
        self.atributos = {}
        self.consolidados = {}

    def agregar_atributo(self, llave, nuevo_dato):
        self.atributos[llave] = nuevo_dato

    def agregar_consolidado(self, sexo, anio, semestre, nuevo_consolidado):
        llave = f"{anio}-{sexo}-{semestre}"
        self.consolidados[llave] = nuevo_consolidado

    def consultar_atributo(self, llave):
        return self.atributos[llave]