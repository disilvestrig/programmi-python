import random
import math
class Entity:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self,direction):
        direction = input("Inserisci direzione (wasd) >>> ")
        direction = direction.lower()
        if direction == "w" :
            self.y -= 1
        if direction == "s" :
            self.y += 1
        if direction == "a" :
            self.x -= 1
        if direction == "d" :
            self.x += 1
class player(Entity):
    def __init__(self,x,y,hp,curhp):
        self.hp = hp
        self.curhp = hp
        Entity.__init__(self,x,y,graphic)
class Enemy(Entity):
    def __init__(self,x,y,damage):
        Entity.__init__(self,x,y,graphic)
        self.damage = damage
    def attack(self,target):
        target.curhp -= 1
        print("Hai perso una vita")
    def move(self,pp1):
        #pp1 deve essere una lista composta da x e y del player
        direct = ["w","a","s","d"]
        xm = self.x - pp1[0]
        ym = self.y - pp1[1]
        if fabs(xm) > fabs(ym) :
            if xm > 0:
                self.x -= 1
            elif xm < 0:
                self.x += 1
        elif fabs(xm) < fabs(ym):
            if ym > 0:
                self.y -= 1
            elif ym < 0:
                self.y += 1
        else:
            num = random.randint(0,1)
            if num == 0:
                if xm > 0:
                    self.x -= 1
                elif xm < 0:
                    self.x += 1
            else:
                if ym > 0:
                    self.y -= 1
                elif ym < 0:
                    self.y += 1
class Gold(Entity):
    def __init__(self,x,y):
        Entity.__init__(self,x,y)


            






