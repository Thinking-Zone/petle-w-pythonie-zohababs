import random

def pytaj_o_pogode():
    czy_pada = random.choice([True, False])
    
    print("pada? odpowiedz 'tak' lub 'nie'.")
    
    while True:
        odpowiedz = input("twoja odpowiedz: ").lower()
        
        if odpowiedz not in ['tak', 'nie']:
            print("odpowiedz 'tak' lub 'nie'.")
            continue
        
        if (odpowiedz == 'tak' and czy_pada) or (odpowiedz == 'nie' and not czy_pada):
            print("dobrze")
            break
        else:
            print("nie XD")

pytaj_o_pogode()

#użyłam chatgbt i przerobiłam lekko. wiec rozumiem co tu sie dzieje :)
