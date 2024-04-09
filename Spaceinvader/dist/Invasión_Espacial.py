import pygame
import random
from math import sqrt, pow
from pygame import mixer
import io

def fuente_bytes(fuente):
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)

pygame.init()

pantalla = pygame.display.set_mode((800, 600))

mixer.music.load('90_Horns_SynthK_E.wav')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("extraterrestre.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fonfo.png")

img_jugador = pygame.image.load("nave-espacial.png")
jugador_x = 368
jugador_y = 520
jugador_mov_x = 0

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_mov_x = []
enemigo_mov_y = []
cantidad_de_enemigos = 8

for e in range(cantidad_de_enemigos):
    img_enemigo.append(pygame.image.load("astronave.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_mov_x.append(1.3)
    enemigo_mov_y.append(25)

img_bala = pygame.image.load("Tiros.png")
balas = []
bala_x = 0
bala_y = 525
bala_mov_x = 0
bala_mov_y = 5
bala_visible = False

puntaje = 0
fuente_como_bytes = fuente_bytes('freesansbold.ttf')
fuente = pygame.font.Font('freesansbold.ttf', 32)
txt_x = 10
txt_y = 10

fuente_final = pygame.font.Font(fuente_como_bytes, 50)


def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (150, 300))


def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x, y))


def hay_colision(x1, x2, y1, y2):
    distancia = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
        return False


se_ejecuta = True

while se_ejecuta:

    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_mov_x = -1.8
            if evento.key == pygame.K_RIGHT:
                jugador_mov_x = 1.8
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('pew.mp3')
                sonido_bala.play()
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_mov_x = 0

    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    # jugador

    jugador_x += jugador_mov_x

    if jugador_x <= -32:
        jugador_x = 800
    elif jugador_x >= 800:
        jugador_x = -32

    # enemigo

    for e in range(cantidad_de_enemigos):

        if enemigo_y[e] > 500:
            for k in range(cantidad_de_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_mov_x[e]

        if enemigo_x[e] <= 0:
            enemigo_mov_x[e] = 1.3
            enemigo_y[e] += enemigo_mov_y[e]
        elif enemigo_x[e] >= 736:
            enemigo_mov_x[e] = -1.3
            enemigo_y[e] += enemigo_mov_y[e]

        colision = hay_colision(enemigo_x[e], bala_x, enemigo_y[e], bala_y)

        if colision:
            sonido_colision = mixer.Sound('boom.mp3')
            sonido_colision.play()
            bala_y = 525
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("boom.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)
    jugador(jugador_x, jugador_y)

    mostrar_puntaje(txt_x, txt_y)

    if bala_y <= -64:
        bala_y = 525
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_mov_y

    pygame.display.update()
