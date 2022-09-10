import requests
import json

response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')

if response.status_code != 200:
    raise Exception("Ошибка выполнения запроса!")

hero_dict = json.loads(response.text)

for hero in hero_dict:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        print(hero['name'] + ', интеллект - ' + str(hero['powerstats']['intelligence']))
