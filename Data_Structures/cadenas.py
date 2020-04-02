"""Podemos correr en el CMD con python main.py >> si usamos eso podemos
guardar el resultado del script hacia un file! por ejem: resultado.txt"""

cadena = "Hola Adrian!"
#para remplazar el atributo de un objeto existente
nueva_cadena = cadena.replace("Hola","Buenas")
#Strip elimina los espacios al principio y al final!
cadena_sinespacios = cadena.strip()
#upper() make upCasses / lower() make lowCasses
#split() -> utiliza un delimitador para separar el string en objetos
palabras = "Ho3la3Mu3gusto3"
lista_separada = palabras.split("3")
print(lista_separada)
#find indica la cantidad de veces que encuentra un char
print(str(cadena.find("a")))
print(nueva_cadena)