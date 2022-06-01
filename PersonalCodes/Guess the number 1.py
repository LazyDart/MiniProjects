import random

def numg(x):
    rn = random.randint(1, x)
    guess = 0
    trials = 0
    
    while guess != rn and trials < 5:
        guess = int(input(f"Zgadnij numer pomiędzy 1, a {x}: "))
        if rn % guess == 0:
            print(f"{guess} jest niepoprawne, ale {guess} jest wielokrotnością tej liczby.")
        elif rn % guess != 0:
            print(f"{guess} jest niepoprawne i {guess} nie jest wielokrotnością tej liczby")
        trials += 1
    while guess != rn and trials > 4:
        guess = int(input(f"Zgadnij numer pomiędzy 1, a {x}: "))
        if rn % guess == 0 and rn > guess:
            print(f"{guess} jest niepoprawne, ale {guess} jest mniejsze od tej liczby i jest jej wielokrotnością.")
        if  rn % guess == 0 and rn < guess:
            print(f"{guess} jest niepoprawne, ale {guess} jest większe od tej liczby i jest jej wielokrotnością.")
        if rn % guess != 0 and rn > guess:
            print(f"{guess} jest niepoprawne, ale {guess} jest mniejsze od tej liczby i nie jest jej wielokrotnością.")
        if  rn % guess != 0 and rn < guess:
            print(f"{guess} jest niepoprawne, ale {guess} jest większe od tej liczby i nie jest jej wielokrotnością.")
        trials += 1
    
    print(f"Brawo zgadłeś właściwie: {rn}")
    print(f"Ilość prób: {trials}")

numg(100)