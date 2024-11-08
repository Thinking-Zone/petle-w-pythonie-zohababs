def pytaj_o_pogode():
    liczba_nie = 0
    
    while True:
        odpowiedz = input("Czy pada? (odpowiedz 'tak', 'nie' lub 'nie wiem'): ").lower()
        
        if odpowiedz == 'tak':
            print(f"sigma Odpowiedziałeś 'nie' {liczba_nie} razy.")
            break
        elif odpowiedz == 'nie':
            liczba_nie += 1
            print("SCAM!!! odpowiedź 'nie' zanotowana.")
        elif odpowiedz == 'nie wiem':
            print("To wyjdź na zewnątrz i się dowiedz.")
        else:
            print("odpowiedz 'tak', 'nie' lub 'nie wiem'.")

pytaj_o_pogode()
