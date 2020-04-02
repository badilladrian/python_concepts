"""Esto son los tipos de estructuras de datos de python
y son objetos iterables
[start:stop:step] [:::]"""

#lista tiene append() remove
mi_primera_lista = [1,2,3,4,5,6,7,8,9]
print(mi_primera_lista)
print(type(mi_primera_lista))
print(id(mi_primera_lista))

#tuplet inmutables
mi_primer_tuplet = ("hola",123,mi_primera_lista)
print(mi_primer_tuplet)
print(type(mi_primer_tuplet))
print(id(mi_primer_tuplet))

#set (es un diagrama de Venn) && join left right 
mi_primer_set = set('94756')
secundo_set = set('75124')
print(mi_primer_set) 
print(type(mi_primer_set))
print(id(mi_primer_set))

#recorre cada elemento de el objeto iterable
for objeto in mi_primera_lista:
    print(objeto)


print(mi_primera_lista[2:7:2])
print(mi_primera_lista[1::-1])