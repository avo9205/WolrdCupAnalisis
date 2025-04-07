import pandas as pd
import pickle
from scipy.stats import poisson



dict_table = pickle.load(open('dic_tablas','rb'))
df_data_historica = pd.read_csv('clean_fifa_worldcup_matches.csv')
df_ficture = pd.read_csv('clean_fifa_worldcup_fixtures.csv')



# print(dict_table['GrupoA'])

# dividir df en df_home y df_away
df_home = df_data_historica[['HomeTeam','HomeGoals','AwayGoals']].copy()	
df_away = df_data_historica[['AwayTeam','HomeGoals','AwayGoals']].copy()


# renombramos columnas 
df_home.rename(columns = {'HomeTeam': 'Team','HomeGoals': 'GoalsScored','AwayGoals': 'GoalsConceded'}, inplace=True)
df_away.rename(columns = {'AwayTeam': 'Team','HomeGoals': 'GoalsConceded','AwayGoals': 'GoalsScored'}, inplace=True)



# concatenamos df_home y df_away, hacer gropu por team  y calcular el promedio
df_team_strength = pd.concat([df_home,df_away], ignore_index = True).groupby('Team').mean()

# print(df_team_strength.head(10))







# aprendiendo pivot 
# print(df_data_historica.head(10))

historico = df_data_historica[['HomeTeam','Year','HomeGoals']]

# realizanod pivo tcon aggfunc = 'sum'
# pivot_test = historico.pivot_table(index = 'Year', columns = 'HomeTeam', aggfunc = 'sum')


# promedio de todo el año
# pivot_test = historico.pivot_table(index = 'Year', columns = 'HomeTeam', margins = True)



print(pivot_test.head(10))
