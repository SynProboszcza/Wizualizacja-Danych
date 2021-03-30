"""
class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        #nie rozumiem do końca co robi linijka nizej, ale tak tez dziala
        #Osoba.__init__(self, imie, nazwisko)

        #super().__init__(imie, nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "Jestem {} {} i zarabiam {}.".format(self.imie, self.nazwisko, self.pensja)

class Menadzer(Pracownik):
    def przedstaw_sie(self):
        return "Jestem {} {}, jestem mgmt i zarabiam {}.".format(self.imie, self.nazwisko, self.pensja)

Jozek = Pracownik("Jozek", "Bajka", 2000)
Adrian = Menadzer("Adrian", "Nowak", 12000)

print(Jozek.przedstaw_sie())
print(Adrian.przedstaw_sie())
"""

# for element in range(1,11):
#     print(element)

"""
imie = "Logitech"
it = iter(imie)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    it = iter(imie)
print(next(it))
print(next(it))
print(next(it))
"""

"""
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

gen = reverse("Feliks")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""
"""
litery = (x for x in "QWEASDzxc")
print(litery)
print(next(litery))
print(next(litery))
print(next(litery))
print(next(litery))
print(next(litery))
"""
"""
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

my_gen()

a = my_gen()
next(a)
next(a)
next(a)
"""
def foo(n):
    #pierwsze next(a)
    yield n+1
    #----------
    #drugie next(a)
    print("boczek")
    #----------
    yield n+2
    #trzecie itd
    yield n+3

    yield n+4

a = foo(3)
print(next(a))
print(next(a))
#print(next(a))
#print(next(a))

