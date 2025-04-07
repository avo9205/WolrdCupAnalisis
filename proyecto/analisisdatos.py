import pandas as pd
import re

df_data_historica	= pd.read_csv('fifa_worldcup_historical_data.csv')
df_misssing_data	= pd.read_csv('fifa_worldcup_missing_data.csv')
df_data_fixture		= pd.read_csv('fifa_worldcup_fixture.csv')

# limpiamos los datos 
# limpiando df_data_fixture
df_data_fixture['home'] = df_data_fixture['home'].str.strip()
df_data_fixture['away'] = df_data_fixture['away'].str.strip()


# limpiando df_misssing_data

# print(df_misssing_data[df_misssing_data['home'].isnull()])
# [64 rows x 4 columns]
df_misssing_data.dropna(inplace = True) 


# concatenamos las tablas de missing_data y data_historica
# print(df_data_historica.shape) antes 
df_data_historica = pd.concat([df_data_historica,df_misssing_data], ignore_index = True) #ignora los indices originales y se toma de cero
# print(df_data_historica.shape) despues

# eliminamos duplicados
df_data_historica.drop_duplicates(inplace = True)
df_data_historica.sort_values('year',inplace = True)


# limpiando df_data_historica
# obtenemos el index que debemos eliminar
index_eliminar = df_data_historica[df_data_historica['home'].str.contains('Sweden') 
	& df_data_historica['away'].str.contains('Austria')].index


# eliminamos el dato que no necesitamos
df_data_historica.drop(index = index_eliminar, inplace = True)
# print(index_eliminar)



# añadimos expresiones regulares 
# print(df_data_historica[df_data_historica['score'].str.contains(r'[^\d-]')])

# remplazamos el texto que no sirve
df_data_historica['score'] = df_data_historica['score'].str.replace(r'[^\d–]', '', regex = True)


#eliminamos los especios enblanco 
df_data_historica['home'] = df_data_historica['home'].str.strip()
df_data_historica['away'] = df_data_historica['away'].str.strip()




# sepramos los datos de score en dos columnas local y visitante
# print(df_data_historica['score'].str.split('–'))
df_data_historica[['HomeGoals','AwayGoals']] = df_data_historica['score'].str.split('–', expand = True)




# df_data_historica['HomeGoal'] = df_data_historica['score'].str.split('').str[0]
# # print(df_data_historica['score'].str.split('').str[1].str.isdigit())
# df_data_historica['AwayGoal'] = df_data_historica['score'].str.split('').str[1]



# eliminamos la columna score
df_data_historica.drop('score', axis = 1, inplace = True) #para columna 1 para fila 0


# renombramos las columnas 
df_data_historica.rename(columns = {'home':'HomeTeam','away':'AwayTeam','year':'Year'}, inplace = True)
# print(df_data_historica.head(10))


# cambiamos el tipo de variables
# print(df_data_historica.dtypes)#nos permite ver el tipo de datos
df_data_historica = df_data_historica.astype({'HomeGoals': int, 'AwayGoals': int})


# creamos una columna con la suma de los goles de local y visitante
df_data_historica['TotalGolas'] = df_data_historica['HomeGoals'] + df_data_historica['AwayGoals']

# print(df_data_historica.head(100))




# Exportamos los dataframes Limpios
# df_data_historica.to_csv('clean_fifa_worldcup_matches.csv', index = False)
# df_data_fixture.to_csv('clean_fifa_worldcup_fixtures.csv', index = False)


# revisamos cuantos mundiales se han jugado 

years = [ 
	"1930",  # Uruguay
    "1934",  # Italia
    "1938",  # Francia
    "1950",  # Brasil
    "1954",  # Suiza
    "1958",  # Suecia
    "1962",  # Chile
    "1966",  # Inglaterra
    "1970",  # México
    "1974",  # Alemania Federal
    "1978",  # Argentina
    "1982",  # España
    "1986",  # México
    "1990",  # Italia
    "1994",  # Estados Unidos
    "1998",  # Francia
    "2002",  # Corea del Sur/Japón
    "2006",  # Alemania
    "2010",  # Sudáfrica
    "2014",  # Brasil
    "2018",  # Rusia
    "2022"   # Catar]
    ]

# print(df_data_historica['Year'].drop_duplicates())

for year in years:
	print(year, len(df_data_historica[df_data_historica['Year'] == int(year)]))