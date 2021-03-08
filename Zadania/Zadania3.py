#Zad1
"""
A = [1-x for x in range(1,11,1)]
print(A)
B = [4**x for x in range(0,8,1)]
print(B)
C = [x for x in B if x%2==0]
print(C)
"""
#Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1,
# następnie wykorzystując Python Comprehension zdefiniuj nową listę,
# która będzie zawierała tylko parzyste elementy

import random
print(int(random.random()*100))
lista1 = [int(random.random()*100) for x in range(11)]
print(lista1)
lista2 = [x for x in lista1 if x%2==0]
print(lista2)

