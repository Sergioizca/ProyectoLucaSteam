import pandas as pd

#Esta función devuelve el archivo con los juegos anteriores al año 2000
def buscar_siglo_veinte(archivo):

    df = pd.read_csv(archivo)
    df = df[df['Year'] < 2000]
    print("Juegos del siglo XX:\n")
    print(df)


# buscar_siglo_veinte("vgsales.csv")
