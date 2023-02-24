import pandas as pd

def buscar_top_5_ventas_globales(archivo):
    
    datos = pd.read_csv(archivo)

    
    top_5 = datos.sort_values('Global_Sales', ascending=False).head(5)

    
    print("Top 5 juegos con mayores ventas globales: ")
    print(top_5)


# buscar_top_5_ventas_globales("vgsales.csv")
