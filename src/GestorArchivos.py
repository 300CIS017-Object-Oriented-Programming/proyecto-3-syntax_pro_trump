import pandas as pd

class GestorArchivos:
    def leer_archivo(self, ruta_archivo, palabra_clave, unico_dato):
        """
        Lee un archivo Excel y filtra las filas que contienen una palabra clave en la columna 'PROGRAMA ACADÉMICO'.
        También selecciona columnas predeterminadas y opcionalmente incluye solo la última columna.

        Args:
            ruta_archivo (str): Ruta del archivo Excel.
            palabra_clave (str): Palabra clave a buscar.

        Returns:
            pd.DataFrame: DataFrame filtrado y procesado.
        """
        try:
            if not unico_dato:
                # Leer el archivo Excel con solo las columnas necesarias al inicio
                df = pd.read_excel(ruta_archivo)  # Cambia si las columnas relevantes están en un rango específico.
                df_palabra_clave = df[df["PROGRAMA ACADÉMICO"].str.contains(palabra_clave, case=False, na=False)]
                columnas_predeterminadas = ["CÓDIGO SNIES DEL PROGRAMA", "METODOLOGÍA", "PROGRAMA ACADÉMICO", "INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)",
                                            "PRINCIPAL O SECCIONAL","DEPARTAMENTO DE DOMICILIO DE LA IES", "MUNICIPIO DE DOMICILIO DE LA IES", "NIVEL DE FORMACIÓN", "SEMESTRE"]
                ultima_columna_nombre = df.columns[-1]
                ultima_columna = df_palabra_clave[ultima_columna_nombre]
                df_filtrado = df_palabra_clave[columnas_predeterminadas]
                df_filtrado = pd.concat([df_filtrado, ultima_columna], axis=1)
                df_consolidado = df_filtrado.groupby(columnas_predeterminadas).sum(numeric_only=True).reset_index()
            else:
                df = pd.read_excel(ruta_archivo)  # Cambia si las columnas relevantes están en un rango específico.
                df_palabra_clave = df[df["PROGRAMA ACADÉMICO"].str.contains(palabra_clave, case=False, na=False)]
                columnas_predeterminadas = ["CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE"]
                ultima_columna_nombre = df.columns[-1]
                ultima_columna = df_palabra_clave[ultima_columna_nombre]
                df_filtrado = df_palabra_clave[columnas_predeterminadas]
                df_filtrado = pd.concat([df_filtrado, ultima_columna], axis=1)
                df_consolidado = df_filtrado.groupby(columnas_predeterminadas).sum(numeric_only=True).reset_index()


            return df_consolidado
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return pd.DataFrame()


