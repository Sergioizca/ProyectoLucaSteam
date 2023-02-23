import pandas as pd

#Esta función calcula la media de la columa Ventas Globales
#Y devuelve el archivo con todos los juegos que tuvieran mas ventas que la media
def media_ventas_globales(archivo):

    df = pd.read_csv(archivo)
    media = df['Global_Sales'].mean()
    encima_media = df[df['Global_Sales'] > media]
    print(encima_media)


# media_ventas_globales("vgsales.csv")
