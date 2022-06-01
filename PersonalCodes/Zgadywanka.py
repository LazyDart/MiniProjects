import sys
print("Witaj w mojej zgadywance, w której musisz rozwiązywać zagadki")

def zagadka1():
    global stage
    global lives
    global gameon
    while lives == 0:
        print("Przegrałeś, jesteś frajer pompka!")
        stage = 4
        break
    print("Pierwsza zagadka: Nie je, nie pije, ale chodzi i bije.")
    score1 = input("Co to?: ")
    if score1 == "zegar":
        print("Gratulację odgadłeś zagadkę!\n")
        stage += 1
        lives = 3
    elif score1 != "zegar":
        lives -= 1
        print("Błędna odpowiedź, spróbuj ponownie")
        print("Ilość żyć: " + str(lives), "\n")


def zagadka2():
    global stage
    global lives
    global gameon
    while lives == 0:
        print("Przegrałeś, jesteś frajer pompka!")
        stage = 4
    print("Druga zagadka: O poranku chodzi na czterech łapach, w południe na dwóch, a wieczorem na trzech.")
    score2 = input("Co to?: ")
    if score2 == "człowiek":
        print("Gratulację odgadłeś zagadkę!\n")
        stage += 1
        lives = 3
    elif score2 != "człowiek":
        lives -= 1
        print("Błędna odpowiedź, spróbuj ponownie")
        print("Ilość żyć: " + str(lives), "\n")


def zagadka3():
    global stage
    global lives
    global gameon
    while lives == 0:
        print("Przegrałeś, jesteś frajer pompka!")
        stage = 4
    print("Trzecia zagadka: Skrzynia bez zawiasów, klucza i pokrywy,lecz złocisty w środku skarb kryje prawdziwy.")
    score2 = input("Co to?: ")
    if score2 == "jajo" or score2 == "jajko":
        print("Gratulację przeszedłeś grę\n")
        stage += 1
        lives = 3
        gameon = False
    elif score2 != "jajo" or score2 != "jajko":
        lives -= 1
        print("Błędna odpowiedź, spróbuj ponownie")
        print("Ilość żyć: " + str(lives), "\n ")
lives = 3
stage = 1
while stage == 1:
    zagadka1()
while stage == 2:
    zagadka2()
while stage == 3:
    zagadka3()
while stage == 4:
    decision = input("Czy chcesz wyjść z gry: ")
    if decision == "tak":
        sys.exit()
    elif decision == "nie":
        stage = 1
        lives = 3
        zagadka1()
    else:
        print("Błędna odpowiedź")
        decision = input("Czy chcesz wyjść z gry: ")


