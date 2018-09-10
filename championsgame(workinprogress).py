print("Benvenuto al gioco simulatore della Champions League")
print()
print("In questa versione puoi solo disputare amichevoli ma la versione con il torneo uscirà presto")
print()
squadre=["Real Madrid CF","Club Atlètico de Madrid","FC Bayern München","FC Barcelona","Juventus","Sevilla FC","Paris Saint-Germain","Manchester City FC",
"Arsenal FC","Borussia Dortmund","FC Porto","Manchester United FC","Chelsea FC","FC Shaktar Donetsk","SL Benfica","FC Zenit",
"SSC Napoli","FC Basel 1893","Tottenham Hotspur FC","Bayer 04 Leverkusen","AS Roma","Liverpool FC","FC Dynamo Kyiv","FC Shalke 04",
"Olympique Lyonnais","Besiktas JK","AS Monaco FC","FC Salzburg","Olympiacos FC","ACF Fiorentina","AFC Ajax","Villareal CF"]
print("Scegli la tua squadra digitando il numero corrispondente")
import os
for i in range(len(squadre)):
    print(i+1,")",squadre[i])
a = int(input(">>> "))
player = squadre[a-1]
print("Hai scelto",player)
print()
del squadre[a-1]
import random
b = len(squadre)-1
match = []
while len(squadre) > 0:
    if len(squadre) == 31:
        c = player
    else:
        d = random.randint(0,b)
        c = squadre[d]
        del squadre[d]
        b -= 1
    match.append(c)
    d = random.randint(0,b)
    e = squadre[d]
    b -= 1
    del squadre [d]
    match.append(e)
    if b > 29:
        print(c,"-",e)
    print()
fase = 0
pointsA = 0
pointsB = 0
campo = []
for i in range (54):
    if i > 1 and i < 7:
        campo.append("_")
    elif i == 10 or i == 9 or i == 16 or i == 17:
        campo.append("_")
    elif i == 11 or i == 15 or i == 18 or i == 27 or i == 36 or i == 45 or i == 26 or i == 35 or i == 44 or i == 53:
        campo.append("|")
    elif i == 13:
        campo.append("A")
    elif i == 40:
        campo.append("o")
    elif i == 49:
        campo.append("P")
    else :
        campo.append(" ")
for i in range(54):
    print(campo[i],end = "")
    if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 :
        print()
turno = 0
while turno < 6:
    if turno == 0:
        print("Indicazioni:")
        print("Giocatore >>> P")
        print("Computer >>> A")
        print(match[0],"-",match[1])
    if turno % 2 == 0:
        campo[49] = "P"
        campo[40] = "o"
        campo[13] = "A"
        shot = input("Dove tiri (S , C , D) ? >>> ")
        keep = random.randint(1,3)
        os.system('clear')
        campo[13] = "A"
        campo[40] = "o"
        campo[12] = " "
        campo[14] = " "
        campo[21] = " "
        campo[22] = " "
        campo[23] = " "
        for i in range(54):
            print(campo[i],end = "")
            if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 :
                print()
        if shot == "S" and keep == 1:
            campo[40] = " "
            campo[12] = "A"
            campo[13] = " "
            campo[21] = "o"
        elif shot == "C" and keep == 1:
            campo[40] = " "
            campo[12] = "A"
            campo[13] = "o"
            pointsA += 1
        elif shot == "D" and keep == 1:
            campo[40] = " "
            campo[12] = "A"
            campo[13] = " "
            campo[14] = "o"
            pointsA += 1
        elif shot == "S" and keep == 2:
            campo[40] = " "
            campo[12] = "o"
            pointsA += 1
        elif shot == "C" and keep == 2:
            campo[40] = " "
            campo[22] = "o"
        elif shot == "D" and keep == 2:
            campo[40] = " "
            campo[14] = "o"
            pointsA += 1
        elif shot == "S" and keep == 3:
            campo[40] = " "
            campo[12] = "o"
            campo[13] = " "
            campo[14] = "A"
            pointsA += 1
        elif shot == "C" and keep == 3:
            campo[40] = " "
            campo[13] = "o"
            campo[14] = "A"
            pointsA += 1
        elif shot == "D" and keep == 3:
            campo[40] = " "
            campo[14] = "A"
            campo[13] = " "
            campo[23] = "o"
        os.system('clear')
        for i in range(54):
            print(campo[i],end = "")
            if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 :
                print()
        input("premi invio per continuare")
        turno += 1
    else:
        campo[49] = "A"
        campo[40] = "o"
        campo[13] = "P"
        shot = input("Dove ti tuffi (S , C , D) ? >>>")
        keep = random.randint(1,3)
        os.system('clear')
        campo[13] = "P"
        campo[40] = "o"
        campo[12] = " "
        campo[14] = " "
        campo[21] = " "
        campo[22] = " "
        campo[23] = " "
        for i in range(54):
            print(campo[i],end = "")
            if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 :
                print()
        if shot == "S" and keep == 1:
            campo[40] = " "
            campo[12] = "P"
            campo[13] = " "
            campo[21] = "o"
        elif shot == "S" and keep == 2:
            campo[40] = " "
            campo[12] = "P"
            campo[13] = "o"
            pointsB += 1
        elif shot == "S" and keep == 3:
            campo[40] = " "
            campo[12] = "P"
            campo[13] = " "
            campo[14] = "o"
            pointsB += 1
        elif shot == "C" and keep == 1:
            campo[40] = " "
            campo[12] = "o"
            pointsB += 1
        elif shot == "C" and keep == 2:
            campo[40] = " "
            campo[22] = "o"
        elif shot == "C" and keep == 3:
            campo[40] = " "
            campo[14] = "o"
            pointsB += 1
        elif shot == "D" and keep == 1:
            campo[40] = " "
            campo[12] = "o"
            campo[14] = "P"
            campo[13] = " "
            pointsB += 1
        elif shot == "D" and keep == 2:
            campo[40] = " "
            campo[13] = "o"
            campo[14] = "P"
            pointsB += 1
        elif shot == "D" and keep == 3:
            campo[40] = " "
            campo[14] = "P"
            campo[13] = " "
            campo[23] = "o"
        os.system('clear')
        for i in range(54):
            print(campo[i],end = "")
            if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 :
                print()
        if turno == 5:
            input("premi invio per il risultato")
        else :
            input("premi invio per continuare")
        turno += 1
os.system('clear')
print(match[0],pointsA,"-",pointsB,match[1])
