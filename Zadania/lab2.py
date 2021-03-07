"""
lista = ['s', 3, 1, 4, [7, 5, 6, [25, 26, 27]]]
print(lista[4][3][1])
# :O to działa
# żeby c było takie łatwe...
lista.reverse()
print(lista)

nowa = []
nowa.append(7)
print("\nnowa: ")
print(nowa)

nowa.insert(1,15)
nowa.insert(1,15)
nowa.insert(1,15)
print(nowa)

nowa.pop()#tutaj mozna wpisac indeks, bez usuwa ostatni element
print(nowa)

nowa.remove(15)#wykasowało jedno 15
print(nowa)

del nowa[0]
print(nowa)

nowa.extend((1,2,3,4,5,6))#tutaj musza byc dwie pary nawiasow
print(nowa)

nowa.reverse()
print(nowa)

nowa.sort()
print(nowa)
"""

"""
slownik = {1: 111, 2:222, "klucz":"Wartosc"}
print(slownik)
print(slownik["klucz"])

slownik['casio'] = 'kalkulator'
print(slownik['casio'])

slownik.pop(2)
print(slownik)

print(slownik.keys())
print(slownik.values())
"""
"""
if true:
	print("prawda to")
elif
"""

"""
a = input("podaj liczbęłę: ")
b = input("podaj jeszcze jedną liczbęłę: ")
a = int(a)
b = int(b)
if a>b:
    print("pierwsza jest większa")
elif b>a:
    print("druga jest większa")
else:
    print("równe")
"""

"""
for licznik in sekwencja:
	in1
	in2
else:
	print("koniec")
"""

"""
for x in range(1,6,1):
	print(x)
"""

"""
lista = [1,2,3,4,5,6,7,8,9,0]
for x in lista:
	print(x)
"""

"""
z = 0 # wrrrrrrrrrrrrrrrrrr
while z!=10:
	print(z)
	z+=1
else:
	print("\n" + str(z) + " wyswietlen")
"""
"""
lista = [5, 7, 9, 3, 45, 1, 8, 333, 1337, 0, 45, 9, 6, 666, 420, 789, 456, 123]

liczba = input('liczba plsss: ')

licznik = 0
while licznik < len(lista) - 1:
	if int(liczba) - lista[licznik] == 0:
		print("Znalazlem taką liczbę w swojej liście")
		break
	else:
		licznik += 1
"""

"""
lista = [5, 7, 9, 3, 45, 1, 8, 333, 1337, 0, 45, 9, 6, 666, 420, 789, 456, 123]
lista2 = [5, 97, 99, 93, 945, 91, 98, 9333, 91337]
suma = []

for a in lista:
	for b in lista2:
		wynik = a + b
		suma.append(wynik)
print(suma)

# weź pierwszy element pierwszej listy
# weź pierwszy element drugiej listy
# dodaj je i zapisz
# 
# potem weź pierwszy element pierwszej listy
# weź drugi element drugiej listy
# dodaj je i zapisz
# 
# wykonaj dla każdego elementu z drugiej listy
# potem przejdź do drugiego wyrazu z pierwszej listy i powtórz
# 
# 
# 
"""
"""
a = input("daj liczbę: ")
b = input("daj liczbę2: ")

try:
	wynik = int(a)/int(b)
except ZeroDivisionError as e:
	raise e
print(wynik)
"""
a = 15
b = 123
c = 9090
s1 = "show me the {}".format("money")
print(s1)
print('{:d} {:f}'.format(a, b))
print(b)






