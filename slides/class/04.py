class Persona:
    # instance attributes
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    # instancia de metodo
    def caminar(self):
        return "{} esta caminando".format(self.nombre)

    def correr(self):
        return "{} esta corriendo, posta 🤣".format(self.nombre)

    def hizoCaca(self, hizo):
        if(hizo):
            return "{} hizo caca".format(self.nombre)

        return "{} no hizo caca".format(self.nombre)


# creamos la instancia del la clase (el objeto rocky)
migue = Persona("Migue", 35, "masculino")

# call our instance methods
print(migue.caminar())
print(migue.correr())
print(migue.hizoCaca(False))
