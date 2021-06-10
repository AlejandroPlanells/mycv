# scraping/tasks.py
# scraping
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


# scraping function
@shared_task
def stats_user():

# --------------------------------------------




#--------------------------------------------

    stats_list = []
    try:
        print('Starting the scraping tool')
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://faceitstats.com/player/Pucheritoo')
        soup = BeautifulSoup(r.text, 'html.parser')
        # select only the "items" I want from the data

        league_table = soup.find('table', class_='table table-striped table-hover')


        for team in league_table.find_all('tbody'):
            rows = team.find_all('tr')
            for row in rows:
                resultado = row.find_all('td')[0].text
                nom_equipo = row.find_all('td')[1].text
                score = row.find_all('td')[2].text
                K_A_D = row.find_all('td')[3].text
                K_R = row.find_all('td')[4].text
                K_D = row.find_all('td')[5].text
                HS = row.find_all('td')[6].text
                mapa = row.find_all('td')[7].text
                fecha = row.find_all('td')[8].text
                elo = row.find_all('td')[9].text

                stat = {
                    'resultado': resultado,
                    'nom_equipo': nom_equipo,
                    'score': score,
                    'K_A_D': K_A_D,
                    'K_R': K_R,
                    'K_D': K_D,
                    'HS': HS,
                    'mapa': mapa,
                    'fecha': fecha,
                    'elo': elo,
                }

                stats_list.append(stat)
                print('Finished scraping the articles')

                return save_function(stats_list)

    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

# scraping/tasks.py
@shared_task
def save_function(stats_list):
    print('starting')
    new_count = 0

    for stat in stats_list:
        try:
            stat.objects.create(
                resultado=stat['resultado'],
                nom_equipo=stat['nom_equipo'],
                score=stat['score'],
                K_A_D=stat['K_A_D'],
                K_R=stat['K_R'],
                K_D=stat['K_D'],
                HS=stat['HS'],
                mapa=stat['mapa'],
                fecha=stat['fecha'],
                elo=stat['elo'],

            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')