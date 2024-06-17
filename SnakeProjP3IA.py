import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir los colores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Tamaño de los bloques y la velocidad del juego
block_size = 20
speed = 20

# Crear la ventana del juego
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

# Función para mostrar el mensaje en la pantalla
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Dibujar la serpiente en la pantalla
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block_size, block_size])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Inicializar la posición de la serpiente
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Posición aleatoria de la comida
    foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0

    # Bucle principal del juego
    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("Perdiste! Presiona Q-Quit o C-Jugar de nuevo", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Mover la serpiente automáticamente
        if len(snake_List) > 0:
            if x1 < foodx:
                x1_change = speed
                y1_change = 0
            elif x1 > foodx:
                x1_change = -speed
                y1_change = 0
            elif y1 < foody:
                y1_change = speed
                x1_change = 0
            else:
                y1_change = -speed
                x1_change = 0

        # Actualizar la posición de la serpiente
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # Dibujar la comida
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificar si la serpiente se ha chocado
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)

        pygame.display.update()

        # Verificar si la serpiente ha comido la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        # Verificar si la serpiente ha chocado con los bordes
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        clock.tick(10)

    pygame.quit()
    quit()

# Iniciar el juego
gameLoop()