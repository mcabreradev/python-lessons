class Perro:
    # atributos de clase
    especie = "mamifero"

    # atributos de instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# instanciamos la clase Perro
pepe = Perro("Pepe", 3)
sasha = Perro("Sasha", 5)
tomy = Perro("Tomy", 1)

# accedemos a los atributos de clase
print("Pepe es " + pepe.__class__.especie)
print("Sasha es " + sasha.__class__.especie)
print("Tomy es " + tomy.__class__.especie)

# accedemos a los atributos de instancia
print(pepe.nombre + " tiene " + str(pepe.edad) + " años de edad")
print(sasha.nombre + " tiene " + str(sasha.edad) + " años de edad")
print(tomy.nombre + " tiene " + str(tomy.edad) + " años de edad")
