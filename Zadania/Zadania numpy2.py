import numpy as np
#Zad1
#Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
"""
x1 = np.array([1,2,3])
x2 = np.array([4,4,4])
print(np.multiply(x1,x2))
"""
#Zad2
#Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
"""
tab1 = np.arange(3*3).reshape((3,3))
tab2 = np.arange(4*4).reshape((4,4))
for i in range(3):
    print("Najmniejsza wartosc w "+str(i+1)+" rzedzie: "+str(tab1[i].min()))
for i in range(4):
    print("Najmniejsza wartosc w "+str(i+1)+" rzedzie: "+str(tab2[i].min()))

for i in range(3):
    print("Najmniejsza wartosc w "+str(i+1)+" kolumnie: "+str(tab1[:,i].min()))
for i in range(4):
    print("Najmniejsza wartosc w "+str(i+1)+" kolumnie: "+str(tab2[:,i].min()))
"""
#Zadanie 3
#Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.
"""
tab1 = np.arange(4*4).reshape((4,4))
tab2 = np.arange(4*4).reshape((4,4))
tab3 = np.matmul(tab1, tab2)
print(tab3)
"""

#Zadanie 4
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.
"""
macierz1 = np.array([2,4,6])
macierz2 = np.array([3.0,5.0,8.1])
print(macierz1*macierz2)
"""

#Zadanie 5
#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.
"""
a=[]
macierz = np.array([[15,30,45],[60,75,90]])
print(macierz)
for i in macierz:
    for j in i:
        a.append(np.sin(j))
#        a.append(np.sin(j*np.pi/180))
#        zamiana na stopnie

print(a)
"""

#Zadanie 6
#Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
"""
b=[]
macierz = np.array([[115,130,145],[160,175,190]])
print(macierz)
for i in macierz:
    for j in i:
        b.append(np.sin(j))
#        b.append(np.sin(j*np.pi/180))
#        zamiana na stopnie

print(b)
"""

#Zadanie 7
#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
"""
a=[]
macierz = np.array([[15,30,45],[60,75,90]])
#print(macierz)
for i in macierz:
    for j in i:
        a.append(np.sin(j))

b=[]
macierz = np.array([[115,130,145],[160,175,190]])
#print(macierz)
for i in macierz:
    for j in i:
        b.append(np.sin(j))

print(a)
print(b)
print(np.add(a,b))
"""

#Zadanie 8
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
"""
macierz = np.arange(3*3).reshape((3,3))
for i in macierz:
    print(i)
"""

#Zadanie 9
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())
"""
macierz = np.arange(3*3).reshape((3,3))
for i in range(macierz.size):
    print(macierz.flat[i])
"""

#Zadanie 10
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
"""
macierz = np.arange(9*9).reshape((9,9))
print(macierz)
macierz = np.arange(9*9).reshape((1,81))
print(macierz)
macierz = np.arange(9*9).reshape((81,1))
print(macierz)
macierz = np.arange(9*9).reshape((27,3))
print(macierz)
macierz = np.arange(9*9).reshape((3,27))
print(macierz)

#81 = 3*3*3*3
#Mamy 81 elementów i żeby zmienić rozmiar możemy używać tylko
#prostokątów i wymiarach, które odpowiadają wielokrotności 3
#można używać tylko składowych 81, a 81 jest potęgą 3
"""

#Zad11
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?
"""
wektor = np.array(np.arange(12))
print("Oryginał:\n"+str(wektor))
wektor = wektor.flatten()
print("Oryginał(spłaszczony):\n"+str(wektor))
print(np.array(np.arange(12))==wektor)

wektor = np.array(np.arange(12))
wektor = wektor.reshape((3,4))
print("3x4:\n"+str(wektor))
wektor = wektor.flatten()
print("3x4(spłaszczony):\n"+str(wektor))
print(np.array(np.arange(12))==wektor)

wektor = np.array(np.arange(12))
wektor = wektor.reshape((4,3))
print("4x3:\n"+str(wektor))
wektor = wektor.flatten()
print("4x3(spłaszczony):\n"+str(wektor))
print(np.array(np.arange(12))==wektor)

wektor = np.array(np.arange(12))
wektor = wektor.reshape((2,6))
print("2x6:\n"+str(wektor))
wektor = wektor.flatten()
print("2x6(spłaszczony):\n"+str(wektor))
print(np.array(np.arange(12))==wektor)
#tak, są takie same
"""




