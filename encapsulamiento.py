# proteger el acceso directo a los datos y metodos de un 
# objeto exponiendolos de manera controlada atraves de metodos 
# getters y setters

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre  # Protegido (por convención)

    def _saludar(self):        # Método protegido
        return f"Hola, soy {self._nombre}"

persona = Persona("Juan")
print(persona._nombre)  # Se puede acceder, pero no es recomendado.

# muy privado

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Privado

    def obtener_nombre(self):  # Getter
        return self.__nombre

persona = Persona("Juan")
# print(persona.__nombre)  # Error: no se puede acceder directamente
print(persona.obtener_nombre())  # Acceso controlado a través del getter

# convencion: usar un guion bajo antes 
# del nombre