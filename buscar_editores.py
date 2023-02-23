import pandas as pd

def buscar_editores(archivo):
    editor= input("Indique el editor del que desea buscar sus publicaciones: ")
    datos = pd.read_csv(archivo)
    juegos_editor =  datos.loc[datos['Publisher'].isin([editor, 'N/A', ""])]
    
    print("Lo que sea:")
    print(juegos_editor)
