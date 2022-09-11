import requests
import json
import os.path

# Задача 1
response = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')

if response.status_code != 200:
    raise Exception("Ошибка выполнения запроса!")

hero_dict = json.loads(response.text)

for hero in hero_dict:
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
        print(hero['name'] + ', интеллект - ' + str(hero['powerstats']['intelligence']))


# Задача 2
GIFS_DIR = "gifs"
HEADERS = {"Authorization": "OAuth <TOKEN_HERE>"}

resp1 = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                     params={"path": "/awesome.gif", "owerwrite": "true"},
                     headers=HEADERS)
d1 = resp1.json()
href = d1["href"]

with open(os.path.join(GIFS_DIR, "<FILENAME_HERE>"), "rb") as f:
    resp2 = requests.put(href, files={"file": f})

resp2.raise_for_status()
print("File has been successful uploaded!")
# print(resp2.json())
