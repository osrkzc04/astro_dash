import pygame
import sys
import random

from constant import *  # Importar constantes

#Score
score = 0
#Vida
live = 3
#Meteoritos
meteors = []

#Jugador
player_width = PLAYER_WIDTH
player_height = PLAYER_HEIGHT
player = pygame.Rect(WIDTH_SCREEN // 2 - player_width // 2, HEIGHT_SCREEN - player_height - 10, player_width, player_height)

meteor_width = METEOR_WIDTH
meteor_height = METEOR_HEIGHT


pygame.init()
#Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
#Titulo de la ventana
pygame.display.set_caption("AstroDash")
#Icono de la ventana
icon = pygame.image.load(ICO_IMAGE)
pygame.display.set_icon(icon)

# Fuentes
font = pygame.font.Font(FONT_FAMILY, 20)
font_score = pygame.font.Font(FONT_FAMILY, 35)

# Cargar el archivo de audio
pygame.mixer.music.load('./assets/audio/game-loop.mp3')

def menu():

    # Cargar imagen de fondo
    background_image = pygame.image.load(BACKGROUND_MENU_IMAGE) 
    background_image = pygame.transform.scale(background_image, (WIDTH_SCREEN, HEIGHT_SCREEN))
    screen.blit(background_image, (0, 0))

    #Nave Espacial
    sapceship = pygame.image.load(SPACESHIP_IMAGE)
    spaceship_rec = sapceship.get_rect()
    spaceship_rec.center = (WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2-120)
    screen.blit(sapceship, spaceship_rec)

    #AstroDash
    astro_dash = pygame.image.load(ASTRODASH_LOGO_IMAGE)
    astro_rect = astro_dash.get_rect() 
    astro_rect.center = (WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2) # Obtiene el rectángulo de la imagen
    screen.blit(astro_dash, astro_rect)  

    # Botón "Jugar"
    play_button = pygame.Rect(224,360,162,51)
    play_image = pygame.image.load(PLAY_BUTTON_IMAGE)
    screen.blit(play_image, (224, 360))
    # Botón "Salir"
    exit_button = pygame.Rect(414,360,162,51)
    exit_image = pygame.image.load(EXIT_BUTTON_IMAGE)
    screen.blit(exit_image, (414, 360))

    pygame.display.flip()

    # Verificar clics en los botones
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                return GAME  # Cambiar al estado de juego
            elif exit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    return MENU  # Mantener el estado actual si no se hace clic en ningún botón

def game():

    global score,live,lives


    if live == 0:
        return GAME_OVER

    # Cargar imagen de fondo
    background_image = pygame.image.load(BACKGROUND_GAME_IMAGE) 
    background_image = pygame.transform.scale(background_image, (WIDTH_SCREEN, HEIGHT_SCREEN))

    # Dibujar imagen de fondo
    screen.blit(background_image, (0, 0))
    
    #Iterar sobre todos los eventos que ocurran
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()

    #Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    #Mover jugador
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH_SCREEN:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT_SCREEN:
        player.y += 5

    #Generar meteoritos de forma aleatoria
    if len(meteors) < 7:
        meteor = pygame.Rect(random.randint(0, WIDTH_SCREEN - meteor_width), 0, meteor_width, meteor_height)
        meteors.append(meteor)

    #Mover meteoritos
    for meteor in meteors:
        meteor.y += 7
        if meteor.y > HEIGHT_SCREEN:
            meteors.remove(meteor)
            score += 1

    #Detectar colisiones
    for meteor in meteors:
        if player.colliderect(meteor):
            meteors.remove(meteor)
            live -= 1      

    #Dibujar jugador
    
    player_image = pygame.image.load(PLAYER_IMAGE)
    screen.blit(player_image, (player.x, player.y))
    
    #Iterar metoritos y dibujarlos
    imagen_metorito = pygame.image.load(METEOR_IMAGE)
    for meteor in meteors:
        screen.blit(imagen_metorito, (meteor.x, meteor.y))

    #Puntuación
    coin_image = pygame.image.load(COIN_IMAGE)
    screen.blit(coin_image, (50, 40))
    score_text = font_score.render(f"{score}", True, YELLOW)
    screen.blit(score_text, (90, 40))

    #Vidas
    heart_image = pygame.image.load(HEART_IMAGE)
    heart_outline_image = pygame.image.load(HEART_OUTLINE_IMAGE)
    if(live == 3):
        screen.blit(heart_image, (605, 40))
        screen.blit(heart_image, (660, 40))
        screen.blit(heart_image, (715, 40))
    elif(live == 2):
        screen.blit(heart_image, (605, 40))
        screen.blit(heart_image, (660, 40))
        screen.blit(heart_outline_image, (715, 40))
    else:
        screen.blit(heart_image, (605, 40))
        screen.blit(heart_outline_image, (660, 40))
        screen.blit(heart_outline_image, (715, 40))

    #Actualizar pantalla
    pygame.display.flip()
    #Definir velocidad de actualización
    clock.tick(60)

    return GAME


def game_over():
    global score,live
    # Cargar imagen de fondo
    background_image = pygame.image.load(BACKGROUND_GAME_OVER_IMAGE) 
    background_image = pygame.transform.scale(background_image, (WIDTH_SCREEN, HEIGHT_SCREEN))
    screen.blit(background_image, (0, 0))

    #Game Over Image
    game_over = pygame.image.load(GAME_OVER)
    game_over_rect = game_over.get_rect() 
    game_over_rect.center = (WIDTH_SCREEN // 2, HEIGHT_SCREEN // 2 -110) # Obtiene el rectángulo de la imagen
    screen.blit(game_over, game_over_rect)  

    #Coin
    coin_image = pygame.image.load(COIN_IMAGE)
    screen.blit(coin_image, (WIDTH_SCREEN // 2 - 50, 280))

    #Puntuación
    score_text = font_score.render(f"{score}", True, YELLOW)
    screen.blit(score_text, (WIDTH_SCREEN // 2, 280))

    # Botón "Jugar"
    play_button = pygame.Rect(224,360,162,51)
    play_image = pygame.image.load(PLAY_BUTTON_IMAGE)
    screen.blit(play_image, (224, 360))

    # Botón "Salir"
    exit_button = pygame.Rect(414,360,162,51)
    exit_image = pygame.image.load(EXIT_BUTTON_IMAGE)
    screen.blit(exit_image, (414, 360))

    pygame.display.flip()

    # Verificar clics en los botones
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                return GAME  # Cambiar al estado de juego
            elif exit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    return GAME_OVER  # Mantener el estado actual si no se hace clic en ningún botón


#Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()


def main():
    #Funcion Inicial
    current_state = MENU   
    # Estado inicial
    running = True
    pygame.mixer.music.play(-1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False      
        # Renderizar la pantalla correspondiente al estado actual
        if current_state == MENU:
            current_state=menu()
        elif current_state == GAME:
            current_state=game()
        elif current_state == GAME_OVER:
            game_over()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()