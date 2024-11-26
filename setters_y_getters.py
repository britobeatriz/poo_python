# Setters y getters son metodos que permiten controlar 
# el acceso a los atributos de una clase.
# Get: obtener
# Set: modificar

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):   # getter
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre
    
bea = Persona("Beatriz", 25)

nombre = bea.get_nombre()
print(nombre)

bea.set_nombre("Bea")
nombre = bea.get_nombre()
print(nombre)