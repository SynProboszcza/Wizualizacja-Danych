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
#wiem że to koszmarnie wygląda ale python nie pozwala zrobić czegoś takiego: int('1.0')
#https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
"""

