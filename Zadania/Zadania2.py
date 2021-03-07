#Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
# a następnie odwróć całą listę. Po odwróceniu listy dodaj kilka pozycji
#(dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać
#10 pozycji)

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




