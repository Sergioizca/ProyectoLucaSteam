import pandas as pd


def buscar_siglo_veinte(archivo):

    df = pd.read_csv(archivo)
    juegos_siglo_veinte = df.loc[df['Year']]
    print("Juegos del siglo XX:\n")
    print(juegos_siglo_veinte)

buscar_siglo_veinte("vgsales.csv")