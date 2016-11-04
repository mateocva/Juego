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
