# Los atributos son variables que pertenecen a una clase.
# ejemplos

# función constructora
class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("apple", "se", "48mp")
print(celular1.marca)