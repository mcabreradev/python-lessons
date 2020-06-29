class Perro:
    especie= "mamifero"

    # instance attributes
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # instancia de metodo
    def ladrar(self):
        return "{} esta ladrando".format(self.nombre)

    def darLaPata(self):
        return "{} esta dando la pata".format(self.nombre)

    def hizoCaca(self, hizo):
        if(hizo):
            return "{} hizo caca".format(self.nombre)

        return "{} no hizo caca".format(self.nombre)

    def mostrarEdad(self):
        return "{} tiene {} de edad".format(self.nombre, self.edad)

    def calcularEdadHumana(self):
        edad = self.edad * 7
        return "{} tiene {} años de humano".format(self.nombre, edad)


# creamos la instancia del la clase (el objeto rocky)
rocky = Perro("Rocky", 7)

# call our instance methods
print(rocky.ladrar())
print(rocky.darLaPata())
print(rocky.hizoCaca(True))
print(rocky.mostrarEdad())
print(rocky.calcularEdadHumana())
