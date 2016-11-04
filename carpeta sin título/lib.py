import pygame

ANCHO=650
ALTO=650
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)

class MuroBloques(pygame.sprite.Sprite):
    def __init__(self,archivo, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Jugador(pygame.sprite.Sprite):

    muros=None
    def __init__(self,archivo,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.var_x=0
        self.var_y=0




    def update(self):
        self.rect.x += self.var_x
        lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)
        for bloque in lista_golpes:
            if self.var_x > 0:
                self.rect.right = bloque.rect.left
            else:
                self.rect.left = bloque.rect.right

        self.rect.y += self.var_y
        lista_golpes = pygame.sprite.spritecollide(self, self.muros, False)
        for bloque in lista_golpes:
            if self.var_y > 0:
                self.rect.bottom = bloque.rect.top
            else:
                self.rect.top = bloque.rect.bottom

    def direccion(self,pos):
        if pos == 1:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_y = -3
            self.var_x = 0
        if pos == 2:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_y = 0
            self.var_x = -3
        if pos == 3:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 3
        if pos == 4:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 3
            self.var_y = 0

        if pos == 55:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 66:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 77:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0

        if pos == 88:
            self.image = pygame.image.load("personaje.png").convert_alpha()
            self.var_x = 0
            self.var_y = 0
