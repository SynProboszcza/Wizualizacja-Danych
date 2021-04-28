import numpy as np
import pandas as pd
import xlrd
import openpyxl
"""
s = pd.Series([1,3,5,np.nan,6,8])
#print(s)
s = pd.Series([10,213,123], index=["qwe","asd","zxc"])
print(s)


data = {
    'Kraj':["Belgia","Indie","Brazylia"],
    'Stolica':["Miasto1","Miasto2","Miasto3",],
    'Populacja':[523123,1231231231245,2523412]
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)

daty = pd.date_range('20210324', periods=5)
print(daty)

df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)

"""
"""
df = pd.read_csv("wyniki kolokwium pierwsze.csv", sep=";", header=0)
print(df)
df.to_csv("nowy plik.csv", index=False)
"""
xlsx = pd.ExcelFile('wyniki kolokwium pierwsze.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df.to_excel('wyniki.xlsx', sheet_name="pierwszy arkusz")




