import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('penguins.csv', sep=',', index_col=False, encoding='UTF-8')
data = data.dropna()
print(data)
#print(data.to_string()) wypisywanie wszystkich danych
print(data.groupby('sex')['body_mass_g'].mean())
print(data.groupby(['species', 'sex'])['body_mass_g'].mean())
print(data.groupby('island').size().plot.bar())
plt.show()

data2 = data[data['body_mass_g'] == data['body_mass_g'].min()]
data3 = data[data['body_mass_g'] == data['body_mass_g'].max()]
print(data2.to_string())
print(data3.to_string())
print(data.groupby(['island']).size())

dlugosc = data['bill_length_mm']
szerokosc = data['bill_depth_mm']
plec = data['sex']
kolory = ['blue' if p == 'MALE' else 'red' for p in plec]
waga = data['body_mass_g']
gatunek = data['species']
ksztalty = ['v' if g == 'Adelie' else 's' if g == 'Chinstrap' else 'o' for g in gatunek]
rozmiar = (waga/2000)**5

plt.scatter(dlugosc, szerokosc, c=kolory, s=rozmiar, marker=ksztalty)


plt.show()


