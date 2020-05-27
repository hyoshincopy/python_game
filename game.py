import pygame

white = (255, 255, 255)
pad_width = 1024
pad_height = 512


def ariplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))


def runGame():
    global gamepad, clock, aircraft

    x = pad_width*0.05
    y = pad_height*0.8
    y_change = 0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change += 5
                elif event.key == pygame.K_DOWN:
                    y_change -= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change

        gamepad.fill(white)
        ariplane(x, y)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()


def initGame():
    global gamepad, clock, aircraft

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')
    aircraft = pygame.display.set_caption('./fly.png')
    clock = pygame.time.Clock()
    runGame()


initGame()
