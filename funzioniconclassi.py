from random import randint
class Rettangolo:
    def __init__(self, base, altezza):
        self.base = int(base)
        self.altezza = int(altezza)
        self.area = base * altezza

def get_lato():
    return randint(5, 10), randint(15, 20)
                                                            
R1 = Rettangolo(get_lato()[0], get_lato()[1])
R2 = Rettangolo(get_lato()[0], get_lato()[1])

print(f"Rettangolo 1: Base: {R1.base}, Altezza: {R1.altezza}, Area: {R1.area}")
print(f"Rettangolo 2: Base: {R2.base}, Altezza: {R2.altezza}, Area: {R2.area}")