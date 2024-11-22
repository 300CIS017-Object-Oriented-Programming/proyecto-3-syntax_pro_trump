from ProgramaAcademico import ProgramaAcademico
from Consolidado import Consolidado
from Utilidad import *
import pandas as pd
from pprint import pprint
from src.GestorArchivos import GestorArchivos

ut = Utilidad()
lector = GestorArchivos()
class SNIESController:
    def __init__(self):
        self.df = None

    def procesar_datos(self, anio1, anio2, palabra_clave):
        """
        Procesa datos de múltiples archivos Excel y los combina en un único DataFrame.

        Args:
            anio1 (int): Año inicial.
            anio2 (int): Año final.
            palabra_clave (str): Palabra clave para filtrar programas.

        Returns:
            pd.DataFrame: DataFrame combinado con los datos procesados.
        """
        try:
            # Generar lista de años
            anios = self.generar_anios_busqueda(anio1, anio2)
            # Iterar por los archivos adicionales
            flag = True
            flag2 = True

            for anio in anios:
                #FIXME: poner bandera para solo hacer el merge con el primer archivo de un año
                for direccion in LISTA_DIRECCIONES:
                    if flag2:
                        # Leer el primer archivo
                        self.df = lector.leer_archivo(LISTA_DIRECCIONES[0] + anios[0] + ".xlsx", palabra_clave, False)

                        # Convertir columnas clave a tipo string
                        self.df["CÓDIGO SNIES DEL PROGRAMA"] = self.df["CÓDIGO SNIES DEL PROGRAMA"].astype(str)
                        self.df["SEMESTRE"] = self.df["SEMESTRE"].astype(str)
                        self.df["AÑO"] = self.df["AÑO"].astype(str)

                        flag2 = False
                    else:
                        # Leer archivo para el año actual
                        ruta_archivo = direccion + anio + ".xlsx"
                        df_filtrado = lector.leer_archivo(ruta_archivo, palabra_clave, True)

                        # Convertir columnas clave a tipo string
                        df_filtrado["CÓDIGO SNIES DEL PROGRAMA"] = df_filtrado["CÓDIGO SNIES DEL PROGRAMA"].astype(str)
                        df_filtrado["SEMESTRE"] = df_filtrado["SEMESTRE"].astype(str)
                        df_filtrado["AÑO"] = df_filtrado["AÑO"].astype(str)

                        # Realizar la fusión
                        if anio == anios[0]:
                            self.df = pd.merge(
                                self.df, df_filtrado,
                                on=["CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE", "AÑO"],
                                how="left",
                                suffixes=("", f"_{anio}")
                            )
                        else:
                            self.df = pd.merge(
                                self.df, df_filtrado,
                                on=["CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE"],
                                how="left",
                                suffixes=("", f"_{anio}")
                            )

                        # Renombrar las columnas duplicadas (agregar el año como sufijo)
                        columnas_duplicadas = [col for col in self.df.columns if col.endswith(f"_{anio}")]
                        for col in columnas_duplicadas:
                            nuevo_nombre = f"{col.split('_')[0]}_{anio}"  # Nombre base + año
                            self.df.rename(columns={col: nuevo_nombre}, inplace=True)

            return self.df


        except Exception as e:
            print(f"Error al procesar los datos: {e}")
            return pd.DataFrame()

    #Funcion de prueba
    def mostrar(self):
        print(self.df)

    def crear_programas(self, df_filtrado):
        # Creación de un diccionario para los programas académicos, evitamos acceder repetidamente a `self.programas_academicos`
        programas_academicos = self.programas_academicos

        # Extraer las últimas 5 columnas que contienen los datos del consolidado
        columnas_consolidado = df_filtrado.columns[-5:]

        # Recorrer todas las filas del DataFrame
        for _, fila in df_filtrado.iterrows():
            # Obtener el código SNIES del programa académico
            codigo_snies = fila["CÓDIGO SNIES DEL PROGRAMA"]
            consolidado = Consolidado()

            # Agregar los datos del consolidado (últimas 5 columnas)
            for columna, valor in fila[columnas_consolidado].items():
                consolidado.agregar_dato(columna, valor)  # Llamamos con nombre de columna y valor

            # Verificar si el programa académico ya existe
            if codigo_snies not in programas_academicos:
                # Si no existe, crear un nuevo programa académico
                programa_academico = ProgramaAcademico()

                # Agregar los atributos del programa académico (todas las columnas menos las últimas 5)
                for columna, valor in fila.iloc[:-5].items():
                    programa_academico.agregar_atributo(columna, valor)

                # Asignar el programa al diccionario
                programas_academicos[codigo_snies] = programa_academico
                programa_nuevo_creado = True
            else:
                # Si el programa ya existe, obtenerlo
                programa_academico = programas_academicos[codigo_snies]
                programa_nuevo_creado = False

            # Obtener datos clave para el consolidado
            id_sexo = consolidado.buscar_dato("ID SEXO")
            anio = consolidado.buscar_dato("AÑO")
            semestre = consolidado.buscar_dato("SEMESTRE")

            # Actualizar o asignar el consolidado al programa académico
            if not programa_nuevo_creado:
                programa_academico.agregar_consolidado(id_sexo, anio, semestre, consolidado)
            else:
                programa_academico.agregar_consolidado(id_sexo, anio, semestre, consolidado)

        # Actualizar el diccionario de programas académicos en el objeto
        self.programas_academicos = programas_academicos

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

    def generar_anios_busqueda(self, anio1, anio2):
        """
        Genera una lista de años como cadenas de texto entre los años anio1 y anio2 (inclusive).

        :param anio1: Año inicial (int).
        :param anio2: Año final (int).
        :return: Lista de años como cadenas (list[str]).
        """
        # Inicializamos la lista para almacenar los años
        anos_busqueda = []

        # Iteramos desde anio1 hasta anio2 inclusive
        for anio_actual in range(anio1, anio2 + 1):
            # Convertimos el año actual a string y lo añadimos a la lista
            anos_busqueda.append(str(anio_actual))

        return anos_busqueda


                



