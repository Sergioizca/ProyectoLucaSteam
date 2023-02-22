print(diccionario.get(''))


# pop(): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(diccionario.pop(''))

print(diccionario)
{'': '', '': ''}

diccionario.update({' ':''})
diccionario.update({' ':''})
print(diccionario)
{'': '', '': '', '': ''}

 # "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
print ("" in diccionario)
True
print ("" in diccionario)
False
print ("" in diccionario)
False

# "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
print ("" in diccionario.values())
True

# del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
del diccionario['']
print(diccionario)
{'': '', '': ''}
