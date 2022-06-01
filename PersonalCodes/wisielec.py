import random

from wisielecwords import words
def wisielec(x):
    lives = x
    word = random.choice(words).upper()
    wordletters = list(word)
    goodguesses = 0
    wordlength = len(word.replace("-", ""))
    usedletters = []
    correctletters = []
    if "-" in wordletters:
        correctletters.append("-")
    while lives > 0 and goodguesses != wordlength:
        stan = [letter if letter in correctletters else "_" for letter in word]
        print("".join(stan))
        print("Użyte litery: " + " ".join(usedletters))
        guess = input("Zgadnij literę: ").upper()
        if guess in wordletters:
            correctletters.append(guess)
            goodguesses += 1
        else:
            lives -= 1
        usedletters.append(guess)
    if lives == 0:
        print(f"Przegrałeś! Słowo to: {word}")
    else:
        print("Wygrałeś!")        
wisielec(10)

