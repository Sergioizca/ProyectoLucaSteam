import csv


def convertir_csv_diccionarios(nombre_archivo):
    juegos = []
    with open(nombre_archivo, newline='\n', encoding='utf-8') as archivo:
        lista = csv.reader(archivo, delimiter=',', quotechar='"')
        
        next(lista)  # Omitir encabezado del archivo
        
        for linea in lista:
            
            
            nombre = linea[1]
            plataforma = linea[2]
            año = linea[3]
            genero = linea[4]
            empresa = linea[5]
            na_sales = linea[6]
            eu_sales = linea[7]
            jp_sales = linea[8]
            other_sales = linea[9]
            global_sales = linea[10]
            
            juegos.append({
                "nombre": nombre,
                "plataforma": plataforma,
                "año": int(año),
                "genero": genero,
                "publisher": empresa,
                "na_sales": float(na_sales),
                "eu_sales": float(eu_sales),
                "jp_sales": float(jp_sales),
                "other_sales": float(other_sales),
                "global_sales": float(global_sales)
            })
        return juegos
