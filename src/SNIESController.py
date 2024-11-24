import pandas as pd
from src.GestorArchivos import *
from src.Settings import *

lector = GestorArchivos()
class SNIESController:
    def __init__(self):
        self.df = None
        self.df_junto = None

    def procesar_datos(self, anio1, anio2, palabra_clave, dict_archivos_extra):
        """
        Procesa datos de múltiples archivos Excel y los combina en un único DataFrame.

        Args:
            anio1 (int): Año inicial.
            anio2 (int): Año final.
            palabra_clave (str): Palabra clave para filtrar programas.

        Returns:
            pd.DataFrame: DataFrame combinado con los datos procesados.
            :param lista_direcciones:
        """
        try:
            # Generar lista de años
            anios = self.generar_anios_busqueda(anio1, anio2)

            # Iterar por los archivos para leerlos
            primer_archivo = True
            for anio in anios:
                for direccion in LISTA_DIRECCIONES:
                    # Leer archivo para el año actual
                    ruta_archivo = direccion + anio + ".xlsx"
                    df_filtrado = lector.leer_archivo(ruta_archivo, palabra_clave, (not primer_archivo), dict_archivos_extra)

                    # Convertir columnas clave a tipo string
                    df_filtrado[STR_CODIGO_SNIES] = df_filtrado[STR_CODIGO_SNIES].astype(str)
                    df_filtrado[STR_SEMESTRE] = df_filtrado[STR_SEMESTRE].astype(str)

                    #Si es el primer archivo renombramos solo la columna de ADMITIDOS
                    if primer_archivo:
                        df_filtrado.rename(columns={STR_ADMITIDOS : f'{STR_ADMITIDOS}_{anio}'}, inplace = True)
                        self.df = df_filtrado
                        primer_archivo = False
                    else:
                        for col in df_filtrado.columns:
                            if not ((col == STR_CODIGO_SNIES) or (col == STR_SEMESTRE)):
                                df_filtrado.rename(columns={col : f'{col}_{anio}'}, inplace = True)

                        self.df = pd.merge(
                            self.df, df_filtrado,
                            on=[STR_CODIGO_SNIES, STR_SEMESTRE],
                            how="left"
                        )

            return self.df


        except Exception as e:
            print(f"Error al procesar los datos: {e}")
            return pd.DataFrame()

    #Funcion de prueba
    def mostrar(self):
        print(self.df)

    def set_df(self, df):
        self.df = df

    def set_df_junto(self, df):
        columnas_predeterminadas = [STR_CODIGO_SNIES, STR_METODOLOGIA, STR_PROGRAMA_ACADEMICO,
                                    STR_NOMBRE_IES, STR_TIPO_IES, STR_DEPARTAMENTO,
                                    STR_MUNICIPIO, STR_NIVEL_FORMACION]
        df_junto = df.groupby(columnas_predeterminadas).sum(numeric_only=True).reset_index()
        self.df_junto = df_junto

    def get_df(self):
        return self.df

    def get_df_junto(self):
        return self.df_junto

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