# Ejercicio de herencia y uso de super: Crear un sistema para una 
# escuela. En este sistema,vamos a tener dos clases principales: 
# Persona y Estudiante. La clase Persona tendrá los atributos de nombre
# y edad y un metodo que imprima el nombre y la edad de la persona. La 
# clase Estudiante heredará de la clase Persona y tambien tendra un 
# atributo adicional: grado y un metodo que imprima el grado del 
# estudiante.

# Deberas utilizar super en el metodo de inicializacion(init) para 
# reutilizar el codigo de la clase padre(Persona). Luego crea una 
# instancia de la clase Estudiante e imprime sus atributos y utiliza 
# sus metodos para asegurarte de que todo funciona correctamente.

class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datosPersona(self):
        print(f"El nombre de la persona es {self.nombre}, y su edad es {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def gradoEstudiante(self):
        print(f"La edad del estudiante es: {self.grado}")

estudiante = Estudiante("beatriz", 25, 3)
estudiante.datosPersona()
estudiante.gradoEstudiante()