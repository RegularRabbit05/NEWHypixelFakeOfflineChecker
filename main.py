import requests

username = "THE NAME"
api_key = "YOUR KEY"

cached = ""
while True:
    url = 'https://api.hypixel.net/player?name=' + username + '&key=' + api_key
    r = requests.get(url)
    if cached != "":
        if cached != r.text:
            print("Change detected, user may be online!")
        else:
            print("No changes detected, most likely offline...")
    cached = r.text
