class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def caminar(self):
        return "{} esta caminando".format(self.nombre)

    def bailar(self):
        if self.sexo == "masculino":
            return "{} esta bailando el robot".format(self.nombre)
        return "{} esta bailando salsa".format(self.nombre)


eric = Persona("Eric", 29, "masculino")
kiss = Persona("Kiss", 25, "femenino")

print(eric.caminar())
print(kiss.caminar())

print(eric.bailar())
print(kiss.bailar())
