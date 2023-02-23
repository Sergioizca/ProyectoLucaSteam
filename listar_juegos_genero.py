import pandas as pd

#Esta función busca el archivo y ordena los juegos por género
def listar_juegos_genero(archivo):
    genero = input("¿Qué género desea buscar?:\n")
    df = pd.read_csv(archivo)
    juegos_por_genero =  df.loc[df['Genre'].isin([genero, 'N/A', ""])]
    
    print(f"Los juegos de {genero} son:")
    print(juegos_por_genero)


listar_juegos_genero("vgsales.csv")