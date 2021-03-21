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
print(plik.read(3))
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





