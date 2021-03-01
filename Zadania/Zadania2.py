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
slownik = {1: 111, 2:222, "klucz":"Wartosc"}
print(slownik)
print(slownik["klucz"])

slownik['casio'] = 'kalkulator'
print(slownik['casio'])

slownik.pop(2)
print(slownik)

print(slownik.keys())
print(slownik.values())







