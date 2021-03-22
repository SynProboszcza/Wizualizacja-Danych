#Zad1
# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
"""
import sys

lista = [x for x in range(1001) if x%4==0]
plik = open("liczby%4", "w", encoding="utf8")
plik.writelines(str(lista))
plik.close()

#Zad2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
plik = open("liczby%4", "r", encoding="utf8")
print(plik.read())
plik.close()
"""


#Zad3
# Wykorzystując komendę with zapisz kilka linijek tekstu
# do pliku a następnie wyświetl je na ekranie.
"""
import sys

dane = input("Podaj mi trochę tekstu, wpisze go do pliku:")
with open("kilka_linijek.txt", "w", encoding="utf8") as plik:
        plik.write(dane)
plik.close()


with open("kilka_linijek.txt", "r", encoding="utf8") as plik:
    print(plik.read())
plik.close()
"""

#Zad4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty: ...
"""
class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = float(ilosc)
        self.jednostka_miary = jednostka_miary
        self.cena_jed = float(cena_jed)
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        print(str(self.ilosc) + str(self.jednostka_miary))
    def ile_kosztuje(self):
        cena = self.ilosc * self.cena_jed
        print(str(cena))





zak = NaZakupy("mleko",10,"litr",12)

# print(zak.nazwa_produktu)
# print(zak.ilosc)
# print(zak.jednostka_miary)
# print(zak.cena_jed)
# niepotrzebne bo wyswietl_produkt()

zak.wyswietl_produkt()
print()
zak.ile_produktu()
print()
zak.ile_kosztuje()
"""

#Zad5
# Utwórz klasę, która definiuje ciągi arytmetyczne.
# Wartości powinny być przechowywane jako atrybut.
# Klasa powinna mieć metody: ...

"""
from math import *

class CiagiA:
    def __init__(self,a1,r,n):
        self.a1 = float(a1)
        self.a2 = float(a1+r)
        self.a3 = float(a1+2*r)
        self.r = float(r)
        self.n = float(n)
    def wyswietl_dane(self):
        print(self.a1)
        print(self.a2)
        print(self.a3)
        print(self.r)
        print(self.n)
    def pobierz_elementy(self):
        self.a1 = float(input("Podaj a1:"))
        self.a2 = float(input("Podaj a2:"))
        self.a3 = float(input("Podaj a3:"))
    def pobierz_parametry(self):
        self.a1 = float(input("Podaj a1:"))
        self.r = float(input("Podaj r:"))
        self.n = float(input("Podaj n:"))
    def policz_sume(self):
        suma = ((2*self.a1+(self.n-1)*self.r)/2)*self.n
        print(suma)
    def policz_elementy(self):
        print(self.a1+(self.n-1)*self.r)


#           (a1,r,n)
ciag = CiagiA(1,1,7)

ciag.wyswietl_dane()
ciag.pobierz_elementy()
ciag.pobierz_parametry()
# ciag.wyswietl_dane()
ciag.policz_sume()
ciag.policz_elementy()
"""

#Zad6
# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka.
# Klasa powinna przechowywać współrzędne x, y, krok
# (stała wartość kroku dla Robaczka) i powinna mieć
# następujące metody: init, lewo/prawo/góra/dół, gdzie_jestes

"""
class Robaczek:
    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self,y):
        self.y += y*self.krok
    def idz_w_dol(self,y):
        self.y -= y*self.krok
    def idz_w_lewo(self,x):
        self.x -= x*self.krok
    def idz_w_prawo(self,x):
        self.x += x*self.krok
    def pokaz_gdzie_jestes(self):
        print("x: " + str(self.x))
        print("y: " + str(self.y))
"""

"""


# klocek = Robaczek(0,0,1)
# klocek.pokaz_gdzie_jestes()
# print(":")
# klocek.idz_w_gore(1)
# klocek.pokaz_gdzie_jestes()
# print(":")
# klocek.idz_w_dol(1)
# klocek.pokaz_gdzie_jestes()
# print(":")
# klocek.idz_w_lewo(1)
# klocek.pokaz_gdzie_jestes()
# print(":")
# klocek.idz_w_prawo(1)
# klocek.pokaz_gdzie_jestes()

# druga żeby sprawdzić czy działa dobrze

# klocek2 = Robaczek(0,0,3)
# klocek2.pokaz_gdzie_jestes()
# print(":")
# klocek2.idz_w_gore(1)
# klocek2.pokaz_gdzie_jestes()
# print(":")
# klocek2.idz_w_dol(1)
# klocek2.pokaz_gdzie_jestes()
# print(":")
# klocek2.idz_w_lewo(1)
# klocek2.pokaz_gdzie_jestes()
# print(":")
# klocek2.idz_w_prawo(1)
# klocek2.pokaz_gdzie_jestes()
"""
