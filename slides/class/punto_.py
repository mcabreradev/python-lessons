import math

class Punto:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
       return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
                print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x == 0 and self.y == 0:
            print("{} se situa en el origen".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} esta situado sobre el eje y".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} esta situado sobre el eje x".format(self))

    def vector(self, p):
        print("el vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))

    def distancia(self, x, y):
        d = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        print(d)

prueba = Punto(3,6)
prueba.cuadrante()
prueba.distancia(4,6)
