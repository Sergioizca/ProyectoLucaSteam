import pandas as pd

def buscar_anios_pares(archivo):
    datos = pd.read_csv(archivo)
    datos = datos[datos['Year'] % 2 == 0]
    print(datos[['Rank', 'Name', 'Year']])


# buscar_anios_pares("vgsales.csv")