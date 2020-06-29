class Circulo:
    pi = 3.14

    def __init__(self, radio):
        self.radio = radio

    def __getPi(self):
        return self.pi

    def getArea(self):
        area = (self.radio * self.radio) * self.__getPi()
        return "el area es {} cm2".format(area)

    def getPerimetro(self):
        perimetro = (self.radio * 2) * self.pi
        return "el perimetro es {} cms".format(perimetro)


circulo = Circulo(5)

print(circulo.getArea())
print(circulo.getPerimetro() )
