# metodo es una funcion, son las acciones que los objetos pueden hacer

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")

    def cortar(self):
        print(f"cortaste la llamada desde tu: {self.modelo}")
celular1 = Celular("samsung", "s23", "48mp")
celular1.llamar()