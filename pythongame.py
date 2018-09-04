print("RUBENTUS GAME")
print("Obiettivo: ruba il tesoro e raggiungi l'arrivo;")
print("Movimento(Nord=W;Sud=S;Est=A;West=D)")
import os
level = 0
tutorial = 0
points = 0
q = 0
while True:
  if tutorial == 0:
    print("Tutorial")
    tutorial = 1

  a = []
  posmonster = []
  z = 0
  u = 0

  for i in range(10):
    for g in range(10):
      if i == 0 and g == 0:
        a.append(['P'])
      a.append([' '])
  a[73] = ['T']
  import random
  for x in range(level):
    randomizer = random.randint(0,81)
    while randomizer == 73 or randomizer  == 9 or randomizer == 0 or a[randomizer] == ['M']:
      randomizer = random.randint(0,81)
    a[randomizer]= ['M']
    posmonster.append(randomizer)

  b = 0
  while b <= 81:
    print(a[b],end = '')
    if b%9 == 0 :
      print()
    b += 1
  b = 0
  while True:

    c = input(">>>")
    if c == "W" and a[b-9]!=['M'] and b-9 >= 0:
    
      a[b] = [' ']
      b -= 9
      a[b] = ['P']
      q += 1
    elif c == "S" and a[b+9]!= ['M'] and b+9<=81:
      if z == 0:
        a[b] = ["BASE"]
        z +=1
      else:
        a[b] = [' ']
      z += 1
      b += 9
      a[b] = ['P']
      q +=1
    elif c == "A" and b-1 != 0 and b-1 != 9 and b-1 != 18 and b-1 != 27 and b-1 != 36 and b-1 != 45 and b-1 != 54 and b-1 != 63 and b-1 != 72 and a[b-1] != ['M']  :
      a[b] = [' ']
      b -= 1
      a[b] = ['P']
      q += 1
    elif c == "D" and b != 0 and b != 9 and b != 18 and b != 27 and b != 36 and b != 45 and b != 54 and b != 63 and b != 72 and b != 81 and a[b+1] != ['M']:
      a[b] = [' ']
      b += 1
      a[b] = ['P']
      q += 1
    for zlatan in range(level):
      randommover = random.randint(1,4)
      pos = posmonster[zlatan]
      if randommover == 1 and pos-9 !=['T'] and pos-9 >= 0 and pos != ['M'] and a[pos-9] != ["A"]:
        a[pos] = [' ']
        posmonster[zlatan] -= 9
        pos = posmonster[zlatan]
        a[pos] = ['M']
      elif randommover == 2 and a[pos+9]!= ['M'] and pos+9<=81 and a[pos+9] != ["T"] and a[pos+9] != ['A']:
        a[pos] = [' ']
        posmonster[zlatan] += 9
        pos = posmonster[zlatan]
        a[pos] = ['M']
      elif randommover == 3 and pos-1 != 0 and pos-1 != 9 and pos-1 != 18 and pos-1 != 27 and pos-1 != 36 and pos-1 != 45 and pos-1 != 54 and pos-1 != 63 and pos-1 != 72 and a[pos-1] != ['M'] and a[pos-1] != ['T'] and a[pos-1] != ['A']:
        a[pos] = [' ']
        posmonster[zlatan] -= 1
        pos = posmonster[zlatan]
        a[pos] = ['M']
      elif randommover == 4 and pos != 0 and pos != 9 and pos != 18 and pos != 27 and pos != 36 and pos != 45 and pos != 54 and pos != 63 and pos != 72 and pos != 81 and a[pos+1] != ['M'] and a[pos+1]!= ['T'] and a[pos+1] != ['A']:
        a[pos] = [' ']
        posmonster[zlatan] += 1
        pos = posmonster[zlatan]
        a[pos] = ['M']
      
      

      

    



    if a[73] == ['P']  and u == 0 :
      randomizer = random.randint(0,81)
      while randomizer == 73 or a[randomizer]== ['M'] or randomizer == 0:
        randomizer = random.randint(0,81)
      a[randomizer]= ['A']
      u += 1
    d = 0
    print()
    print()
    print()
    if tutorial != 1:
      os.system('clear')
    tutorial = 2

    while d <= 81:
      print(a[d],end = '')
      if d%9 == 0:
        print()
      d += 1
    print()
    print()
    print()

    if a[b] == ["M"]:
      break
    if a[73] == [' '] and a[randomizer] == ['P'] :
      print("Livello superato")
      level += 1
      points += level
      break
  if level == 78:
    break
  if a[b] == ['M']:
    break
  
    
print()
print()
print()
print()
if a[73] == [' '] and a[randomizer] == ['P']:
  print("COMPLIMENTI HAI SUPERATO TUTTI I LIVELLI!!!!!")
else:
  print("Che peccato ritenta")
print("Riassunto")
print("Livelli superati:",level)
print("Punti totalizzati:",points)
print("Mosse utilizzate:",q)
