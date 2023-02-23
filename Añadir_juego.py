def obtener_valor(valor):
    while not valor:
        print("El valor no puede estar vacío.")
        valor = input("Introduzca un valor: ")
    return valor

def obtener_float(dato):
    while True:
        if not dato:
            print("El valor no puede estar vacío.")
        else:
            try:
                dato_float = float(dato)
                return dato_float
            except ValueError:
                print("El valor debe ser un número.")
        dato = input("Ingrese el valor nuevamente: ")

def agregar_juego(juegos):
    encurso = True
    
    while encurso:
        nombre = input("Introduzca el nombre del juego: ")
        obtener_valor(nombre)
        plataforma = input("Introduzca la plataforma del juego: ")
        obtener_valor(plataforma)
        
        año = None
        while año is None:
            try:
                año = int(input("Introduzca el año de lanzamiento del juego: "))
            except ValueError:
                print("El año debe ser un número entero.")
        genero = input("Introduzca el género del juego: ")
        obtener_valor(genero)        
        empresa = input("Introduzca la empresa del juego: ")
        obtener_valor(empresa)
        na_sales =  input('introduce valor de ventas de Norte America')
        obtener_float(na_sales)
        eu_sales = input('introduce valor de ventas de Europa')
        obtener_float(eu_sales)    
        jp_sales = input('introduce valor de ventas de Japon')
        obtener_float(jp_sales)
        other_sales = input('introduce valor de ventas del resto del mundo')
        obtener_float(other_sales)
        global_sales = input('introduce valor de ventas a nivel global')
        obtener_float(global_sales)
    
        juego = {
            "nombre": nombre,
            "plataforma": plataforma,
            "año": año,
            "genero": genero,
            "publisher": empresa,
            "na_sales": na_sales,
            "eu_sales": eu_sales,
            "jp_sales": jp_sales,
            "other_sales": other_sales,
            "global_sales": global_sales
        }

        a = True
        while a:
            confirmar= input("¿Quieres agregar este juego? (1 = si/2 = no):")
            
            if confirmar == '1':
                juegos.append(juego)
                print("El juego se ha agregado correctamente.")
                a = False
            elif confirmar == '2':
                print("El juego no se ha agregado.")
                a = False
            else:
                print("Tiene que ser 1: Si o 2: No")
        b= True
        while encurso:
            while b:
                confirmar = input("¿Desea agregar otro juego? (1 = si/2 = no): ")
                
                if confirmar == '1':
                    encurso = True
                    b = False
                
                elif confirmar == '2':
                    encurso = False
                    b = False
                else: 
                    confirmar = input("¿Desea agregar otro juego? (1 = si/2 = no): ")
                    b = True





