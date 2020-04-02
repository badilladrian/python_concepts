
"""Aqui vamos a ver herencia, lo que es super()
y la diferencia entre method overloading y method overriding
el constructor de python se llama init"""

#esta es mi clase base
class Humano1:
    def __init__(self,nombre,edad):
        self.nombre=nombre #definiendo las propiedades
        self.edad=edad #de la clase


class Humano2:
    #variables globales
    nombre=None
    edad=0

    def __init__(self):#puedo llamar funciones de la misma clase dentro de otra funcion de la misma clase
        self.nombre=self.pedirNombre()#tengo que usar self. para hacer referencia a mis propiedades
        self.edad=18

    def pedirNombre(self):#todo metodo dentro de una clase recibe Self como parametro
        return input("Escriba el nombre: ")

#esta es mi clase que herada Humano 
# -> se envia como parametro en la declaracion
class Trabajor(Humano2):
    salario=7000;
    #creo una funcion para desplegar mis atributos
    def imprimirDatos(self):
        print(self.nombre,self.edad)

    
mi_humano1 = Humano1("Juan",123)
mi_humano2 = Humano2()
print(mi_humano1) 
print((mi_humano2))

mi_trabajador = Trabajor()
print(mi_trabajador.imprimirDatos()) 
print(type(mi_trabajador))



"""el method overriding es cuando cambiamos el comportamiento de un metodo de su padre a hijo
el padre se referencia con super() y por ejemplo Humano2 imprimirDatos()
trabajor imprimirDatos() -> tiene diferente comportamiento print("Yo soy un trabajador")

Method overloading es cuando se le envian diferentes parametros a la misma funcion
Humano2 imprimiDatos(name,edad) --> trabajor imprimirDatos(name,edad,salario)"""