class Perro:
    # atributos de clase
    especie = "mamifero"

    # atributos de instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# instanciamos la clase Perro
pepe = Perro("Pepe", 3)

# accedemos a los atributos de clase
print("Pepe es " + pepe.__class__.especie)

# accedemos a los atributos de instancia
print(pepe.nombre + " tiene " + str(pepe.edad) + " años de edad")
