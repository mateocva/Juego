import pygame
import random
import sys
import ConfigParser

ANCHO=650
ALTO=650
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

#Pantalla de carga del juego
def InicioJuego(Pantalla, reloj):
    Cargando = 0
    time = 1
    font = pygame.font.Font(None, 80)
    while(Cargando < 100):
        Pantalla.fill(NEGRO)
        texto = font.render("Cargando " + str(Cargando) + "%", True, BLANCO)
        Cargando += time
        time += random.randrange(2)
        Pantalla.blit(texto, (ANCHO/2-200 , ALTO/2))
        reloj.tick(5)
        pygame.display.flip()

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

#Enemigos nivel2 movimiento en eje
class Enemigoy1(pygame.sprite.Sprite):
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
class Objetivof(pygame.sprite.Sprite):
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

if __name__ == '__main__':
    pygame.init()

    pygame.font.init()
    font = pygame.font.Font(None, 100)

    mods=pygame.sprite.Group()

    #listas
    reloj=pygame.time.Clock()
    todos=pygame.sprite.Group()
    packMuros=pygame.sprite.Group()
    objetivo=pygame.sprite.Group()
    objetivof=pygame.sprite.Group()

    font=pygame.font.Font(None,36)

    #Enemigo
    enemigos=pygame.sprite.Group()
    e=Enemigox1(0,0)
    #e1=Enemigox2(0,600)
    e2=Enemigox3(400,200)
    e3=Enemigoy1(200,100)
    e4=Enemigoy2(300,200)
    e5=Enemigoy3(500,150)
    enemigos.add(e,e2,e3,e4,e5)
    todos.add(e,e2,e3,e4,e5)

    level1 = []
    level = open("laberinto.txt")
    x = 0
    y = 0
    for l in level:
            level1.append(l)
    for row in level1:
            for col in row:
                    if col == "x":
                            muroB = MuroBloques("ladrillo.png",x,y)
                            packMuros.add(muroB)
                            todos.add(muroB)

                    if col == "c":
                            muro = MuroBloques("door.png",x,y)
                            packMuros.add(muro)
                            todos.add(muro)

                    if col == "A":
                            ob = Objetivo1("llave.png",x,y)
                            objetivo.add(ob)
                            todos.add(ob)

                    if col == "Z":
                            obf = Objetivof("Ha.png",x,y)
                            objetivof.add(obf)
                            todos.add(obf)

                    if col == "P":
                            jp = Jugador("ss.png",x,y)
                            jp.ls_muros = packMuros
                            todos.add(jp)
                    x += 50
            y += 50
            x = 0

    jp.ls_mods=mods

    pantalla.blit(fondo,(0,0))
    todos.update()
    todos.draw(pantalla)
    pygame.display.flip()
    reloj.tick(60)
