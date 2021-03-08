"""
#bawiłem się przed zajęciami
owoce = ["jalbko","banan","kiwi","cytryna","kartofel","mario"]
owoce_z_n = [x.upper() for x in owoce if "n" in x]
liczby_nieparzyste = [x for x in range(1000) if x%2!=0]
imiona = ["dawid","alicja","mariusz","ketchup","zerotwo","michael"]
Imiona = [x.capitalize() for x in imiona]

try:
    print(int('1.0'))
    print("bezbłędnie")
except ValueError:
    print(int(float('1.0')))
    print("błędnie")
"""
"""
lista = [x**2 for x in range(10)]


lista = [3**x for x in range(10)]

liczby_nieparzyste = [x for x in range(1000) if x%2!=0]
#sam sie bawiłem ale podobny przykład był na labach
"""
"""
lista = [x for x in range(1,11,1)]
listy = []
listy = [listy.append(x) for x in lista if x%2!=0]
#co tu sie to ja nawet nie xDDD
"""

"""
lista = []
for i in [1,2,3]:
	for j in [4,5,6]:
		lista.append((i,j))
#to nie działa z jakeigoś powodu, ale zrobione nizej
#w python comprehension dziala
print(lista)

lista = [(i,j) for i in [1,2,3] for j in [4,5,6]]
#[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
"""

"""
slownik = {
	"PZU":"PZU!",
	"ZUS":"ZUS1",
	"PKO":"PKO!"
}
slownik2 = {}
for key, value in slownik.items():
	slownik2[value] = key

print(slownik2)
"""



