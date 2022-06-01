import random

def comg(x, y):
    low = min(x, y)
    high = max(x, y)
    guess = 0
    feedback = ""
    while feedback != "d":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        
        print(f"Czy to?: {guess}")
        feedback = input("Napisz W jeśli twój numer jest większy, M jeśli mniejszy i D jeśli dobry: ").lower()
        if feedback == "w":
            low = guess + 1
        elif feedback == "m":
            high = guess - 1
    print("Wygrałem!")

comg(1, 1000)