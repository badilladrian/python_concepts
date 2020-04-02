import json as mialias_json
#traigo la libreria de json
import os

# para revisar en que carpeta estoy trabajando print(os.getcwd())
#cambio el directorio default donde python busca primero
os.chdir("C:\\Users\\badil\\Documents\\Work\\Clase12\\JSON_Managing") 

"""INVESTIGUEN DE LA LIBRERIA
PANDAS PARA GENERAR DATAFRAMES
LOS DATAFRAMES PUEDEN CONVERTIRSE A DICCIONARIOS Y DE AHI
A JSON Y VICEVERSA O NO, JSON --> Dict -> captura los valores y hace query inyection"""

# Python object (dict):
dicionario = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#aqui tengo un objeto string que contiene un JSON
json_already = '{ "Nombre":"David", "Clase":"Progra", "Edad":26 }'

print("Aqui voy a imprimit el dicionario:\n", dicionario) #para ver un valor especifico uso dicionario['key']

#transformo el objeto python a JSON
jsonObject = mialias_json.dumps(dicionario)
print(jsonObject)
# Con esto podemos hacerle identacion (ordenar mejor)
print("\nIdentado:",mialias_json.dumps(dicionario, indent=2))
# Con estos parametros podemos definir los separadores 
print("\nSeparadores:",mialias_json.dumps(dicionario, indent=2, separators=(". ", " = ")))
# Con sort podemos ordenar el display de los datos 
print("\nOrdenado por keys:",mialias_json.dumps(dicionario, indent=2, sort_keys=True))


#Convert from JSON to python
python_obj = mialias_json.loads(json_already)
print("\nJSON data transformado a Python:")
print(python_obj)
print("\nEl nombre del usuario: ",python_obj["Nombre"])
print("Se encuentra en la clase: ",python_obj["Clase"])
print("Tiene esta edad: ",python_obj["Edad"]) 

#with y open son palabras reservadas de Python y de parametro envio el archivo con su path absoluto o relativo
with open('data.json') as file:
  productos_data= mialias_json.load(file)

print("\nJSON file transformado a JSON dentro de script:")
print(productos_data)

