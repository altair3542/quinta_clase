class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} emite un sonido generico")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hablar(self):
        print(f"{self.nombre} ladra... guau guau 🐶")

silvestre = Animal("Aguila")
mascota = Perro("Altair", "Criollito")

silvestre.hablar()
mascota.hablar()
