import random

def game(x):
    wincount = 0
    for i in range(x):
        player = input("Papier - P, Kamień - K, czy Nożyce - N?: ").lower()
        ai = random.choice(["p", "r", "s"])
        if player == ai:
            print("Remis")
        elif (player == "p" and ai == "k") or (player == "k" and ai == "n") or (player == "n" and ai == "p"):
            print("Wygrałeś!")
            wincount += 1
        else:
            print("Przegrałeś")
    print(f"Koniec Gry: Twój wynik {wincount}/{x}")

game(3)