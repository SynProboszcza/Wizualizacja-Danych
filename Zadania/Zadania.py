#Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne
"""
int1 = 1
int2 = 2
string1 = "Candy"
string2 = "Strawberry"
float1 = 15.3
float2 = 15.15
complex1 = 1+1j
complex2 = 12+12j

print(int1, int2, string1, string2, float1, float2, complex1, complex2)
"""
#Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
"""
from math import *

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
Pa = sqrt(a)
Pb = sqrt(b)
print("Dla zmiennych %d i %d wyniki są następujące: "%(a, b))
print("Dodawanie a+b = %d" %(a+b))
print("Odejmowanie a-b = %d" %(a*b))
print("Mnożenie a*b = %d" %(a*b))
print("Dzielenie a/b = %d" %(a/b))
print("Potęgowanie a^b = %d" %(a**b))
print("Pierwiastkowanie(stopnia drugiego) sqrt(a) = %d, sqrt(b) = %d" %(Pa, Pb))
print("Dzielenie całkowite a//b = %d" %(a//b))
print("Reszta z dzielenia a%%b = %d" %(a%b))
print("Potęgowanie pow(b,a) = %d" %(pow(b,a)))
print("a++ = %d" %(a+1))
print("b++ = %d" %(b+1))
#print("Zaokrąglenie do całości w gół = %d" %())
#print("Zaokrąglenie do całości w górę = %d" %())
print("sin(a) = %d" %(sin(a)))
print("sin(b) = %d" %(sin(b)))
print("cos(a) = %d" %(cos(a)))
print("cos(b) = %d" %(cos(b)))
"""
#Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
"""
a = 6
b = 12
a+=b
print(a)

a = 6
b = 12
a-=b
print(a)

a = 6
b = 12
a*=b
print(a)

a = 6
b = 12
a/=b
print(a)

a = 6
b = 12
a**=b
print(a)

a = 6
b = 12
a%=b
print(a)
"""
#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
"""
from math import *
print(e**10)
print(log(5+sin(radians(8)**2)**(1/6)))
print(floor(3.55))
print(floor(4.80))
"""
#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)
"""
D = "D"
A = "A"
W = "W"
I = "I"
D = "D"#redundant

S = "S"
O = "Ó"
J = "J"
K = "K"
A = "A"#redundant
imie_i_nazwisko = D + A + W + I + D + " " + S + O + J + K + A
print(imie_i_nazwisko.capitalize())
#nazwisko jest z małej, ale chyba o to chodziło w zadaniu
"""
#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)
"""
Rihanna_Work = "Work, work, work, work, work, work He said me haffi work, work, work, work, work, work He see me do mi dirt, dirt, dirt, dirt, dirt, dirt So me put in work, work, work, work, work, work When you ah gon' learn, learn, learn, learn, learn? Me nuh care if him hurt, hurt, hurt, hurt, hurting"
print(Rihanna_Work)

ilosc_work = Rihanna_Work.count("work")
ilosc_dirt = Rihanna_Work.count("dirt")
ilosc_learn = Rihanna_Work.count("learn")

print("work występiło " + str(ilosc_work) + " razy.")
print("dirt występiło " + str(ilosc_dirt) + " razy.")
print("learn występiło " + str(ilosc_learn) + " razy.")
"""
#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystując indeksy.
"""
dowolna_zmienna_lancuchowa = "Terraria"
print("Druga literka w Terraria to " + dowolna_zmienna_lancuchowa[1])
print("Ostatnia literka w Terraria to " + dowolna_zmienna_lancuchowa[len(dowolna_zmienna_lancuchowa)-1])
"""
#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. (trzeba użyć metody split)
"""
Rihanna_Work = "Work, work, work, work, work, work He said me haffi work, work, work, work, work, work He see me do mi dirt, dirt, dirt, dirt, dirt, dirt So me put in work, work, work, work, work, work When you ah gon' learn, learn, learn, learn, learn? Me nuh care if him hurt, hurt, hurt, hurt, hurting"
print(Rihanna_Work.split(" "))
"""
#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie wyświetl je wykorzystując odpowiednie formatowanie.
"""
s = "Hakuna matata"
f = "2.12"
h = hex(0xF)

print(s)
print(f)
print(h)
"""





