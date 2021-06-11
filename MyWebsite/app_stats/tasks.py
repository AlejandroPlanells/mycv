# tasks.py
# celery worker -A MyProject.celery --loglevel=info --concurrency 1 -P solo               Ejecutar celery
# celery -A MyProject beat -l info             Actualizar cada x tiempo

import requests

from bs4 import BeautifulSoup
from celery import Celery, shared_task
from .models import csgo, lol
from celery.schedules import crontab


app = Celery('tasks')


@shared_task
def save_function_cs(lista_estadisticas):

    delete_stats_cs = csgo.objects.all()
    delete_stats_cs.delete()

    new_count = 0
    for stat in lista_estadisticas:
        try:
            csgo.objects.create(
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
    return print('Guardado del cs finalizado')


@shared_task
def save_function_lol(lista_estadisticas):

    delete_stats_lol = lol.objects.all()
    delete_stats_lol.delete()

    new_count = 0
    for stat in lista_estadisticas:
        try:
            lol.objects.create(
                partida=stat['partida'],
                resultado=stat['resultado'],
                personaje=stat['personaje'],
                img_personaje=stat['img_personaje'],
                score=stat['score'],
                KDA=stat['KDA'],
                duracion=stat['duracion'],
                fecha=stat['fecha'],
                nivel=stat['nivel'],
                minions=stat['minions'],
                ckills=stat['ckills'],
            )
            new_count += 1
        except Exception as e:
            print('Error: latest_article is none')
            print(e)
            break
    return print('Guardado del lol finalizado')


@shared_task
def stats_user_cs():
    stats_list_cs = []
    try:
        print('--------------------------------------------')
        print('Iniciando Scraping del cs')
        # execute my request, parse the data using XML
        # parser in BS4
        r_cs = requests.get('https://faceitstats.com/player/Pucheritoo')
        soup_cs = BeautifulSoup(r_cs.text, 'html.parser')
        # select only the "items" I want from the data

        league_table_cs = soup_cs.find('table', class_='table table-striped table-hover')

        for team_cs in league_table_cs.find_all('tbody'):
            rows = team_cs.find_all('tr')
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

                stat_cs = {
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

                stats_list_cs.append(stat_cs)

            print('Scraping del cs finalizado')
            print('--------------------------------------------')
        return save_function_cs(stats_list_cs)

    except Exception as e:
        print('Algo ha fallado al hacer scrapping del cs. Mira la excepción:')
        print(e)


@shared_task
def stats_user_lol():
    stats_list_lol = []
    try:
        print('--------------------------------------------')
        print('Iniciando Scraping del lol')
        # execute my request, parse the data using XML
        # parser in BS4
        r_lol = requests.get('https://euw.op.gg/summoner/userName=Pucheritoo')
        soup_lol = BeautifulSoup(r_lol.text, 'html.parser')
        # select only the "items" I want from the data

        league_table_lol = soup_lol.find('div', class_='GameItemList')

        for team_lol in league_table_lol.find_all('div', class_='GameItemWrap'):

            partida = team_lol.find_all('div', class_='GameType')[0].text
            resultado = team_lol.find_all('div', class_='GameResult')[0].text
            personaje = team_lol.find_all('div', class_='ChampionName')[0].text
            img_personaje = team_lol.find('img', class_='Image').attrs['src']
            score = team_lol.find_all('span', class_='Kill')[0].text + "/" + team_lol.find_all('span', class_='Death')[0].text + "/" + team_lol.find_all('span', class_='Assist')[0].text
            KDA = team_lol.find_all('span', class_='KDARatio')[0].text
            duracion = team_lol.find_all('div', class_='GameLength')[0].text
            fecha = team_lol.find_all('div', class_='TimeStamp')[0].text
            nivel = team_lol.find_all('div', class_='Level')[0].text
            minions = team_lol.find_all('span', class_='CS tip')[0].text
            ckills = team_lol.find_all('div', class_='CKRate')[0].text

            stat_lol = {
                'partida': partida,
                'resultado': resultado,
                'personaje': personaje,
                'img_personaje': img_personaje,
                'score': score,
                'KDA': KDA,
                'duracion': duracion,
                'fecha': fecha,
                'nivel': nivel,
                'minions': minions,
                'ckills': ckills,
            }

            stats_list_lol.append(stat_lol)
        print('Scraping del lol finalizado')
        print('--------------------------------------------')
        return save_function_lol(stats_list_lol)

    except Exception as e:
        print('Algo ha fallado al hacer scrapping del lol. Mira la excepción:')
        print(e)

