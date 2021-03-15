#plik = open(nazwa, tryb, bufor)
import sys
plik = open("test", "r")
#print(plik.read())
linia = ""
for x in plik.read(8):
	linia += x
	if linia == "1zerotwo":
		print("")
plik.close()
#####################tutaj jak jest a+ to sie dopisuje, a jak w to nadpisuje
plik = open("test", "w+", encoding="utf8")
plik.writelines("10zerotwo\n")
plik.writelines("11zerotwo\n")
plik.writelines("12zerotwo\n")
dane = input(":")
plik.writelines(dane + "\n")
plik.close()

with open("test","r",encoding="utf8") as plik:
	for linie in plik:
		print(linie, end="")
plik.close()
