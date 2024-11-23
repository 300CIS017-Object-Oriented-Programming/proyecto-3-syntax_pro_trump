#Esto es para probar

from SNIESController import *
from src.GestorArchivos import *
import pandas as pd
controller = SNIESController()
leer = GestorArchivos()
df = controller.procesar_datos(2020, 2021, "ZOO")
#print("Sali")
#df = pd.read_excel("D:/ProyectoPOO/proyecto-3-syntax_pro_trump/docs/inputs/admitidos2020.xlsx")
#print("Ya sali")
#df.to_excel("Prueba.xlsx", index=False)
#print("Termine")
#controller.mostrar()
#df1 = leer.leer_archivo("D:/POO/proyecto-3-syntax_pro_trump/docs/inputs/admitidos2020.xlsx", "ZOO", False)
#df2 = leer.leer_archivo("D:/POO/proyecto-3-syntax_pro_trump/docs/inputs/graduados2020.xlsx", "ZOO", True)
#common_columns = df1.columns.intersection(df2.columns)
#df2_unique = df2.merge(df1, on=list(common_columns), how="left", indicator=True)
#df2_unique = df2_unique[df2_unique["_merge"] == "left_only"].drop(columns=["_merge"])
#result = pd.concat([df1, df2_unique], ignore_index=True)
#ultima =  df2.columns[-1]
#ultima_columna = df2[ultima]
#result = pd.concat([df1, ultima_columna], axis=1)
#ultima = df2.columns[-1]  # Nombre de la última columna
#ultima_columna = df2[["CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE",ultima]]

#df = pd.merge(df1, ultima_columna, on=["CÓDIGO SNIES DEL PROGRAMA", "SEMESTRE"], how="left")


df.to_excel("Prueba5.xlsx", index=False)
#df2.to_excel("Prueba.xlsx", index=False)

