# Dawid Sójka 10.03.2021
# Metoda analityczna obliczenia pola powierzchni ze współrzędnych wzorami
# Gaussa
# https://pl.wikipedia.org/wiki/Metoda_analityczna_obliczania_p%C3%B3l

# punkty są podane w zadaniu
punkty = {
    "x": "y",  # 0
    "108.79": "210.45",  # 1
    "120.60": "249.68",  # 2
    "158.43": "246.88",  # 3
    "189.95": "230.76",  # 4
    "NaN1": "NaN",  # 5
    "NaN2": "NaN",  # 6
    "NaN3": "NaN",  # 7
    "NaN4": "NaN",  # 8
    "178.39": "188.38",  # 9
    "138.11": "200.99",  # 10
    "103.43": "203.44",  # 11
    "139.16": "191.53",  # 12
    "174.19": "181.03",  # 13
    "NaN5": "NaN",  # 14
    "NaN6": "NaN",  # 15
    "NaN7": "NaN",  # 16
    "NaN8": "NaN",  # 17
    "162.63": "130.24",  # 18
    "126.90": "123.23",  # 19
    "88.72": "158.96"  # 20
}
# lista musi byc z tymi NaNami - nie wszystkie punkty sa podane,
# a jak zostawie "":"" to to nie liczy się jako element i psuje to indeksy

print(list(punkty.values()))
# punkty.keys() zwraca cos takiego:
#  dict_keys(['x', '108.79', '120.60', '158.43', ''])
# i nie jest to dostepne za pomoca indeksu, wiec zamieniam
# to na liste, która już jest dostępna indeksowo

ile_pkt = int(float(input("ile pkt:")))
print("podaj numery punktow swojej figury po kolei:")
punkty_po_kolei = [int(input("x"+str(x+1)+":")) for x in range(ile_pkt)]
# python list comprehension B) uwielbiam
# tworzy tablice wypełnioną punktami w odpowiedniej kolejności
# [1,10,3,2]


# tutaj rozbiłem to na 3 części, bo nie umiałem zrobić
# kołowej listy, tak żeby na indeksie -1 był ostatni element itd,
# bo potrzebuje w każdym przejściu pętli i+1 i i-1
# taki wzór ¯\_(ツ)_/¯
pole = 0
for i in range(ile_pkt):
    if i == 0:  # dla pierwszego elementu tablicy
        x = float(list(punkty.keys())[punkty_po_kolei[i]])
        y1 = float(list(punkty.values())[punkty_po_kolei[i+1]])
        y2 = float(list(punkty.values())[punkty_po_kolei[len(punkty_po_kolei)-1]])
        pole += x*(y1-y2)
        print(str(i+1)+"x"+"*("+str(y1)+"-"+str(y2)+")="+str(x*(y1-y2)))
    elif i == ile_pkt-1:  # dla ostatniego elementu tablicy
        x = float(list(punkty.keys())[punkty_po_kolei[i]])
        y1 = float(list(punkty.values())[punkty_po_kolei[0]])
        y2 = float(list(punkty.values())[punkty_po_kolei[i-1]])
        pole += x*(y1-y2)
        print(str(i+1)+"x"+"*("+str(y1)+"-"+str(y2)+")="+str(x*(y1-y2)))
# dla każdego elementu innego niż pierwszy/ostatni,
# tak ten skrypt powinien wyglądać
    else:
        x = float(list(punkty.keys())[punkty_po_kolei[i]])
        y1 = float(list(punkty.values())[punkty_po_kolei[i+1]])
        y2 = float(list(punkty.values())[punkty_po_kolei[i-1]])
        pole += x*(y1-y2)
        print(str(i+1)+"x"+"*("+str(y1)+"-"+str(y2)+")="+str(x*(y1-y2)))

print(pole/2)
