import csv


def convertir_csv_diccionarios(nombre_archivo):
    
    with open(nombre_archivo, encoding="utf-8") as archivo:
        next(archivo)  # Omitir encabezado del archivo
        juegos = []
        for linea in archivo:
            linea = linea.rstrip("\n")  # Quitar salto de línea
            columnas = linea.split(',')
            nombre = columnas[1]
            plataforma = columnas[2]
            año = columnas[3]
            genero = columnas[4]
            empresa = columnas[5]
            na_sales = columnas[6]
            eu_sales = columnas[7]
            jp_sales = columnas[8]
            other_sales = columnas[9]
            global_sales = columnas[10]

            juegos.append({
                "nombre": nombre,
                "plataforma": plataforma,
                "año": año,
                "genero": genero,
                "publisher": empresa,
                "na_sales": na_sales,
                "eu_sales": eu_sales,
                "jp_sales": jp_sales,
                "other_sales": float(other_sales),
                "global_sales": float(global_sales)
            })
        return juegos
