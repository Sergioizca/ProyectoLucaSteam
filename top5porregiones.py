import pandas as pd


def elegir_region():
    print('Elige la region donde quieras saber el top 5 de ventas: ')
    a = True
    while a:
        region = input('1.America\n2.Europa\n3.Japon\n4.Resto regiones ')
        if region == '1':
            region = 'NA_Sales'
            a = False
        elif region == '2':
            region = 'EU_Sales'
            a = False
        elif region == '3':
            region = 'JP_Sales'
            a = False
        elif region == '4':
            region = 'Other_Sales'
            a = False
        else:
            print('Introduzca un numero valido')
            a = True
    return region


def buscar_top_5_ventas_regiones(archivo, region):
    datos = pd.read_csv(archivo)

    top_5 = datos.sort_values(region, ascending=False).head(5)

    print(f'Top 5 de ventas en {region}:')
    print(top_5)


#region = elegir_region()
#buscar_top_5_ventas_regiones("vgsales.csv", region)