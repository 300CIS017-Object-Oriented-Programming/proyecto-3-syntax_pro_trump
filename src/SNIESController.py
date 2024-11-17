from requests import delete

from ProgramaAcademico import ProgramaAcademico
from Consolidado import Consolidado
from Utilidad import Utilidad
import pandas as pd
ut = Utilidad()
class SNIESController:
    def __init__(self):
        self.programas_academicos = {}

    def crear_programas(self, df_filtrado):
        for _, fila in df_filtrado.iterrows():  # Usar iterrows para obtener la fila directamente
            programa_academico = ProgramaAcademico()
            consolidado = Consolidado()
            # Iterar sobre las columnas del DataFrame y agregar los atributos al objeto
            for columna in df_filtrado.iloc[:, :-5].columns:
                # Limpiar el nombre de la columna y agregar el valor correspondiente
                nombre_atributo = columna
                valor_atributo = fila[columna]
                programa_academico.agregar_atributo(nombre_atributo, valor_atributo)

            for columna in df_filtrado.iloc[:,-5 :].columns:
                nombre_atributo = columna
                valor_atributo = fila[columna]
                consolidado.agregar_dato(nombre_atributo, valor_atributo)


            # Obtener el código SNIES del nuevo programa
            codigo_snies = programa_academico.consultar_atributo("CÓDIGO SNIES DEL PROGRAMA")

            # Verificar si el código SNIES ya está en el diccionario
            if codigo_snies not in self.programas_academicos:
                # Si no está, agregarlo al diccionario
                self.programas_academicos[codigo_snies] = programa_academico
                programa_nuevo_creado = True
            else:
                # Si ya está, no se agrega y se indica que no fue creado
                programa_nuevo_creado = False


            id_sexo = consolidado.buscar_dato("ID SEXO")
            anio = consolidado.buscar_dato("AÑO")
            semestre = consolidado.buscar_dato("SEMESTRE")

            # Si el programa ya existía, actualizamos el consolidado
            if not programa_nuevo_creado:
                # Asignamos el consolidado al programa existente
                programa_existente = self.programas_academicos[codigo_snies]
                programa_existente.agregar_consolidado(id_sexo, anio, semestre, consolidado)
            else:
                # Si el programa es nuevo, le asignamos el consolidado correspondiente
                programa_academico.agregar_consolidado(id_sexo, anio, semestre, consolidado)

    def asignar_consolidados(self, df_filtrado):
        for _, fila in df_filtrado.iterrows():
            codigo_snies = fila["CÓDIGO SNIES DEL PROGRAMA"]
            id_sexo = fila["ID SEXO"]
            anio = fila["AÑO"]
            semestre = fila["SEMESTRE"]

            if codigo_snies in self.programas_academicos:
                programa_existente = self.programas_academicos[codigo_snies]

                try:
                    # Verificar si ya existe un consolidado
                    consolidado_viejo = programa_existente.consultar_consolidado(id_sexo, anio, semestre)

                    ultima_columna = df_filtrado.columns[-1]
                    dato_ultima_columna = fila[ultima_columna]
                    # Si existe, añadimos el dato clave

                    consolidado_viejo.agregar_dato(ultima_columna, dato_ultima_columna)
                except KeyError:
                    # Si no existe, crear un nuevo consolidado y agregar todos los datos
                    consolidado_nuevo = Consolidado()
                    for columna in df_filtrado.iloc[:, 1:].columns:
                        nombre_atributo = columna
                        valor_atributo = fila[columna]
                        consolidado_nuevo.agregar_dato(nombre_atributo, valor_atributo)

                    # Asociar el nuevo consolidado al programa existente
                    programa_existente.agregar_consolidado(id_sexo, anio, semestre, consolidado_nuevo)

                



