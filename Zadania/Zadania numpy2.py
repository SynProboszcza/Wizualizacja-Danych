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








