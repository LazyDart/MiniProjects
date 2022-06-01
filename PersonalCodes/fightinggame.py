# Dobra to chcemy utworzyć program, w którym
# 1) input użytkownika pozwoli stworzyć postać. GOT IT
# 2) program przechowa informacje z karty postaci GOT IT
# 3) będzie można walczyć postać z postacią i przeciwnik z postacią (player1 v player 2 or player v npc) GOT IT
# 4) postać będzie miała klasę swoją, a klasa będzie miała skille określone, których efektywność będzie podyktowana statystykami z karty postaci GOT IT
from fightinggame_classes import fighter
from time import sleep
from os import path 
from sys import path as path2

lines = []
attributes = []
with open(path.join(path2[0], "fightinggame_Data.txt"), "r+") as file1:
    for line in file1:
        lines.append(line.strip().split())
#tutaj robimy listę list wszystkich atrybutów wszystkich postaci, tak że każdy kolejny element podlisty odpowiada statystykom każdej kolejnej postaci

names = lines[0]
vitality = lines[1]
strength = lines[2]
dexterity = lines[3]
intelligence = lines[4]
klasa = lines[5]
# ^ To tutaj na razie bez zastosowania.. Słownik co jest czym

def createchamp():
    champname = input("Podaj swoje imię: ")
    champclass = input("Wybierz swoją Klasę (Wojownik, Czarownik, Zwiadowca): ")
    if champclass not in ["Wojownik", "Czarownik", "Zwiadowca"]:
        raise ValueError
    freepoints = -1
    while freepoints < 0:
        freepoints = 40
        print("Zaraz rozpoczniesz wypełniać swoje statystyki, suma wydanych punktów, nie może przekroczyć 40. Do wyboru będzie Życie, Siła, Zręczność i Inteligencja")
        champvit = input("Podaj swoje punkty Życia: ")
        champstr = input("Podaj swoje punkty Siły: ")
        champdex = input("Podaj swoje punkty Zręczności: ")
        champint = input("Podaj swoje punkty Inteligencji: ")
        try:    
            freepoints -= int(champvit) + int(champstr) + int(champdex) + int(champint)
        except ValueError:
            freepoints = -1
    lines[0].append(champname)
    lines[1].append(champvit)
    lines[2].append(champstr)
    lines[3].append(champdex)
    lines[4].append(champint)
    lines[5].append(champclass)    

def deletechamp():
    name = input("Którą postać chcesz usunąć?: ")
    delind = lines[0].index(name)
    lines[1].remove(lines[1][delind])
    lines[2].remove(lines[2][delind])
    lines[3].remove(lines[3][delind])
    lines[4].remove(lines[4][delind])
    lines[5].remove(lines[5][delind])
    lines[0].remove(name)

def fight(player1, player2):
    while player1.hp > 0 and player2.hp > 0:
        damage = player1.makeaction()
        player2.hp -= damage
        sleep(0.5)
        print(player2.hp)
        if player2.hp <= 0:
            print(f"Gratulacje {player1.name}!")
            break
        damage = player2.makeaction()
        player1.hp -= damage
        sleep(0.5)
        print(player1.hp)
        if player1.hp <= 0:
            print(f"Gratulacje {player2.name}!")
            break

def initiate():
    close = False
    print("Witaj na Arenie!")
    while close == False:
        prompt = input("Wybierz akcję (d = deletechamp, a = addchamp, f = fight) ").lower()
        if prompt == "d":
            deletechamp()
            if input("Czy chcesz zakończyć? tak/nie ") == "tak":
                close = True
        if prompt == "a":
            createchamp()
            if input("Czy chcesz zakończyć? tak/nie ") == "tak":
                close = True
        if prompt == "f":
            fight(fighter(input(f"{lines[0]} Wybierz postać: "), lines, input("Wybierz typ gracza human/pc: ").lower()), fighter(input(f"{lines[0]} Wybierz postać: "), lines, input("Wybierz typ gracza human/pc: ").lower()))
            if input("Czy chcesz zakończyć? tak/nie ") == "tak":
                close = True

initiate()
with open(filedir, "w") as file1:
    file1.writelines([" ".join(lines[i])+"\n" for i in range(len(lines))])
