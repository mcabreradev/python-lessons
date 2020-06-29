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

    def bailar(self):
          if self.sexo == "masculino":
              return "{} esta bailando el robot".format(self.nombre)
          return "{} esta bailando salsa".format(self.nombre)
