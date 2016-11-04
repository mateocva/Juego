import pygame
import os
import pygame
import sys

ANCHO=650
ALTO=650
blanco = (255,255,255)
negro = (0,0,0)
amarillo = (255,255,0)
dorado = (231,174,24)
azulclaro = (0,255,255)
violeta = (204,0,102)
rojo = (255,0,0)
rojooscuro = (190,17,17)
verde = (0,255,0)
azul = (0,0,255)
morado = (153,51,255)
naranja = (255,128,0)
gris = (128,128,128)

#INICIALIZACION DE VARIABLES
pygame.init()

#DIMENSIONES DE LA PANTALLA
pantalla = pygame.display.set_mode((ANCHO,ALTO),pygame.FULLSCREEN)

#DIMENSIONES DEL MENU
MenuX = 410
MenuY = 478
DimensionMenu = [MenuX,MenuY]

#IMAGENES Y MUSICA DEL MENU
Seleccion = pygame.image.load('Seleccion.png').convert_alpha()

#VARIABLES DE JUEGO
salir = False
scroll = False
reloj = pygame.time.Clock()  
CambioNivel2 = False

# ESTRUCTURA DEL TEXTO DEL MENU 
def TextoMenu(texto, posx, posy, negro):
    fuente = pygame.font.Font("bloodcrow.ttf", 35)
    salida = pygame.font.Font.render(fuente, texto, 0, negro)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def IniciarJuego():
#fondo
    fondo=pygame.image.load('noche.jpg').convert()

    pygame.event.clear
    os.system('clear')
    salir = False
    FinGameOver = False
    FinMeta = False

    global event ,scroll, CambioNivel2
    while salir != True: 
       reloj.tick(60) 
       tecla = pygame.key.get_pressed()
       for event in pygame.event.get():   
           if event.type == pygame.QUIT:
              salir = True
           if tecla[pygame.K_s]:
              sys.exit()
           if tecla[pygame.K_SPACE]:
                print "Disparar"
                scroll = False
#-------------------------------------
def Menu(opcion):
    Seleccion = pygame.image.load('Seleccion.png').convert_alpha() 
    fuente = pygame.font.Font('Zombified.ttf', 80)
    #Titulo = fuente.render("PODER CIENTIFICO", 1, (dorado))
    if opcion == 1:
       IniciarJuego,opcion1 = TextoMenu("INICIAR  JUEGO",900,540,(azul))
       Salir,opcion5 = TextoMenu("SALIR",900,740,(rojo))
       pantalla.blit(Seleccion,(MenuX+260,MenuY+35))
    if opcion == 2:
       IniciarJuego,opcion1 = TextoMenu("INICIAR  JUEGO",900,540,(rojo))
       Salir,opcion5 = TextoMenu("SALIR", 900, 740,(azul))
       pantalla.blit(Seleccion,(MenuX+360,MenuY+75))
    pantalla.blit(IniciarJuego,opcion1)
    pantalla.blit(Salir,opcion5)

#---------------------------------------
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
               ReiniciarTiempo = True
	    if opcion == 2:
	       sys.exit()
    Menu(opcion)
    pygame.display.flip()
pygame.quit()






