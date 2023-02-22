import csv 

def findAndReplace(lista, itemAReemplazar, nuevoValor): 
    for index, item in enumerate(list):
        if item == itemAReemplazar:
            lista[index] = nuevoValor

def mostrarMensajeInicio():
    opcion = int(input("""
      Indique lo que desea realizar:
        \n 
          1) Mostrar los elementos de la lista 
          2) Editar un elemento
      """))
    return opcion

seguir = True

while seguir:   
    opcion = mostrarMensajeInicio()
    if opcion == 1:
        for index in range(len(Lista)):
            print(f'\n Posicion {index} Valor:  {[index]}')

    if opcion == 2:
        edit = input('Indique el Valor que quiere cambiar: ')
        if edit in cvs:
            newValue = input(f'A que desea cambiar el valor seleccionado {edit}: ')
            findAndReplace(Lista,edit,newValue)
            print('Se ha cambiado exitosamente')
        else :
            print('No se encuentra en la Lista, intente nuevamente.')