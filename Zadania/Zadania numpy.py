import numpy as np
#Zad1
#Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.
"""

print(np.arange(3,48,3))

"""

#Zad2
#Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64
"""
a = np.array([4.4,5.8,1.6,1.9,7.2])
b = np.array(a, dtype="int64")
"""
#Zad3
#Napisz funkcję, która będzie:
#•   Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
#•   Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
"""
def foo(n):
    if type(n) != int:
        return -1
    return np.arange(n*n).reshape((n,n))
"""
#Zad4
#Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
"""
def potegi(podstawa, ilosc):
    return np.logspace(1,ilosc,ilosc,base=podstawa)
"""

#Zad5
#Napisz funkcję, która:
#•   Na wejściu przyjmuje jeden parametr określający długość wektora
#•   Na podstawie parametru generuj wektor, ale w kolejności odwróconej
#•   Generuj macierz diagonalną z w/w wektorem jako przekątną
"""
def wektor(n):
    a = np.arange(n,0,-1)
    #lista = np.arange(n*n).reshape((n,n))
    lista = np.zeros((n,n))
    for i in range(int(lista.size/n)):
        lista[i][i] = a[i]
    return lista
"""
#Zad6
#Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.
"""
import numpy as np
rozmiar_wykreslanki = 17
wykreslanka = np.zeros((rozmiar_wykreslanki,rozmiar_wykreslanki),dtype="<U1")
wykreslanka.fill(" ")
slowo1 = "alieny tu sa"
slowo2 = "karta klienta"
slowo3 = " snajperski"
for i in range(len(slowo1)):
    wykreslanka[0][i+1] = slowo1[i*-1-1]


for i in range(len(slowo2)):
    wykreslanka[i+2][1] = slowo2[i]


for i in range(len(slowo3)):
    wykreslanka[i+2][i+3] = slowo3[i]

print(wykreslanka)
"""
#Zad7
#Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
#[[2 4 6]
# [4 2 4]
# [6 4 2]]
#Przy założeniach:
#funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
"""
def macierz2(n):
    a = np.zeros((n,n))
    for i in range(n):
        np.diag(a,)
"""
########################dokonczyc, bo na razie nie wiem jak to zrobic
#np.diag(v,k)
#np.fill_diag
#a = np.zeros((n,n))
#a = np.arange(n*n).reshape((n,n))

#Zad8
#Napisz funkcję, która:
#•   jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
#•   parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
#•   funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)

###################


#Zad9
#Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.
"""
fib_tab = [0,1,1]
for i in np.arange(21,-1,-1):
    fib_tab.append(fib_tab[len(fib_tab)-1]+fib_tab[len(fib_tab)-2])
fib_tab = np.array(fib_tab)
fib_tab = fib_tab.reshape(5,5)
print(fib_tab)
"""





