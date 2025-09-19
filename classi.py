class Player:
    def __init__(self, name, hp = 100, shield = 5, attack = 7):
        self.name = name
        if hp < 1:
            hp = 100
            print("Valore non valido, ho impostato 100 di HP")
        self.hp = hp
        self.shield = shield
        self.attack = attack 

p1 = Player("Mario")
p2 = Player("Luigi", -80, 6, 5)

print(f"Io sono {p1.name}, ho {p1.hp} di vita, ho {p1.shield} di scudo e ho {p1.attack} di attacco")
print(f"Io sono {p2.name}, ho {p2.hp} di vita, ho {p2.shield} di scudo e ho {p2.attack} di attacco")