from convertir_csv_diccionario import *

# Introducir bucle que pregunte si quiere salir con teclado
# o si quiere continuar eliminando otro juego


def pregunta_continuar(mensaje):
    # Función que pregunta si quieres seguir ejecutando un bucle.
    # Si el input es "n" saldrá del bucle
    respuesta = input(mensaje).lower()
    if respuesta == "n":
        return False
    return True


def borrar_de_dic(juegos):
    # Función para borrar juegos del diccionario importado de csv
    continuar = True
    while continuar:
        # En un bucle vamos a preguntar al usuario por el nombre del juego que desea borrar
        nombre_borrar = input(
            "Inserta el nombre del juego que deseas borrar: \n")

        # Variable que indica si se ha encontrado el nombre en el diccionario
        juego_encontrado = False
        # Busca en el campo "nombre" el valor introducido para ver si coincide en el diccionario
        for juego in juegos:
            if juego["nombre"] == nombre_borrar:
            
                a = input(f"¿Quieres eliminar este juego? (1 = si/2 = no): {juego}")
                
                if a == '1':
                    juegos.remove(juego)
                    juego_encontrado = True  # Variable cambia el estado a "encontrada"
                else:    
                    print('Juego no eliminado')
                    break
                    
                
        # Si la variable ha sido encontrada, el valor "nombre" introducido se borrará
        # Este if pregunta si quieres ejecutar el código de nuevo
        if juego_encontrado:
            continuar = pregunta_continuar(
                "Se ha borrado la entrada seleccionada. ¿Quieres eliminar otra entrada? s/n:\n")
        # Si el valor introducido no ha sido encontrado,
        # se preguntará si quieres buscar de nuevo o introducir "n" para salir
        else:
            continuar = pregunta_continuar(
                "Ese juego no consta en nuestro archivo. ¿Quieres intentarlo de nuevo? s/n:\n")
            
