from math import sqrt
from random import randint

class Punto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distanza_origine(self):
        return sqrt(self.x**2 + self.y**2)

    def distanza(self, altro_punto: "Punto"):
        return sqrt(abs(self.x - altro_punto.x)**2 + abs(self.y - altro_punto.y)**2)

    def visualizza(self):
        print(f"({self.x}, {self.y})")

class Rettangolo:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p2.x - self.p1.x)
    
    def altezza(self):
        return abs(self.p2.y - self.p1.y)
    
    def area(self):
        return self.base() * self.altezza()
    
    def contiene(self, punto: Punto):
        if self.p1.x <= punto.x <= self.p2.x and self.p1.y <= punto.y <= self.p2.y:
            return True
        else:
            return False

def ottieni_coordinata():
    return randint(0, 10)

def main():
    print("-- Punti --")
    p1 = Punto(ottieni_coordinata(), ottieni_coordinata())
    p2 = Punto(ottieni_coordinata(), ottieni_coordinata())
    p1.visualizza()
    p2.visualizza()
    print(f"Distanza tra il Punto 1 e l'origine: {round(p1.distanza_origine(), 2)}")
    print(f"Distanza tra il Punto 2 e l'origine: {round(p2.distanza_origine(), 2)}")
    print(f"Distanza tra i 2 punti: {round(p1.distanza(p2), 2)}")
    print("\n-- Rettangolo --")
    rettangolo = Rettangolo(p1, p2)
    print(f"Base: {rettangolo.base()}")
    print(f"Altezza: {rettangolo.altezza()}")
    print(f"Area: {rettangolo.area()}")
    punto_test = Punto(ottieni_coordinata(), ottieni_coordinata())
    print(f"Punto test: ({punto_test.x}, {punto_test.y})")
    if rettangolo.contiene(punto_test):
        print(f"Il rettangolo contiene il punto ({punto_test.x}, {punto_test.y})")
    else:
        print(f"Il rettangolo non contiene il punto ({punto_test.x}, {punto_test.y})")


if __name__ == "__main__":
    main()