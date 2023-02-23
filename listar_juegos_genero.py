import pandas as pd

#Esta función busca el archivo y ordena los juegos por género
def listar_juegos_genero(archivo):

    df = pd.read_csv(archivo)
    df = df.sort_values[df['Genre']]
    print(df)


# buscar_siglo_veinte("vgsales.csv")