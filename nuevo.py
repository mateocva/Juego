from libreria import *
from pygame.locals import *

#variables globales
global segundos #Duracion de la partida
global llaveEquipada #objeto interactivo
global trifuerzaEquipada #objeto interactivo
global pausado #auxiliar para pausar el juego
global segundosPausados # segundos guardados en la pausa
global introJuego #Activar la imagen de inicio
global pag
global lv
global vidaNivel1
global arcoItem
global arriba
global abajo
global izquierda
global derecha
global NumeroMuro

#iniciacion de variables globales

segundos=120 # tiempo = segundos - 1
llaveEquipada = False
trifuerzaEquipada = False
pausado=False
segundosPausados=0
introJuego=False
pag=1
lv = 1
vidaNivel1 = 0
arcoItem=False
arriba=False
abajo=False
izquierda=False
derecha=False
NumeroMuro=0

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


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

#IMAGENES
    fondo=pygame.image.load('noche.jpg').convert()

    
#importando Font(fuente de letra)
    historia=pygame.font.Font("Triforce.ttf",40)

#primer nivel
    nivel1=historia.render("Level 1",True,BLANCO)


#reloj
    reloj=pygame.time.Clock()

#actualizacion
    pygame.display.flip()



    #Cant = InicioJuego(pantalla, reloj)

    #fin = False
    while introJuego:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
	pygame.display.flip()
	reloj.tick(60)

	if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_SPACE:
                #pygame.mixer.music.stop()
                introJuego=False
                pantalla.fill(NEGRO)
                pantalla.blit(nivel1,(ANCHO/2-50,ALTO/2-50))
                pygame.display.flip()
                #pygame.time.delay(3000)

#Sprites
    
    todos=pygame.sprite.Group()
    packMuros=pygame.sprite.Group()
    objetivo=pygame.sprite.Group()
    objetivof=pygame.sprite.Group()
    mods=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    objetivo2=pygame.sprite.Group()
    objetivoff=pygame.sprite.Group()


    def get_line(start, end):


        """Bresenham's Line Algorithm
        Produces a list of tuples from start and end


        """
        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Swap start and end points if necessary and store swap state
        swapped = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            swapped = True

        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1

        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        # Iterate over bounding box generating points between start and end
        y = y1
        points = []
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            points.append(coord)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

        # Reverse the list if the coordinates were swapped
        if swapped:
            points.reverse()
        return points


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


    font=pygame.font.Font(None,36)

    #Enemigo
    
    e=Enemigox1(0,0)
    e1=Enemigox2(0,600)
    e2=Enemigox3(400,200)
    e3=Enemigoy1(200,100)
    e4=Enemigoy2(300,200)
    e5=Enemigoy3(500,150)
    enemigos.add(e,e2,e3,e4,e5)
    todos.add(e,e2,e3,e4,e5)

#----- SPRITES DEL NIVEL 2 ------


#MANTENER EL JUEGO EN UN CICLO

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                segundos=-1
                pygame.quit()
                sys.exit()

            #telclasPulsadas=pygame.key.get_pressed() #telca pulsada
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
            print"nivel 2"
            reloj.tick(30)

            Cant = InicioJuego(pantalla, reloj)

            lv = 2
            #fondo=pygame.image.load('noche.jpg').convert()
            historia=pygame.font.Font("Triforce.ttf",40)

            nivel2=historia.render("Level 2",True,BLANCO)

            while introJuego:
	            for event in pygame.event.get():
	                    if event.type == pygame.QUIT:
	                        pygame.quit()
	                        sys.exit()

	            pygame.display.flip()
	            reloj.tick(60)

	            if event.type == pygame.KEYDOWN:

	        	    if event.key==pygame.K_SPACE:
	            	    #pygame.mixer.music.stop()
	                	introJuego=False
	              	 	pantalla.fill(NEGRO)
	               		pantalla.blit(nivel2,(ANCHO/2-50,ALTO/2-50))
	               		pygame.display.flip()

            packMuros.empty()
            todos.empty()
            enemigos.empty()
            mods.empty()
            objetivo.empty()
            objetivof.empty()

            level2 = []
            level = open("laberinto2.txt")
            x = 0
            y = 0
            for l in level:
                    level2.append(l)
            for row in level2:
                    for col in row:


                            if col == "x":
                                    muroB = MuroBloques("ladrillo.png",x,y)
                                    packMuros.add(muroB)
                                    todos.add(muroB)

                            if col == "c":
                            		muro = MuroBloques("door.png",x,y)
                            		packMuros.add(muro)
                            		todos.add(muro)

                            if col == "C":
                            		muro1 = MuroBloques("door.png",x,y)
                            		packMuros.add(muro1)
                            		todos.add(muro1)


                            if col == "q":
                            		ob = Objetivo1("llave.png",x,y)
                            		objetivo.add(ob)
                            		todos.add(ob)

                            if col == "Q":
                            		ob1 = Objetivo2("llave.png",x,y)
                            		objetivo2.add(ob1)
                            		todos.add(ob1)

                            if col == "w":
                            		ob = Objetivoff("Ha.png",x,y)
                            		objetivoff.add(ob)
                            		todos.add(ob)

                            if col == "p":
                            		jp = Jugador("ss.png",x,y)
                            		jp.ls_muros = packMuros
                            		todos.add(jp)

                            x += 50
                    y += 50
                    x = 0

            jp.ls_mods=mods

            p=Enemigox11(0,0)
            enemigos.add(p)
            todos.add(p)
    
    	l_choque = pygame.sprite.spritecollide(jp,objetivo2,True)
    	for ecol in l_choque:
    	    	packMuros.remove(muro1)
    	    	todos.remove(muro1)
    	    	pygame.display.flip()
    	    	reloj.tick(0)

    	l_choque = pygame.sprite.spritecollide(jp,objetivoff,True)
    	for ecol in l_choque:
    			print"Fin del juego"
    			pantalla.fill(NEGRO)
    			texto = font.render("HAS GANADO", True, BLANCO)
    			pantalla.blit(texto, (200,100))
    			pygame.display.flip()
    			reloj.tick(1)
    			fin=True




	pantalla.blit(fondo,(0,0))
	todos.update()
	todos.draw(pantalla)
	pygame.display.flip()
	reloj.tick(30)









