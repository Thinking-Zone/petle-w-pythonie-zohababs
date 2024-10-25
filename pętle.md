# Python Zajęcia- pętle
Pętle w Pythonie Starter Pack dla Thinking Zone
# Pętelki

W programowaniu, pętla oznacza powtarzanie czegoś wielokrotnie.
Jest ich kilka rodzajów (W zasadzie to więcej, ale na razie ćśś)

- [While loops](#while-loops) Powtarzaj coś, dopóki warunek jest spełniony (jest prawdą).
- [Until loops](#until-loops) Powtarzaj coś, dopóki warunek nie jest spełniony (jest nieprawdą).
- [For loops](#for-loops) Powtarzaj coś dla każdego elementu lub określoną ilość razy.

Pogadamy sobie dzisiaj głównie o nich, w kółko, albo na okrągło, czy tam do upadłego (hehe).

## Pętle While

To poniżej to prosta instrukcja **if** (jeżeli coś to zrób inne coś).

```python
czy_pada = True
if czy_pada:
    print("Jasny Gwint, pada!")
```
Pętla While jest w zasadzie podobna do instrukcji **if**

```python
czy_pada = True
while czy_pada:
    print("Jasny Gwint, pada!")
    # we'll jump back to the line with the word "while" from here
print("O, w sumie już nie pada")
```

Jeśli pętle nie są Ci znajome, to Twoim oczom ukaże się ten oto piękny kawałek tekstu w konsoli:
(Wypróbuj go w pliczku [testowanko.py](testowanko.py))

    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    Jasny Gwint, pada!
    (dużo, dużo więcej deszczu w terminalu...)
    
Przykro mi, od tego komputer nie wybuchnie, chociaż śmiesznie by było.
Jedyne co robi to printuje wciąż to samo, w pętli, w nieskonczoność (no, przynajmniej dopóki się prąd albo miejsce w pamięci nie skończy)
Możemy to przerwać za pomocą klawiszy Ctrl+C

W tym przykładzie, `czy_pada` było **warunkiem**. Jeśli coś w pętli
pętli **While** ustawiłoby wartość `czy_pada` na *False*, pętla
zakończyłaby się, a program wypisałby `O, w sumie już nie pada`.

Spróbujmy stworzyć właśnie taki programik, który to zrobi. Przeklejcie go sobie do [testowanko.py](testowanko.py)

```python
czy_pada = True
while czy_pada:
    print("Jasny Gwint, pada!")
    odpowiedz = input("Czy na pewno? (t=tak, n=nie)")
    if odpowiedz == 't':
        print("No cóż, w końcu jest jesień, to musi padać...")
    elif odpowiedz == 'n':
        czy_pada = False     # kończymy pętlę While
    else:
        print("Cwane, a instrukcja (t=tak, n=nie) to za trudna była?")
print("O, w sumie już nie pada")
```

Running the program may look like this:

    Jasny Gwint, pada!
    Czy na pewno? (t=tak, n=nie) Nie wieeeeem
    Cwane, a instrukcja (t=tak, n=nie) to za trudna była?
    Jasny Gwint, pada!
    Czy na pewno? (t=tak, n=nie) t
    No cóż, w końcu jest jesień, to musi padać...
    Jasny Gwint, pada!
    Czy na pewno? (t=tak, n=nie) n
    O, w sumie już nie pada

Pętla **While** nie sprawdza warunku cały czas, tylko na początku

```python
>>> czy_pada = True
>>> while czy_pada:
...     czy_pada = False
...     print("W sumie to nie pada, ale jeszcze pętla while o tym nie wie")
...
 W sumie to nie pada, ale jeszcze pętla while o tym nie wie
>>>
```

Możemy również przerwać pętlę nawet, jeśli warunek wciąż jest prawdziwy, a tak jak nam się znudzi albo coś innego ważniejszego się wykona, i już nie potrzebujemy, żeby działało.
Robi to słówko `break`. W tym przypadku, ustawimy warunek na *True* i będziemy polegać tylko na tym nowym elemencie `break` żeby się uwolnić

(I want to `break` free)

```python
while True:
    odpowiedz = input("Czy pada? (t=tak, n=nie) ")
    if odpowiedz == 't':
        print("Jasny Gwint, pada!")
    elif odpowiedz == 'n':
        print("O, w sumie już nie pada")
        break   # koniec pętli
    else:
        print("Wpisz t lub n")
```

Program będzie działał mniej więcej tak:

    Czy pada? (t=tak, n=nie) Kto wie, ja nie wiem
    Wpisz t lub n
    Czy pada? (t=tak, n=nie) t
    Jasny Gwint, pada!
    Czy pada? (t=tak, n=nie) n
    O, w sumie już nie pada

W przeciwieństwie do ustawienia warunku na False, "Złamanie" pętli za pomocą `break` kończy ją natychmiast

```python
>>> while True:
...     break
...     print("Nikt mnie nigdy nie wydrukuje :C Smuteczek")
...
>>>
```

## Pętla Until

Tak w zasadzie to takie pętle nie występują w Pythonie, ale możemy użyć czegoś takiego jak
`while not`:

```python
pada = False
while not pada:
    print("Nie pada! yaaay")
    if input("Czy pada (t/n) ") == 't':
        pada = True
print("Padaaaa! Buuuuu :(")
```

## Pętle For

Załóżmy, że mamy [listę](listy.md) rzeczy które chcemy wyświetlić. Żeby wyświetlić każdy element, moglibyśmy to zrobić tak:

```python
lista_zadan = ['Hej', 'jestem', 'to-do', 'listą', 'co miałem zrobić?', 'a, przejrzeć Tik-Toka']

print(lista_zadan[0])
print(lista_zadan[1])
print(lista_zadan[2])
print(lista_zadan[3])
print(lista_zadan[4])
print(lista_zadan[5])
```
Program wypluje nam coś takiego wtedy:

    Hej
    jestem
    to-do
    listą
    co miałem zrobić?
    a, przejrzeć Tik-Toka

To tylko 6 elementów, a jakbyśmy mieli wyświetlić ich 200? Albo więcej? Trzeba to 200 razy skopiować? Trochę bez sensu.
Albo jak pozbędziemy się elementu jakiegoś z listy, żeby było ich mniej niż chcemy wyświetlić. pojawi się nam błąd *"IndexError: list index out of range"*

Na szczęście jest pętla For, która nam w tym pomoże.


```python
lista_zadan = ['Hej', 'jestem', 'to-do', 'listą', 'co miałem zrobić?', 'a, przejrzeć Tik-Toka']

for zadanie in lista_zadan:
    print(zadanie)
```
To sprawi, że ze dla każdego `zadanie` w `lista_zadan` coś zrobimy. Tutaj akurat wyświetlimy. Zamiast słówka `zadanie` możemy wpisać cokolwiek innego, np:

```python
lista_zadan = ['Hej', 'jestem', 'to-do', 'listą', 'co miałem zrobić?', 'a, przejrzeć Tik-Toka']

for nie_wiem_co_tu_wpisac in lista_zadan:
    print(nie_wiem_co_tu_wpisac)
    print("|-----------------------|") #ale ładną tabelkę sobie zrobię hihi
```
W tej pętli `zadanie` oraz `nie_wiem_co_tu_wpisac` jest taką **tymczasową przechowalnią** dla elementów, po których robimy pętlę. Z każdym jej przejściem wstawia się w tą przechowalnię nowy element z listy (To mogą być cyferki, tekst, obiekt i wiele innych rzeczy).

Możemy również zrobić pętlę, która sprawdzi każdą literkę w zdaniu(stringu). Oto przykładzik:

```python
zdanie= "Ale ja lubię się uczyć Pythona, no fantastyczne to jest, zero ironii"
for literka in zdanie:
    print(literka)
```

Albo po prostu wyświetlić coś z jakiegoś zakresu, np. liczbowego  
wyświetlimy dzięki czemu liczby od 200 do 1000 (ale bez 1001 ;))
```python
for liczba in range(200,1001):
    print(liczba)
```


Jeśli możemy po czymś zrobić pętelkę i przejść po wszystkich elementach, to taki element jest **iterowalny**, czyli możemy po nim zrobić **iterację** albo **iterować**

*Iteracja (łac. iteratio – powtarzanie) – czynność powtarzania tej samej operacji w pętli z góry określoną liczbę razy lub aż do spełnienia określonego warunku.*  
#Z Wikipedii uczciwie pod...kradnięte :)

## Podsumowanko

- **Pętla** oznacza powtarzanie czegoś wiele razy.
- Pętle **while** powtarzają coś tak długo, jak warunek jest prawdziwy, i sprawdzają warunek tylko na początku.
- Pętle **For** mogą być używane do powtarzania czegoś dla każdego elementu na liście.
- **Iterować** czyli przejść po kolei po jakichś elementach.
- Słówko kluczowe `break` może być użyte do przerwania wewnętrznej pętli w dowolnym momencie. Dobre do natychmiastowej ewakuacji z pętli lub programu.

## Zadanka!
### Zadanka pisz w odpowiednim pliczku, zadanko 1 ma miejsce w [zadanie1.py](zadanie1.py) i tak dalej... Powodzenia!
1. [zadanie 1](zadanie1.py) . Ten kod powinien wyświetlić numerki 1,2,3,4,5. Napraw go.

    ```python
    things = str([1, 2, 3, 4, 5])
    for thing in things:
        print(thing)
    ```

2. [zadanie 2](zadanie2.py) Napisz program, który wypisze wszystkie liczby od 0 do 9999 (Można wypisać ręcznie jak ktoś chce)
3. [zadanie 3](zadanie3.py) Napisz program, który tym razem wypisz wszystkie liczby z przedziału od 0 do 9999, ale parzyste.  
    > Czyli 0,2,4,6,8,10...9998

4. [zadanie 4](zadanie4.py) Napisz program, który odwróci podany przez użytkownika ciąg znaków. Możesz przekopiować sobie ten kawałek, żeby łatwiej było zacząć
    ```python
    tekst = input("Podaj ciąg znaków: ")
    odwrocony = ""

    #Tu rozwiązanie :)
    ```
5. [zadanie 5](zadanie5.py) Napisz program, który obliczy sumę wszystkich liczb nieparzystych od 1 do 100
6. [zadanie 6](zadanie6.py) Napisz w komentarzu, jaka Twoim zdaniem jest różnica pomiędzy pętlą **for** a pętlą **while**
7. [zadanie 7](zadanie7.py) Napisz program, który będzie pytał użytkownika o pogodę, dopóki użytkownik nie zgadnie poprawnie. Program powinien losować, czy pada, czy nie, i informować użytkownika, czy jego odpowiedź była poprawna. Ten kawałek kodu może Ci pomóc:
    ```python
    import random

    pada = random.choice([True, False]) #Tutaj program losuje którąś z opcji
    zgaduj = True

    while zgaduj:
        odpowiedz = input("Czy pada? (t/n) ")
        #tutaj rozwiązanie
    ```
8. [zadanie 8](zadanie8.py) Napisz program, który będzie liczył, ile razy użytkownik odpowiedział “nie” na pytanie “Czy pada?”. Program powinien zakończyć się, gdy użytkownik odpowie “tak”, i wypisać liczbę odpowiedzi “nie”. Dodaj opcję, jak użytkownik wpisze "nie wiem" to program odpisze "To wyjdź na zewnątrz i się dowiedz." Ten kawałek kodu może Ci pomóc:
    ```python
    pada = False
    licznik_nie = 0
    while not pada:
        print("Nie pada! yaaay")
        odpowiedz = input("Czy pada? (tak/nie) ")
    ```
9. [zadanie 9](zadanie9.py) Napisz program, który znajdzie i wypisze pierwszą liczbę podzielną przez 7 w zakresie od 1 do 100. Program powinien zakończyć działanie natychmiast po znalezieniu takiej liczby, używając słowa kluczowego `break`
10. [zadanie 10](zadanie10.py) Wymyśl jedno zadanie z pętlami w Pythonie i zaproponuj rozwiązanie. O w taki sposób:
    ```python
    #Tutaj treść zadanka w komentarzu
    print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")
    ```