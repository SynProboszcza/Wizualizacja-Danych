import numpy as np
rozmiar_wykreslanki = 10
wykreslanka = np.zeros((rozmiar_wykreslanki,rozmiar_wykreslanki),dtype="<U1")
wykreslanka.fill(" ")
slowo1 = "paluszki"
slowo2 = "cocacola"
slowo3 = "tasma"
for i in range(len(slowo1)):
    wykreslanka[0][i+1] = slowo1[i*-1-1]


for i in range(len(slowo2)):
    wykreslanka[i+2][1] = slowo2[i]


for i in range(len(slowo3)):
    wykreslanka[i+2][i+3] = slowo3[i]

print(wykreslanka)