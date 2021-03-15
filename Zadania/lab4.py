"""
class PierwszaKlasa:
	atrybut = 123
	def metoda(self):
		return True

obiekt = PierwszaKlasa()
print(obiekt.atrybut)
#print(obiekt)
print(obiekt.metoda())
obiekt.tekst = "pipipopo"
print(obiekt.tekst)

#nowyObiekt = PierwszaKlasa()
#print(nowyObiekt.tekst)
#nie dziala xd
"""

class Ksztalt:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.opis = "klasa dla ksztaltow, mimo ze mamy tylko pare dlugosci"
	def pole(self):
		return self.x*self.y
	def suma(self):
		return self.x+self.y
	def obwod(self):
		return 2*self.x+2*self.y
	def dodajOpis(self,text):
		self.opis = text
	def skalowanie(self,czynnik):
		self.x *= czynnik
		self.y *= czynnik

prostakat = Ksztalt(2,5)
print(prostakat.opis)
print(prostakat.pole())
print(prostakat.suma())
print(prostakat.obwod())
prostakat.dodajOpis("zerotwo")
print(prostakat.opis)
prostakat.skalowanie(3)
print(prostakat.pole())
print(prostakat.suma())
print(prostakat.obwod())



