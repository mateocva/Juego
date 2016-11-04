import pygame
import sys
import random

ANCHO = 650
ALTO = 650
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

cx = int(ANCHO/2)
cy = int(ALTO/2)

def ClearNivel(ls_Enemigos, ls_Todos, ls_objetivo1,ls_objetivof, packMuros):
	ls_Enemigos.empty()
	ls_jugador.empty()
	ls_Todos.empty()
	ls_objetivo1.empty()
	ls_objetivof.empty()
	packMuros.empty()

def InicioJuego(Pantalla, reloj):
	Cargando = 0
	time = 1
	font = pygame.font.Font(None, 80)
	while(Cargando < 100):
		Pantalla.fill(NEGRO)
		texto = font.render("Cargando " + str(Cargando) + "%", True, BLANCO)
		Cargando += time
		time += random.randrange(2)
		Pantalla.blit(texto, (ANCHO/2-150 , ALTO/2))
		reloj.tick(10)
		pygame.display.flip()

#Funcion para mostrar el fin del juego
def FinJuego(Pantalla, jugador, reloj):
	Pantalla.fill(NEGRO)
	font = pygame.font.Font(None, 100)
	font2 = pygame.font.Font(None, 50)
	font.set_bold(True)
	if jugador.vida == 0:
		texto = font.render("Game Over.", True, BLANCO)
	else:
		texto = font.render("You Win.", True, BLANCO)
	pygame.display.flip()
	reloj.tick(1)

#Funcion para limpiar los grupos al pasar de nivel
def InitNivel(jugador, ls_enemigos, ls_todos, pantalla, reloj, fondo):
	font = pygame.font.Font(None, 100)
	InicioJuego(pantalla, reloj)
	if jugador.nivel == 1:
		texto = font.render("Nivel 1", True, BLANCO)
		Cant = random.randrange(5,15)
		laberinto()
	else:
		texto = font.render("Nivel 2", True, BLANCO)
		Cant1 = random.randrange(15,30)
		#ls_enemigos,ls_todos=Crear_enemigos(Cant1,ls_enemigos,ls_todos,6,1)
		#ls_enemigos,ls_todos=Crear_enemigos(Cant1-14,ls_enemigos,ls_todos,5,1)
		#Cant = Cant1 + (Cant1-14)
	pantalla.blit(fondo, (0,0))
	pantalla.blit(texto, (100, ALTO/2))
	pygame.display.flip()
	reloj.tick(1)
	return Cant

#Muros del juego
class MuroBloques(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#Jugador
class jugador(pygame.sprite.Sprite):
	ls_muros=None
	ls_mod=None
	def __init__(self,archivo,x,y):
		self.nivel=1
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

def laberinto():
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

def main():
	pygame.init()

	pygame.font.init()
	font = pygame.font.Font(None, 100)
	font2 = pygame.font.Font(None, 40)
	font3 = pygame.font.Font(None, 20)

	pantalla = pygame.display.set_mode((ANCHO,ALTO))
	#pygame.display.set_caption("space")

	fondo = pygame.image.load("noche.jpg").convert()
	#sonidoExplosion = pygame.mixer.Sound("Explosion/eSonido.mp3")

	#RELOJ
  	reloj=pygame.time.Clock()

	#LISTAS
	ls_Todos=pygame.sprite.Group()
	packMuros=pygame.sprite.Group()
	ls_objetivo=pygame.sprite.Group()
	ls_objetivof=pygame.sprite.Group()
	ls_Enemigos=pygame.sprite.Group()

	#tecla = pygame.key.get_pressed()
	Cant = InitNivel(jugador, ls_Enemigos, ls_Todos, pantalla, reloj, fondo)
	print "x",jugador.rect.x,"y",Jugador.rect.y," main"
	while not terminar:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				terminar=True
			if(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
				if jugador.nivel==1:
					laberinto=packMuros()


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
            pantalla.fill(NEGRO)
            #ganar=pygame.image.load('1.gif').convert()
            #texto = font.render("HAS GANADO", True, NEGRO)
            #pantalla.blit(texto, (200,100))
            #pantalla.blit(ganar,(0,0))
            pygame.display.flip()
            reloj.tick(0)
            #fin=True
	#pantalla.blit(fondo,(0,0))
	#todos.update()
	#todos.draw(pantalla)
	#pygame.display.flip()
	#reloj.tick(60)

	ls_Enemigos.update()
	ls_todos.update()
	ls_jugadores.draw(pantalla)
	ls_Explosiones.update()
	ls_Explosiones.draw(pantalla)
	ls_jugadores.draw(pantalla)
	ls_todos.draw(pantalla)
	pygame.display.flip()
	reloj.tick(90)
	ls_enemigos,ls_todos = Crear_enemigos(num_enemigos,ls_enemigos,ls_todos,band,a)
	Cant=len(ls_enemigos)
	a=0
	if Cant <= 0 :

		if band<=2:

			band+=1
			a=1
			num_enemigos=6

		else:
			print "entra nivel dos"
			#ClearNivel(ls_enemigos, ls_todos, ls_balas, ls_Explosiones, ls_Escudo)
			Jugador.nivel=2
			if Jugador.nivel == 2:
				Cant = InitNivel(Jugador, ls_enemigos, ls_todos, PANTALLA, reloj, fondo,band)
	FinJuego(pantalla, Jugador, reloj)

#codeacademy
if __name__ == '__main__':
	main()
