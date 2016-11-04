import pygame
import time
import threading
import sys
import random

ANCHO=650
ALTO=650
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

# Punto Medio para la posicion de la bala del enemigo 2
def PmBalaEnemigo(bala):
    xy = []
    if bala.direccion == 1:
        m = 4
    else:
        m = -4
    y = bala.rect.y
    x = bala.rect.x
    b = y - m* x
    if bala.direccion != 0:
        while y < 8000:
            if bala.direccion == 1:
                d1 = (x + 1, y)
                d2 = (x + 1, y + 1)
                pm = y + 1/2
                if y > pm:
                    xy.append(d1)
                else:
                    xy.append(d2)
                x += 1
                y = int(round(m*x + b))
            else:
                d1 = (x - 1, y)
                d2 = (x - 1, y + 1)
                pm = y + 1/2
                if y > pm:
                    xy.append(d1)
                else:
                    xy.append(d2)
                x -= 1
                y = int(round(m*x + b))
    return xy

    #Funcion usando el punto medio de la circunferencia para darle la posicion al enemigo 2
def PmCircunfPosEnemigo(enemigo):
    centro = (enemigo.rect.x, enemigo.rect.y)
    puntos = []
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    x = 0
    y = 50
    d = 5/4 - y
    xy = Traslacion(centro, (x ,y))
    p1.append(xy)
    xy = Traslacion(centro, (x, -y))
    p2.append(xy)
    xy = Traslacion(centro, (-x, y))
    p3.append(xy)
    xy = Traslacion(centro, (-x, -y))
    p4.append(xy)
    xy = Traslacion(centro, (y, x))
    p5.append(xy)
    xy = Traslacion(centro, (y, -x))
    p6.append(xy)
    xy = Traslacion(centro, (-y, x))
    p7.append(xy)
    xy = Traslacion(centro, (-y, -x))
    p8.append(xy)
    while x < y:    
        x += 1
        if d < 0:
            d = d + 2*x + 1
        else:
            d = d + 2*(x - y) + 1
            y -= 1      
        xy = Traslacion(centro, (x ,y))
        p1.append(xy)
        xy = Traslacion(centro, (x, -y))
        p2.append(xy)
        xy = Traslacion(centro, (-x, y))
        p3.append(xy)
        xy = Traslacion(centro, (-x, -y))
        p4.append(xy)
        xy = Traslacion(centro, (y, x))
        p5.append(xy)
        xy = Traslacion(centro, (y, -x))
        p6.append(xy)
        xy = Traslacion(centro, (-y, x))
        p7.append(xy)
        xy = Traslacion(centro, (-y, -x))
        p8.append(xy)
    p5.reverse()
    p2.reverse()
    p8.reverse()
    p3.reverse()
    puntos = p1 + p5 + p6 + p2 + p4 + p8 + p7 + p3
    return puntos


#-------------CLASES
#Muros del juego
class MuroBloques(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Jugador
class Jugador(pygame.sprite.Sprite):

    ls_muros=None
    ls_mod=None
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=0
        self.var_y=0

    def update(self):

               self.rect.x+=self.var_x
               ls_golpes=pygame.sprite.spritecollide(self,self.ls_muros,False)
               for m in ls_golpes:
                   if self.var_x > 0:
                       self.rect.right=m.rect.left
                   else:
                       self.rect.left=m.rect.right

               self.rect.y+=self.var_y
               ls_golpes=pygame.sprite.spritecollide(self,self.ls_muros,False)
               for m in ls_golpes:
                   if self.var_y > 0:
                       self.rect.bottom=m.rect.top
                   else:
                       self.rect.top=m.rect.bottom

               ls_captura=pygame.sprite.spritecollide(self,self.ls_mods,True)
               for md in ls_captura:
                   self.vel=3
#Enemigos movimiento eje X
class Enemigox1(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = 30
        self.alto = 30
        self.image=pygame.Surface([self.ancho,self.alto])
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=3

    def update(self):
        self.rect.x+=self.var_x
        if self.rect.x>(ANCHO-350):
            self.var_x=-3
        elif self.rect.x <= 0 and self.rect.x < (ANCHO-350):
            self.var_x=3
class Enemigox2(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = 30
        self.alto = 30
        self.image=pygame.Surface([self.ancho,self.alto])
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=3

    def update(self):
        self.rect.x+=self.var_x
        if self.rect.x>(ANCHO-50):
            self.var_x=-3
        elif self.rect.x <= 0 and self.rect.x < (ANCHO):
            self.var_x=3
class Enemigox3(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.ancho = 30
        self.alto = 30
        self.image=pygame.Surface([self.ancho,self.alto])
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=3

    def update(self):
        self.rect.x+=self.var_x
        if self.rect.x>(ANCHO-150):
            self.var_x=-3
        elif self.rect.x <= 300 and self.rect.x < (ANCHO-250):
            self.var_x=3
#Enemigos movimiento eje Y
class Enemigoy1(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=3

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>(ALTO-150):
            self.var_y=-3
        elif self.rect.y <= 100 and self.rect.y < (ALTO-500):
            self.var_y=3
class Enemigoy2(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=3

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>(ALTO-150):
            self.var_y=-3
        elif self.rect.y <= 200 and self.rect.y < (ALTO-400):
            self.var_y=3
class Enemigoy3(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=3

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>(ALTO-150):
            self.var_y=-3
        elif self.rect.y <= 150 and self.rect.y < (ALTO-450):
            self.var_y=3

#ENEMIGOS NIVEL 2
class Enemigox11(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('ast.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_y=3

    def update(self):
        self.rect.y+=self.var_y
        if self.rect.y>(ALTO-150):
            self.var_y=-3
        elif self.rect.y <= 150 and self.rect.y < (ALTO-450):
            self.var_y=3

#Objetivos del Jugador
class Objetivo1(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        #self.var_x=0
        #self.var_y=0

    def update(self):
        pass

class Objetivo2(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        #self.var_x=0
        #self.var_y=0

    def update(self):
        pass

class Objetivof(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Objetivoff(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

#Bala del Enemigo 2
class BalaEnemigo2(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.direccion = random.randrange(0,3)
        self.balas = ["Enemigos/EB2.png", "Enemigos/EB2I.png", "Enemigos/EB2D.png"]
        self.image = pygame.image.load(self.balas[self.direccion]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.posicion = PmBalaEnemigo(self)
        self.contador = 1
    
    def update(self):
        if self.direccion == 0:
            self.rect.y += 3
        else:
            self.rect.x = self.posicion[self.contador][0]
            self.rect.y = self.posicion[self.contador][1]
            self.contador += 1

def Traslacion((x,y), (tx,ty)):
    x=x+tx
    y=y-ty
    return (x,y)

    #Enemigo 2
class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Enemigos/E2.png")
        self.rect = self.image.get_rect()
        self.direccion = 0
        self.rect.x = x
        self.rect.y = y
        self.recarga = random.randrange(50, 100)
        self.posicion = PmCircunfPosEnemigo(self)
        self.contador = 0
        self.disparar = False
        self.distintivo = 2

    def update(self):
        if self.contador <= len(self.posicion)-1:
            self.rect.x = self.posicion[self.contador][0]
            self.rect.y = self.posicion[self.contador][1]
            self.contador += 3

        else:
            self.contador = 0
        
        if self.recarga == 0:
            self.disparar = True
            self.recarga = random.randrange(100)
        else:
            self.recarga -= 1
            self.disparar = False
