# Crear un objeto Estudiante y usar el metodo estudiar(). Debe 
# interactuar con el usuario

# Clase: Estudiante
# Atributos: Nombre, Edad y Grado
# Metodos: estudiar() "el estudiante (nombre) está estudiando"

# al escribir: "estudiar". utilizar el método estudiar()
# (no case sensitive)

# se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante():
    def __init__(self, nombre, edad, grado): # fuccion constructora
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self): # metodo
        print(f"el estudiante {self.nombre} está estudiando.")

nombre = input("Digame su nombre: ")
edade = input("Ahora su edad: ")
grado = input("Por ultimo, su grado: ")

estudiante = Estudiante(nombre, edade, grado) # objeto
print(f"""
    Datos del Estudiante: \n\n
    Nombre: {estudiante.nombre}\n
    Edad: {estudiante.edad}\n
    Grado: {estudiante.grado}\n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break
    else:
        print("Intenta otra vez...")
        