import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
s = s.cumsum()
print(s)
s.plot()
plt.show()
"""

"""
data = {'Kraj':['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
        'Kontynent': ['Europa','Azja','Ameryka Południowa','Europa'],
        'Populacja': [11190846,1303171035,207847528,38675467]}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})

wykres = grupa.plot.bar()
wykres.set_xlabel("Kontynenty")
wykres.set_ylabel("Populacja w mld")
wykres.legend()

plt.title('Populacja z podziałem na kontynenty')
plt.xticks(rotation=0)
plt.savefig('wykres.png')
plt.show()
"""
"""
#coś tu nie działa, ale nie wiem co
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
#print(df)
grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia'})
wykres = grupa.plot.pie(subplots=True, autopot='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0,0 ))
plt.legend(loc='lower right')
plt.title('Suma zamówienia dla sprzedawcy')
plt.show()
"""

"""
s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
s = s.cumsum()

df = pd.DataFrame(s)
df['MA'] = df.rolling(window=100).mean()
df.plot()
plt.show()
"""


########################
#tuaj robimy już wykresy z plt
"""
plt.plot([1,2,3,4,5,6,7,8,98])
plt.ylabel('liczby')
plt.show()
"""
"""
#plt.plot(x,y, kolorki i styl punktów)
plt.plot([1,2,3,4,5,6,7,8,9],[2,4,6,8,10,12,14,16,18], 'ro-')
plt.axis([0,6,0,20]) # skąd widać "kamerę" wykresu (domyślne jej miejsce)
plt.show()
"""
"""
plt.plot([x for x in range(10)], [x**2 for x in range(10)], 'r')
plt.plot([x for x in range(10)], [x**2 for x in range(10)], 'o')
        #[x1y1x2y2]
plt.axis([0,6,0,20]) # skąd widać "kamerę" wykresu (domyślne jej miejsce)
plt.show()
"""
"""
t = np.arange(0, 5, 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
#r-- red przerywana
#bs blue square
#g^ green trójkąt

plt.show()
"""
"""
x = np.linspace(0,2,100)
plt.plot(x,x,label="Postać liniowa")
plt.plot(x,x**2,label="Postać kwadratowa")
plt.plot(x,x**3,label="Postać sześcienna")
plt.xlabel('etykieta X')
plt.ylabel('etykieta Y')
plt.legend()
plt.title('Prosty wykres')

plt.show()
"""
x = np.arange(1, 10, 0.1)
s = np.sin(x)
plt.plot(x,s, label='sinus od x')
plt.legend()
plt.title('Wykres sin(x)')
plt.ylabel('y')
plt.xlabel('x')


plt.show()



