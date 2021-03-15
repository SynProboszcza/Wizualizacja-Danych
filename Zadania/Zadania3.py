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
"""
import random
print(int(random.random()*100))
lista1 = [int(random.random()*100) for x in range(11)]
print(lista1)
lista2 = [x for x in lista1 if x%2==0]
print(lista2)
"""

#Zad3
# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu,
# a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy,
# gdzie będą produkty, których wartość to sztuki.


"""
produkty = {
	"Cukierki":"sztuki",
	"Draże":"paczka",
	"Gra komputerowa":"sztuki",
	"Lays Paprykowe":"paczka",
	"KitKat":"sztuki",
	"Cheetos Spirals":"paczka",
	"McNuggets":"sztuki",
	"Popcorn maślany":"paczka",
	"Draże z orzechami":"sztuki",
	"Masło":"kostka",
	"Cukierki pudrowe":"kg",
	"Ser":"kg",
	"Szynka":"plastry",
	"Mleko":"l",
	"Woda gazowana":"butelka",
	"Woda niegazowana":"butelka",
	"Tymbark jabłko-mięta":"butelka",
	"Caprio":"karton"
}

sztuki = [list(produkty.keys())[x] for x in range(len(produkty)) if list(produkty.values())[x] == "sztuki"]
print(sztuki)
"""

#Zad 4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
"""
def czyProstokatny(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	elif a**2 + c**2 == b**2:
		return True
	elif c**2 + b**2 == a**2:
		return True
	else:
		return False

print(czyProstokatny(3,4,5))
print(czyProstokatny(5,12,13))
"""



#Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
"""
def poleTrapezu(a=9,b=4,h=12):
	print(((a+b)*h)/2)

poleTrapezu()
poleTrapezu(5,1,10)
"""

"""
#Zad6
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
def iloczynElementowCiagu(a1=1,b=4,ile=10):
	if b!=1:
		S = a1*((1-b**ile)/(1-b))
	else:
		S = a1*ile

	print(S)


iloczynElementowCiagu()
iloczynElementowCiagu(1,2,5) # spodziewane 31
"""
#Zad7



#Zad8
# Napisz funkcję, która wykorzystuje symbol **.
# Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.
"""
def cenaZakupow(lista):
	# "nazwa":"koszt"
	print("Liczba kupionych rzeczy: " + str(len(lista)))
	suma = 0.0
	for x in range(len(lista)):
		suma += float(list(lista.values())[x])
	print("Cena kupionych rzeczy: " + str(suma))


produkty = {
	"Cukierki":"5.00",
	"Draże":"7.00",
	"Gra komputerowa":"2.05",
	"Lays Paprykowe":"6.00",
	"KitKat":"4.00",
	"Cheetos Spirals":"1.00",
	"McNuggets":"7.00",
	"Popcorn maślany":"8.00",
	"Draże z orzechami":"9.00",
	"Masło":"6.00",
	"Cukierki pudrowe":"5.00",
	"Ser":"4.00",
	"Szynka":"6.00",
	"Mleko":"1.00",
	"Woda gazowana":"5.00",
	"Woda niegazowana":"7.00",
	"Tymbark jabłko-mięta":"9.00",
	"Caprio":"3.00"
}

cenaZakupow(produkty)
"""






