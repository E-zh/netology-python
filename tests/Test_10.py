import os.path

import requests
from pprint import pprint

GIFS_DIR = "gifs"

response = requests.get('https://www.reddit.com/r/gifs.json?limit=10', headers={'User-agent': 'Netology'})
if response.status_code != 200:
    raise Exception("Ошибка!")

posts = response.json()["data"]["children"]
for post in posts:
    # pprint(post["data"]["title"])
    title: str = post["data"]["title"]
    title = "".join(x for x in title if x.isalnum() or x.isspace())
    url = post["data"]["url"]
    url = url.replace(".gifv", ".gif")
    if "imgur.com/" not in url:
        continue
    # pprint(post["data"]["url"])
    # print(url)

    gif_resp = requests.get(url)
    gif_resp.raise_for_status()

    # print(os.path.abspath(GIFS_DIR) + ".gif")
    with open(os.path.join(GIFS_DIR, title + ".gif"), "wb") as f:
        f.write(gif_resp.content)
        print(title)

# pprint(data)
