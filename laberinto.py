import pygame
import ConfigParser
import pygame
import random
import os

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

def TextoMenu(texto, posx, posy, negro):
    fuente = pygame.font.Font("bloodcrow.ttf", 35)
    salida = pygame.font.Font.render(fuente, texto, 0, negro)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect


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
#Obetivos del Jugador
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



pygame.event.clear
os.system('clear')
salir = False
FinMeta=False
CambioNivel2 = False

#DIMENSIONES DEL MENU
MenuX = 410
MenuY = 478
DimensionMenu = [MenuX,MenuY]


if __name__ == '__main__':
    pygame.init()

    pygame.font.init()
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 40)
    font3 = pygame.font.Font(None, 20)

    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    #fondo
    fondo=pygame.image.load('noche.jpg').convert()
    Seleccion = pygame.image.load('Seleccion.png').convert_alpha()

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
    e1=Enemigox2(0,600)
    e2=Enemigox3(400,200)
    e3=Enemigoy1(200,100)
    e4=Enemigoy2(300,200)
    e5=Enemigoy3(500,150)
    enemigos.add(e,e1,e2,e3,e4,e5)
    todos.add(e,e1,e2,e3,e4,e5)

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

    mods=pygame.sprite.Group()
    jp.ls_mods=mods

    Cant = InicioJuego(pantalla, reloj)    

	
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                #segundos=-1
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jp.var_x=5
                    jp.var_y=0
                if event.key == pygame.K_LEFT:
                    jp.var_x=-5
                    jp.var_y=0
                if event.key == pygame.K_UP:
                    jp.var_y=-5
                    jp.var_x=0
                if event.key == pygame.K_DOWN:
                    jp.var_y=5
                    jp.var_x=0
                if event.key == pygame.K_SPACE:
                    jp.var_x=0
                    jp.var_y=0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    jp.var_x=0
                if event.key == pygame.K_LEFT:
                    jp.var_x=0
                if event.key == pygame.K_UP:
                    jp.var_y=0
                if event.key == pygame.K_UP:
                    jp.var_y=0

        if jp.rect.x>ANCHO-jp.rect.width:
            jp.rect.x=ANCHO-jp.rect.width
            jp.var_x=0
        if jp.rect.x<0:
            jp.rect.x=0
            jp.var_x=0
        if jp.rect.y>ALTO-jp.rect.height:
            jp.rect.y=ALTO-jp.rect.height
            jp.var_y=0
        if jp.rect.y<0:
            jp.rect.y=0
            jp.var_y=0

        l_choque = pygame.sprite.spritecollide(jp,enemigos,True)
        for ecol in l_choque:
            pantalla.fill(BLANCO)
            derrota=pygame.image.load('over.png').convert()
            pantalla.blit(derrota,(0,0))
            pygame.display.flip()
            reloj.tick(1)
            fin=True

        l_choque = pygame.sprite.spritecollide(jp,objetivo,True)
        for ecol in l_choque:
            packMuros.remove(muro)
            todos.remove(muro)
            pygame.display.flip()
            reloj.tick(0)

        l_choque = pygame.sprite.spritecollide(jp,objetivof,True)
        for ecol in l_choque:
            #pantalla.fill(NEGRO)
            #ganar=pygame.image.load('1.gif').convert()
            #texto = font.render("HAS GANADO", True, NEGRO)
            #pantalla.blit(texto, (200,100))
            #pantalla.blit(ganar,(0,0))
            print"nivel 2"
            FinMeta=True
            pygame.display.flip()
            reloj.tick(0)
            #fin=True
        if CambioNivel2 == True:
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


            



	pantalla.blit(fondo,(0,0))
	todos.update()
	todos.draw(pantalla)
	pygame.display.flip()
	reloj.tick(60)


def Menu(opcion):
	pantalla.fill(BLANCO)
	#Titulo = fuente.render("PODER CIENTIFICO", 1, (dorado))
	if opcion == 1:
		IniciarJuego,opcion1 = TextoMenu("INICIAR  JUEGO",900,540,(AZUL))
		Salir,opcion5 = TextoMenu("SALIR",900,740,(ROJO))
		pantalla.blit(Seleccion,(MenuX+260,MenuY+35))
	if opcion == 2:
		IniciarJuego,opcion1 = TextoMenu("INICIAR  JUEGO",900,540,(rojo))
		Salir,opcion2 = TextoMenu("SALIR", 900, 740,(AZUL))
		pantalla.blit(Seleccion,(MenuX+360,MenuY+75))
	pantalla.blit(IniciarJuego,opcion1)
	pantalla.blit(Salir,opcion5)

opcion = 1
while salir != True:
    reloj.tick(60)
    tecla = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True
        if tecla[pygame.K_s]:
	    sys.exit()
        if tecla[pygame.K_UP] and opcion > 1 and MenuY > DimensionMenu[1]:
            sounds.OpcionMenu.play()
            opcion -= 1
            MenuY = MenuY-40
            Seleccion
        if tecla[pygame.K_DOWN] and opcion < 5 and MenuY > DimensionMenu[0]:
            sounds.OpcionMenu.play()
            opcion += 1
            MenuY = MenuY+40
            Seleccion
	if tecla[K_RETURN]:
	    if opcion == 1:
	       print "ACCEDER AL JUEGO"
               sounds.EnterMenu.play()
               IniciarJuego()
	    if opcion == 2:
	       sys.exit()
    Menu(opcion)
    pygame.display.flip()
pygame.quit()
