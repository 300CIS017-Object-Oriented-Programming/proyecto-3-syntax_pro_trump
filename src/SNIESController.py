from src.Utilidad import *
import pandas as pd
from src.GestorArchivos import *

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

    def set_df(self, df):
        self.df = df

    def get_df(self):
        return self.df

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


                



