
def buscar_juego_nombre(archivo):

    df = pd.read_csv(archivo)
    df = df[df['name']]

    print("Buscar juegos:\n")
    print(df)


buscar_juego_nombre("vgsales.csv")