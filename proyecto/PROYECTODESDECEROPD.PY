# fases data science 
# recoleccion datos -> limpieza y preparacion 
# -> esplireacion de datos -> creacion del modelo 
# -> evaluacion del modelo  y despliegue 



import pandas as pd
import pickle
from string import ascii_uppercase as alfabeto

# todas las tablas estan separadas en una lista.
todas_tablas = pd.read_html('https://en.wikipedia.org/wiki/2014_FIFA_World_Cup')

# las tablas a trabajar. A->H estan de 7 en el indice de la lista
# print(todas_tablas[11])
# print(todas_tablas[18])
# print(todas_tablas[25])

print(todas_tablas[11].columns[1])


# cambiamos los nombres de las tablas que vamos a trabajar
# y lo guedamos en un nuevo data frame
# alamcenasmos alas tablas en un diccionario con los grupos
dic_tablas = {}
for letra,i in zip(alfabeto, range(11,67,7)):
	df = todas_tablas[i]
	df.rename(columns = {df.columns[1]:'Team'}, inplace = True)
	df.pop('Qualification')
	dic_tablas[f'Grupo{letra}'] = df

print(dic_tablas.keys())

with open('dic_tablas','wb') as output:
	pickle.dump(dic_tablas, output)