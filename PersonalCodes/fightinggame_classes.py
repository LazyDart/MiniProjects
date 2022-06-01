#Tutaj umieszczę class Fighter, którą będzie mógł przyjąć albo Gracz albo komputer, oraz stworzę klasy, które będą pozwalały castować skille skalowane ze statystykami postaci.
import random

class Klasa():
    def __init__(self, typ):
        self.typ = typ
        self.availableactions = []
    #Klasy Wojownik, Czarownik, Zwiadowca

        if self.typ == "Wojownik":
            self.availableactions = ["miecz"]

        elif self.typ == "Czarownik":
            self.availableactions = ["kostur"]

        else:
            self.availableactions = ["łuk"]       


class fighter():
    def __init__(self, name, lines, player):
        self.player = player
        self.name = name
        self.textind = lines[0].index(name)
        self.hp = int(lines[1][self.textind])*10
        self.strength = int(lines[2][self.textind])
        self.dexterity = int(lines[3][self.textind])
        self.intelligence = int(lines[4][self.textind])
        self.klasa = Klasa(lines[5][self.textind])
        self.availableactions = self.klasa.availableactions

    def action(self, action):
        actlist = ["miecz", "kostur", "łuk"]
        damage = [self.strength + random.randint(0, 12), self.intelligence + random.randint(0, 12), self.dexterity + random.randint(0, 12)]
        return damage[actlist.index(action)]

    def makeaction(self):
        if self.player == "human":
            move = input("Wybierz akcję: " + ", ".join(self.availableactions) + " ").lower
            if move in self.availableactions:
                return self.action(move)
        
        if self.player == "pc":
            move = random.choice(self.availableactions)
            return self.action(move)

