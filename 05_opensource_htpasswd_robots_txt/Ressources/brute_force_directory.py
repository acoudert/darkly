import requests

with open("directory.txt", "r") as f:
    for l in f:
        url = "http://192.168.1.59/" + l[:-1]
        r = requests.get(url)
        if r.status_code == 200:
            print(url)
