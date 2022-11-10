import pyxel, random, time

def vaisseau_deplacement(x, y):
    if pyxel.btn(pyxel.KEY_RIGHT):
        if x < 240 :
            x = x + 4  
    if pyxel.btn(pyxel.KEY_LEFT):
        if x > 0:
            x = x - 4  
    if pyxel.btn(pyxel.KEY_DOWN):
        if y < 234 :
            y = y + 4  
    if pyxel.btn(pyxel.KEY_UP):
        if y > 0 :
            y = y - 4
    if pyxel.btn(pyxel.KEY_END): #a voir
        if y > 0 :
            y = y - 20
            #time.sleep(0.5)
            #y = y + 20
    return x, y


def tirs_creation(x, y, tirs_liste):
    if pyxel.btnr(pyxel.KEY_SPACE):
        tirs_liste.append([x+8, y - 4]) 
    return tirs_liste


def tirs_deplacement(tirs_liste):
    for tir in tirs_liste:
        tir[1] -= 3
        if tir[1] < -16:
            tirs_liste.remove(tir)  
    return tirs_liste


def ennemis_creation(ennemis_liste):
    if pyxel.frame_count % 30 == 0:
        ennemis_liste.append([random.randint(0, 240), 0])
    return ennemis_liste


def ennemis_deplacement(ennemis_liste):
    for ennemi in ennemis_liste:
        ennemi[1] += 1
        if ennemi[1] > 234:
            ennemis_liste.remove(ennemi)
    return ennemis_liste


def vaisseau_suppression(vies):
    for ennemi in ennemis_liste:
        if ennemi[0] <= vaisseau_x + 16 and ennemi[1] <= vaisseau_y + 16 and ennemi[0] + 16 >= vaisseau_x \
                and ennemi[1] + 16 >= vaisseau_y:
            
            ennemis_liste.remove(ennemi)  
            vies -= 1
    return vies


def ennemis_suppression(points):
    for ennemi in ennemis_liste:
        for tir in tirs_liste:
            if ennemi[0] <= tir[0] + 1 and ennemi[0] + 16 >= tir[0] and ennemi[1] + 16 >= tir[1]:
                points += 10
                ennemis_liste.remove(ennemi) 
                tirs_liste.remove(tir)  
    return points


def update():
    global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, points
    vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)
    tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)
    tirs_liste = tirs_deplacement(tirs_liste)
    ennemis_liste = ennemis_creation(ennemis_liste)
    ennemis_liste = ennemis_deplacement(ennemis_liste)
    points = ennemis_suppression(points)
    vies = vaisseau_suppression(vies)



def draw():
    pyxel.cls(0)
    pyxel.text(2, 2, 'Vies : '+str(vies) + '   Points : '+str(points), 7)
    if vies > 0:
        #pyxel.rect(vaisseau_x, vaisseau_y, 16, 16, 4) #vaissaux carré
        pyxel.blt(vaisseau_x, vaisseau_y, 0, 0, 0, 16, 16)
        pyxel.rect(0, 250, 256, 1, 6)
        
        for tir in tirs_liste:
            pyxel.rect(tir[0], tir[1], 1, 6, 10) #pour tir vertical
            #pyxel.rect(tir[0], tir[1], 6, 1, 10)
        for ennemi in ennemis_liste:
            #pyxel.rect(ennemi[0], ennemi[1], 16, 16, 8) #ennemi carré
            pyxel.blt(ennemi[0], ennemi[1], 1, 0, 0, 16, 16)
        
    else:
        pyxel.text(120, 115, 'GAME OVER', 7)



pyxel.init(256, 256, title="Jeu pyxel")

vaisseau_x = 120
vaisseau_y = 234

vies = 10
points = 0
tirs_liste = []

ennemis_liste = []
pyxel.load("my_resource.pyxres")
pyxel.run(update, draw)

