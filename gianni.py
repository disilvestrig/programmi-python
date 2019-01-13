import random
import requests
import time
import json
def accreditamento():
	res = requests.post("http://192.168.1.231:8000/signup",json = {"nome":"AFRICA"})

def shot():
    res = requests.get("http://192.168.1.231:8000/info")
    campo = res.json()["field"]["grid"]
    x = res.json()["field"]["h"]
    y = res.json()["field"]["w"]
    coords = [0,0]
    curcode = 0
    add = 0
    while True:
        while curcode == 120:
            res = requests.get("http://192.168.1.231:8000/info")
            campo = res.json()["field"]["grid"]
            if campo[a+1][b] == 0:
                a+=1
                add -= 1
                res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                while res.json()["code"] == 120:
                    res = requests.get("http://192.168.1.231:8000/info")
                    campo = res.json()["field"]["grid"]
                    a += 1
                    add -= 1
                    if campo[a+1][b] == 0:
                        res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                        print(res.json()["message"])
                if res.json()["code"] != 120:

                    break
            a -= add
            add = 0
            elif campo[a-1][b] == 0:
                a -= 1
                add +=1
                res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                while res.json()["code"] == 120:
                    res = requests.get("http://192.168.1.231:8000/info")
                    campo = res.json()["field"]["grid"]
                    a -= 1
                    add += 1
                    if campo[a-1][b] == 0:
                        res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                        print(res.json()["message"])
                if res.json()["code"] != 120:

                    break
                a += add
                add = 0
            elif campo[a][b+1] == 0:
                b += 1
                add -=1
                res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                while res.json()["code"] == 120:
                    res = requests.get("http://192.168.1.231:8000/info")
                    campo = res.json()["field"]["grid"]
                    b += 1
                    add -= 1
                    if campo[a][b+1] == 0:
                        res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                        print(res.json()["message"])
                if res.json()["code"] != 120:

                    break
                b -= add
                add = 0
            elif campo[a][b-1] == 0:
                b -= 1
                add +=1
                res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                while res.json()["code"] == 120:
                    res = requests.get("http://192.168.1.231:8000/info")
                    campo = res.json()["field"]["grid"]
                    b -= 1
                    add += 1
                    if campo[a][b-1] == 0:
                        res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
                        print(res.json()["message"])
                if res.json()["code"] != 120:

                    break
                b += add
                add = 0




        a = random.randint(0,x)
        b = random.randint(0,y)
        res = requests.get("http://192.168.1.231:8000/info")
        campo = res.json()["field"]["grid"]
        while campo[a][b] != 0:
            a = random.randint(0,x)
            b = random.randint(0,y)
        coords = [a,b]
        res = requests.post("http://192.168.1.231.:8000",json = {"x": coords[0],"y":coords[1]})
        curcode = res.json()["code"]
        if curcode == 120:
            print("nave colpita")
        elif curcode == 130:
            print("nave affondata")
        elif curcode == 150:
            print("Già colpito")
            return
accreditamento()
shot()
