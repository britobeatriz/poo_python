# herencia permite que las clases hijas puede absorber todas las 
# caracteristicas, propiedades de las clases padres

class Persona:
    def __init__(self, nombre, edad, nacionalidad): # funccion constructora
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("hola, estoy hablando un poco")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

roberto = Empleado("roberto", 43, "brasileno", "desarroladora", 200000)
print(roberto.nacionalidad)
roberto.hablar()

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return f"mi habilidad es: {self.habilidad}"

# herencia multiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en: {self.empresa}")

beatriz = EmpleadoArtista("beatriz", 25, "brasilena", "cantar", 300000, "cia")
herencia = issubclass(EmpleadoArtista, Artista) # es una propriedad
instancia = isinstance(beatriz, EmpleadoArtista) # es una propriedad
print(herencia)
print(instancia)

print(beatriz.mostrar_habilidad())
print(beatriz.presentarse())