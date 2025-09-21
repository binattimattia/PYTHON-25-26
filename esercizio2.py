from random import randint
class Rettangolo:
    def __init__(self, base: int,altezza: int):
        self.base = base
        self.altezza = altezza
        self.area  = (base * altezza)
        
    def perimetro(self):
        return (self.base + self.altezza) * 2
    
    def is_quadrato(self):
        return True if self.base == self.altezza else False
    
    def ridimensiona(self, fattore: int):
        self.base *= fattore
        self.altezza *= fattore
        self.area = self.base * self.altezza

    def visualizza(self):
        print(f"La base è {self.base}")
        print(f"L'altezza è {self.altezza}")
        if self.is_quadrato():
            print("Il rettangolo è in realtà un quadrato")
        print(f"L'area è {self.area}")

class Cerchio:
    def __init__(self, raggio: int):
        self.raggio = raggio
        self.area = 3.14 * (raggio ** 2)
        self.circonferenza = round(2 * 3.14 * raggio, 2)

    def visualizza(self):
        print(f"Il raggio è {self.raggio}")
        print(f"L'area è {self.area}")
        print(f"La circonferenza è {self.circonferenza}")

def get_lato():
    return randint(1, 50)

def area_maggiore(area_rettangolo, area_cerchio):
    if area_rettangolo > area_cerchio:
        return "Il rettangolo ha un'area maggiore"
    elif area_rettangolo < area_cerchio:
        return "Il cerchio ha un'area maggiore"
    else:
        return "Le aree sono uguali"

def main():
    print("-- Rettangolo --")
    rettangolo_1 = Rettangolo(get_lato(), get_lato())
    rettangolo_1.ridimensiona(randint(1, 10))
    rettangolo_1.visualizza()
    print("\n-- Cerchio --")
    cerchio_1 = Cerchio(get_lato())
    cerchio_1.visualizza()
    print("\n-- Confronto Aree --")
    print(area_maggiore(rettangolo_1.area, cerchio_1.area))

if __name__ == "__main__":
    main()
