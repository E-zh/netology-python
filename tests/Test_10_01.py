import os.path

import requests
from pprint import pprint

GIFS_DIR = "gifs"
HEADERS = {"Authorization": "OAuth <TOKEN_HERE>"}

# Get list of directories and files from Yandex.Disk
response = requests.get("https://cloud-api.yandex.net/v1/disk/resources",
                        params={"path": "/"},
                        headers=HEADERS)
response.raise_for_status()
data = response.json()
for file in data["_embedded"]["items"]:
    print(file["name"])

# Upload file on Yandex.Disk
resp1 = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                     params={"path": "/_Test/awesome.gif", "owerwrite": "true"},
                     headers=HEADERS)
d1 = resp1.json()
href = d1["href"]

with open(os.path.join(GIFS_DIR, "Star Gazer collaboration with ufox.gif"), "rb") as f:
    resp2 = requests.put(href, files={"file": f})

resp2.raise_for_status()
print("File has been successful uploaded!")
# print(resp2.json())
