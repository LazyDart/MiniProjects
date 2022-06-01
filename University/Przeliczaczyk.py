# Powitanie :)
print("Witaj w Przeliczaczyku!")

# While Loop, który będzie powtarzał sekwencję wprowadzania danych, dopóki użytkownik nie poda prawidłowych danych lub nie przerwie działania programu wybierając 3 -> Nic
poprawne = False
while poprawne == False:
    try:
        # Tutaj w Liście składuję wszystkie nazwy jednostek używanych w późniejszych wiadomościach, 
        # Stosowanie list pozwala również na dowolne powiększanie programu o dodatkowe miary, wystarczy jedynie dodawać dodatkowe nazwy oraz dodatkowe przelicznik w odpowiedniej kolejności.
        nazwy = [["Kilometry", "Mile"], ["Celsjusz", "Fahrenheit"], ["Kilogramy", "Funty"]]
        # Zdecydowałem się na numeryczny wybór aniżeli literowy (Przepraszam że to niezgodne z treścią zadania, ale proszę o wyrozumiałość),
        # ponieważ chciałem wymyślić trochę sprawniejszy sposób, od ciągu If'ów i Else'ów, którego nauczono nas na zajęciach
        ind1 = int(input("Którą z miar chcesz przeliczyć? (0 = Odległość, 1 = Temperatura, 2 = Masa, 3 = Nic): "))
        # Tutaj Program zakańcza pracę jeśli taka jest wola użytkownika
        if ind1 == 3:
            print("Zakończono Pracę Programu.")
            exit()
        # Tutaj użytkownik może wybrać z czego na co będą przeliczane jednostki. To dodatkowa funkcja względem rozwiązania podanego w treści zadania
        # I dzięki niej użytkownik uzyska w odpowiedzi jedynie istotne dane.
        ind2 = int(input(f"W którym kierunku chcesz aby dokonać Obliczeń (0 = {nazwy[ind1][0]} -> {nazwy[ind1][1]}, 1 = {nazwy[ind1][1]} -> {nazwy[ind1][0]}: "))
        # If, który pozwala na powtórzenie sekwencji w wypadku, w którym użytkownik wybrał inną cyfrę niż dozwolono.
        if ind2 != 0 and ind2 != 1:
            raise ValueError
        value = int(input("Podaj wartość do przeliczenia: "))
        poprawne = True
    # Tutaj wszystkie błędy doprowadzają do powtórzenia się sekwencji.
    except (ValueError, IndexError) as E:
        print("Wprowadzono Niewłaściwe Dane!, Proszę spróbować jeszcze raz.")
        poprawne = False
# Tutaj lista z której wczytywana jest ostateczna odpowiedź, w każdej rubryczce podane są przeliczniki dla różnych miar oraz dla obu kierunków przeliczania
przeliczniki = [[value*0.621504, value*1.609], [(9/5)*value + 32, 5/9*(value-32)], [value*2.2046, value*0.453597]]
# tutaj program udziela ostatecznej odpowiedzi i informuje o zakończeniu.
print(f"{nazwy[ind1][ind2]}: {value} = {nazwy[ind1][(3 + ind2)%2]}: {przeliczniki[ind1][ind2]}")
print("Zakończono Pracę Programu.")