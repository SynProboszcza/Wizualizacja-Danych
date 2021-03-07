#Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
# a następnie odwróć całą listę. Po odwróceniu listy dodaj kilka pozycji
#(dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać
#10 pozycji)
"""
ulubione_filmy = ["Shrek","The Walking Dead","Black Mirror","La Casa De Papel","Joker","Breaking Bad"]
#["Rick and Morty","Avatar: Legenda Aanga","Mindhunter","Kakegurui"]
print(ulubione_filmy)
ulubione_filmy.reverse()
print(ulubione_filmy)
ulubione_filmy.insert(5,"Rick and Morty")
ulubione_filmy.insert(6,"Avatar: Legenda Aanga")
ulubione_filmy.insert(7,"Mindhunter")
ulubione_filmy.insert(8,"Kakegurui")
#ulubione_filmy.insert(9,"RickMorty")
print(ulubione_filmy)
print(len(ulubione_filmy))
"""
#Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1. Pomyśl co może być kluczem
"""
#slownik = {"klucz":"wartosc"}
#ulubione_filmy = ["Shrek","The Walking Dead","Black Mirror","La Casa De Papel","Joker","Breaking Bad"]
#["Rick and Morty","Avatar: Legenda Aanga","Mindhunter","Kakegurui"]
slownik = {
	"tytul1":"Shrek",
	"tytul2":"The Walking Dead",
	"tytul3":"Black Mirror",
	"tytul4":"La Casa De Papel",
	"tytul5":"Joker",
	"tytul6":"Breaking Bad",
	"tytul7":"Rick and Morty",
	"tytul8":"ShAvatar: Legenda Aangarek",
	"tytul9":"Mindhunter",
	"tytul10":"Kakegurui"
}
print(slownik)
#wrocic do tego, nie rozumiem o co chodzi z tym kluczem bo nie moze on byc duplikatem
"""
#Zad 3. Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów z obecnego semestru oraz ich skrótami. Policz liczbę elementów w słownik
"""
przedmioty = {
	"Wizualizacja danych":"WD",
	"CAD komputerowe wspomaganie programowania":"CAD-kwp",
	"Przedmiot humanizujący":"human",
	"Język angielski":"angol",
	"Rachunek różniczkowy i całkowy":"rachun",
	"Elementy matematyki dyskretnej":"matma",
	"Programowanie strukturalne":"PS"
}
print(przedmioty)
print(len(przedmioty))
"""

#Zad 4. Napisz skrypt gdzie wczytasz liczbę dowolnego typu i podnieś ją do tej samej potęgi. Użyj funkcji input.
"""
wejscie = input("Podaj dowolną liczbęłę:")
if float(wejscie)==int(float(wejscie)):
	print("Int")
	print((int(float(wejscie)**int(float(wejscie)))))
else:
	print("Float")
	print((float(wejscie)**float(wejscie)))
#wiem że to koszmarnie wygląda ale python nie pozwala zrobić czegoś takiego: int('1.0'), za to int(1.0) idzie normalnie,
#dlatego najpierw rzutuje do floata, a potem z floata do inta
#https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
"""
#Zad 5. Napisz skrypt gdzie wczytasz dowolny ciąg znaków, i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).

"""
import sys as system
wejscie = system.stdin.readline()
system.stdout.write(str(wejscie.count("a")))
"""

#Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a%2==0 and b>c:
	print("a jest parzysta i b>c")
elif a%2==0:
	print("a jest parzysta, ale b!>c")
elif a%2!=0 and b>c:
	print("a jest nieparzysta, ale b>c")
elif a%2!=0:
	print("a jest nieparzysta, i b!>c")
"""

#Zad 8. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą pętli for oblicz sumę elementu obecnego z poprzednim.
"""
lista = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5]
#print(len(lista))
for i in range(1,len(lista),1):
	print(lista[i]+lista[i-1])
"""
#Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, a następnie dodaje do listy tylko liczby całkowite
"""
lista_intow = []
lista_do_sprawdzenia = []
i = 0
while i<10:
	lista_do_sprawdzenia.append(input("Podaj " + str(i+1) + " liczbe:"))
	#print(i)
	i+=1

print(lista_do_sprawdzenia)
#i=0
for i in range(0,len(lista_do_sprawdzenia),1):
	#if type(lista_do_sprawdzenia[i])==int:
	if int(float(lista_do_sprawdzenia[i])) == float(lista_do_sprawdzenia[i]):
		lista_intow.append(int(float(lista_do_sprawdzenia[i])))

print(lista_intow)
"""

#Zad 9. Napisz skrypt, który rysuje następującą literę
"""
OOOOOO
O    O
O    O - 6x6 o
O    O
O    O
OOOOOO
Etapy wykonania ćwiczenia:
Deklarujemy jedną następującą listę [1,2,3,4,5,6]. 
Następnie za pomocą pętli i instrukcji warunkowej wykonujemy odpowiednie działania. 
Trzeba wykorzystać zagnieżdżenia.
"""
"""
lista = [1,2,3,4,5,6]
for i in lista:
	if i == 1 or i == 6:
		print("O"*6)
	elif i == 2 or i == 3 or i == 4 or i == 5:
		print("O    O")
#nie wiem czy prawidłowo zrozumiałem zadanie
"""

