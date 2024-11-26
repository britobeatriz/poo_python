# "muchas formas" de diferentes tipos de objetos responder a
# la misma interfaz(es decir, metodos con el mismo nombre) de 
# distintas maneras.


class Gato():
    def sonido(self):
        return "Miau!!!"
class Perro():
    def sonido(self):
        return "Guau!!!"
    
def hacer_sonido(animal):
    print(animal.sonido())


gato = Gato()
perro = Perro()

hacer_sonido(perro)
hacer_sonido(gato)
print(perro.sonido())
print(gato.sonido())