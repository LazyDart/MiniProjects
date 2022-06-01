print("Witaj w naszym programie, pomożemy ci sformułować myśl o twoim przyjacielu, \
\n na podstawie sytuacji z twojego życia")
imie = input("Imię przyjaciela: ")
okreslenie = input("Jaki jest twój przyjaciel?: ")
kiedy = input("Kiedy wydarzyła się sytuacja o której chcesz powiedzieć?: ")
jak = input("W jaki sposób zachował się twój przyjaciel?: ")

madlib = f"Mój najlepszy przyjaciel {imie} jest {okreslenie}, dlatego ze {kiedy} zachowal sie {jak}."
print(madlib)
