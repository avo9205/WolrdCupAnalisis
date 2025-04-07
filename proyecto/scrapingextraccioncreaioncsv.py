import pandas as pd
import requests
from bs4 import BeautifulSoup

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

def get_matches(year):
	web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
	res = requests.get(web) 

	content = res.text
	soup = BeautifulSoup(content, 'lxml') 

	matches = soup.find_all('div', class_ = 'footballbox')


	home = []
	away = []
	score = []

	for match in matches: 
		home.append(match.find('th' , class_= 'fhome').get_text())
		score.append(match.find('th' , class_= 'fscore').get_text())
		away.append(match.find('th' , class_= 'faway').get_text())


	# insertamos los datos exxtraidos de la pagina a un diccionario
	dict_football = {'home':home , 'score':score ,'away':away}

	# creamo un data frame 
	df_fotball = pd.DataFrame(dict_football)
	df_fotball['year'] = year
	
	return df_fotball

fifa = []
for year in years: 
	fifa.append(get_matches(year))


# metodo concat junta las columnas en un mismo data frame 
df_fifa = pd.concat(fifa, ignore_index = True)
df_fifa.to_csv('fifa_worldcup_historical_data.csv', index = False)


