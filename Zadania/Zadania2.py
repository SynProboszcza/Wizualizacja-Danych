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



