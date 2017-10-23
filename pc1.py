import sys, pygame
pygame.init()

size = width, height = 920, 840
speed = [0, 0]
black = 100, 100, 100

screen = pygame.display.set_mode(size)
angle = 0;
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
pygame.transform.rotate(ball ,90)
#ballrect = ballrect.move(500, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # check if key is pressed
        # if you use event.key here it will give you error at runtime
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                angle=180
                speed = [-1, 0];
            if event.key == pygame.K_RIGHT:
                angle=0
                speed = [1, 0];
            if event.key == pygame.K_UP:
                angle=90
                speed = [0, -1];
            if event.key == pygame.K_DOWN:
                angle=270
                speed = [0, 1];

    ball = pygame.transform.rotate(ball ,angle-prev)


    screen.fill(black)
    ballrect = ballrect.move(speed)
    screen.blit(ball, ballrect)
    pygame.display.flip()
