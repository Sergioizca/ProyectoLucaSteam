# menu
print(" **** MENU **** \n **** 1.Añadir **** \n **** 2.Borrar **** \n **** 3.Modificar **** \n **** 4.Listar **** \n **** 5.Salir **** \n ***************")
valor = int(input())

match valor:
    case 1 | None:
        # agregar_juego()
        print("Añadir")
    case 2 | None:
        print("Borrar")
        # borrar_juego()
    case 3 | None:
        print("Modificar")
        # modificar_juego(obtener_cambio())
    case 4 | None:
        print("Listar")
        # mostrar_lista_juegos()
    case 5 | None:
        print("Salir")

# Pdte ampliar el menú (si fuera necesario), acotar rango de numeros.
