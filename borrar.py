import csv



def borrar(juegos):
    a = True
    while True:
        nombre_borrar = int(input("Inserta el nombre del juego que deseas borrar"))
        if nombre_borrar in juegos:
            del juegos[nombre_borrar]
            print("Se ha borrado la entrada seleccionada")
            a = False
        else:
            print("Ese videojuego no consta en nuestro archivo. Vuelve a intentarlo")
            
borrar(juegos)
print(juegos) #Esto se quita despues