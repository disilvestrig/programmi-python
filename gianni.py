import random
import requests
import time
def accreditamento():
	res = requests.post("http://192.168.1.231:8000/signup",json = {"nome":"AFRICA"})

def shot():
    x = 35
    y = 22
    preshot = []
    coords = [0,0]
    while True:
        a = random.randint(1,35)
        b = random.randint(1,22)
        while [a,b] in preshot:
            a = random.randint(1,35)
            b = random.randint(1,22)
        preshot.append([a,b])
        coords = [a,b]
        res = requests.post("http://192.168.1.231:8000",json = {"x":coords[0],"y":coords[1]})
        print(res)
        time.sleep(3)
