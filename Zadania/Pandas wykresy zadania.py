import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad1
#Wykres liniowy - liczba urodzonych dziaci dla każdego roku
"""
df = pd.read_excel('imiona.xlsx', header=0)
#print(df)
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
plt.legend(loc='lower right')
#plt.title('Suma zamówienia dla sprzedawcy')
plt.show()
"""


#Zad2
#Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
"""
df = pd.read_excel('imiona.xlsx', header=0)
#print(df)
grupa = df.groupby(['Plec']).agg({'Plec':['count']})
wykres = grupa.plot.bar()
plt.legend(loc='lower left')
plt.xticks(rotation=0)
plt.show()
"""
#Zadanie 3
#Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
"""
df = pd.read_excel('imiona.xlsx', header=0)
#print(df['Plec'])
grupa = df.groupby(['Liczba']).agg({'Plec':['']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
plt.show()
"""
#Zadanie 4
#Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
"""
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa = df.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
wykres = grupa.plot.bar()
plt.xticks(rotation=0)
plt.show()
"""





