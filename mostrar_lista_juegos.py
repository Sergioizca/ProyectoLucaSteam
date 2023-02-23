# Creamos una función mostrar_lista_juegos() que devuelve el resultado de la lista de diccionarios

import csv

def mostrar_lista_juegos():
    # Abrir el archivo CSV con los datos de los videojuegos
    with open('vgsales.csv', 'r') as csvfile:
        # Crear un objeto DictReader para leer los datos del archivo CSV
        lista = csv.DictReader(csvfile)

        # Imprimir el encabezado de las columnas
        print('Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales')
        
        # Recorrer los datos e imprimir cada fila en el formato especificado
        for fila in lista:
            print(f"{fila['Rank']},{fila['Name']},{fila['Platform']},{fila['Year']},{fila['Genre']},{fila['Publisher']},{fila['NA_Sales']},\
                {fila['EU_Sales']},{fila['JP_Sales']},{fila['Other_Sales']},{fila['Global_Sales']}")


"""


def main():
    lista=convertir_csv_diccionarios("vgsales.csv")
    mostrar_lista_juegos(lista)

main()

"""
