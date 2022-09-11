import requests

URL = "https://api.vk.com/method/users.get"
params = {
    "user_id": "1",
    "access_token": "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c",
    "v": "5.131"
}

response = requests.get(URL, params=params)
print(response.json())
