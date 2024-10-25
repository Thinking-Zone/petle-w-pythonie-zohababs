import random

pada = random.choice([True, False])
zgaduj = True
while zgaduj:
    odpowiedz = input("Czy pada (t/n) ")
    if (odpowiedz == 't' and pada) or (odpowiedz == 'n' and not pada):
        print("Zgadłeś! :)")
        zgaduj = False
    else:
        print("Nie zgadłeś, spróbuj ponownie.")
print("Koniec gry.")