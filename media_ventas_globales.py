import pandas as pd


def media_ventas_globales(archivo):

    df = pd.read_csv(archivo)
    media = df['Global_Sales'].mean()
    encima_media = df[df['Global_Sales'] > media]
    print(encima_media)


# media_ventas_globales("vgsales.csv")
