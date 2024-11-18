import pandas as pd

class GestorArchivos:
    def leer_archvivo(self, ruta_archivo, palabra_clave, solo_ultima_columna):
        """
        Lee un archivo Excel y filtra las filas que contienen una palabra clave en la columna especificada.
        ruta_archivo: Ruta del archivo Excel.
        columna: Nombre de la columna donde buscar.
        palabra_clave: Palabra clave a buscar.
        return: DataFrame con las filas filtradas.
        """
        try:
            # Leer el archivo Excel
            df = pd.read_excel(ruta_archivo)

            # Filtrar las filas que contienen la palabra clave en la columna especificada
            df_filtrado = df[df["PROGRAMA ACADÉMICO"].str.contains(palabra_clave, case=False, na=False)]
            columnas_predeterminadas = ["CÓDIGO SNIES DEL PROGRAMA", "ID SEXO", "SEXO", "AÑO", "SEMESTRE"]

            if solo_ultima_columna:
                # Seleccionar la última columna y mantener su nombre original
                ultima_columna = df_filtrado.iloc[:, -1]

                # Seleccionar las columnas predeterminadas
                df_filtrado = df_filtrado[columnas_predeterminadas]

                # Concatenar la última columna con el DataFrame filtrado, manteniendo su nombre original
                df_filtrado[ultima_columna.name] = ultima_columna
            return df_filtrado
        except Exception as e:
            print(f"Error al procesar el archivo Excel: {e}")
            return None

