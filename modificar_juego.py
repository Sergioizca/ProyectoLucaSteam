def modificar_juego(diccionario_seleccion,cambio):
    if cambio == 1:
        diccionario_seleccion.update({"nombre": input("Ingrese el nuevo nombre: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 2:
        diccionario_seleccion.update({"plataforma": input("Ingrese la nueva plataforma: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 3:
        diccionario_seleccion.update({"año": input("Ingrese el nuevo año: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 4:
        diccionario_seleccion.update({"genero": input("Ingrese el nuevo genero: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 5:
        diccionario_seleccion.update({"publisher": input("Ingrese la nueva empresa: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 6:
        diccionario_seleccion.update({"na_sales": input("Ingrese las nuevas ventas de NA: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 7:
        diccionario_seleccion.update({"eu_sales": input("Ingrese las nuevas ventas de EU: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 8:
        diccionario_seleccion.update({"jp_sales": input("Ingrese las nuevas ventas de Japon: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 9:
        diccionario_seleccion.update({"other_sales": input("Ingrese las nuevas ventas de otras regiones: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")
    elif cambio == 10:
        diccionario_seleccion.update({"global_sales": input("Ingrese las nuevas ventas globales: ")})
        print(f"\nElemento editado correctamente: {diccionario_seleccion}\n")    
    else:
        print(f"\nSeleccione un elemento correcto")

