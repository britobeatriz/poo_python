# Ejercicio de herencia multiple y MRO

# imagina que estás modelando animales en un zoologico. Crear tres 
# clases: "Animal", "Mamifero" y "Ave". La clase Animal debe tener 
# un metodo llamado "comer". La clase "Mamifero" debe tener un 
# metodo llamado "amamentar" y la clase "Ave" un metodo llamado 
# "volar".

# Ahora, crea una clase "Murcielago" que herede de "Mamifero" y 
# "Ave", en ese orden, y por lo tanto debe ser capaz de "amamentar"
# y "volar", ademas de "comer".

# Finalmente, juega con el orden de herencia de la clase 
# "Murcielago" y observa como cambia el MRO y el comportamiento
# de los metodos al usar super().

class Animal():
    def comer(self):
        print("El animal esta comiendo")

class Mamifero(Animal):
    def amamentar(self):
        print("El animal esta amamantando")

class Ave(Animal):
    def volar(self):
        print("El animal está volando")

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.comer()
murcielago.amamentar()
murcielago.volar()

print(Murcielago.mro())