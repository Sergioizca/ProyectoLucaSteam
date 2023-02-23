import pandas as pd


def buscar_nintendo(archivo):

    datos = pd.read_csv(archivo)
    nintendo_games = datos.loc[datos['Publisher'].isin(['Nintendo'])]
    print("Juegos de Nintendo:")
    print(nintendo_games)

buscar_nintendo("vgsales.csv")