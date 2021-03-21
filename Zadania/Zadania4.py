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
import sys

dane = input("Podaj mi trochę tekstu, wpisze go do pliku:")
with open("kilka_linijek.txt", "w", encoding="utf8") as plik:
        plik.write(dane)
plik.close()


with open("kilka_linijek.txt", "r", encoding="utf8") as plik:
    print(plik.read())
plik.close()






