#Esto es para probar

from SNIESController import SNIESController
from src.GestorArchivos import GestorArchivos
import pandas as pd
controller = SNIESController()
leer = GestorArchivos()
#df = controller.procesar_datos(2020, 2021, "ZOO")
#print("Sali")
#df = pd.read_excel("D:/ProyectoPOO/proyecto-3-syntax_pro_trump/docs/inputs/admitidos2020.xlsx")
#print("Ya sali")
#df.to_excel("Prueba.xlsx", index=False)
#print("Termine")
#controller.mostrar()
df1 = leer.leer_archivo("D:/ProyectoPOO/proyecto-3-syntax_pro_trump/docs/inputs/admitidos2020.xlsx", "ZOO", False)
df2 = leer.leer_archivo("D:/ProyectoPOO/proyecto-3-syntax_pro_trump/docs/inputs/admitidos2021.xlsx", "ZOO", False)
#common_columns = df1.columns.intersection(df2.columns)
#df2_unique = df2.merge(df1, on=list(common_columns), how="left", indicator=True)
#df2_unique = df2_unique[df2_unique["_merge"] == "left_only"].drop(columns=["_merge"])
#result = pd.concat([df1, df2_unique], ignore_index=True)
#ultima =  df2.columns[-1]
#ultima_columna = df2[ultima]
#result = pd.concat([df1, ultima_columna], axis=1)


#df = pd.merge(df1, df2, on="CÓDIGO SNIES DEL PROGRAMA", how="left")


df1.to_excel("Prueba1.xlsx", index=False)
df2.to_excel("Prueba.xlsx", index=False)

