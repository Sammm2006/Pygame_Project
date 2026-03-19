import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Colour Palate 
C_BG = (5,8,18)
C_PLAYER = (0,220,255)
C_BULLET = (0, 255, 162)
C_SHOOT = (255,255,255)

x,y = 320, 240 # Spawn Position
SIZE = 15
SPEED = 3
bullets = []
shoot_timer = 0
shoot_flash = 0
shake = 0

# Functions
def angle_to(ox, oy, tx, ty):
    return math.atan2(ty - oy, tx - ox)


# Main Loop
while True:
    clock.tick(60)

    ## Check for Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys   = pygame.key.get_pressed()
    mouse  = pygame.mouse.get_pressed() 
    mx, my = pygame.mouse.get_pos()

    ## Handle Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: y -= SPEED
    if keys[pygame.K_s]: y += SPEED
    if keys[pygame.K_a]: x -= SPEED
    if keys[pygame.K_d]: x += SPEED

    if shoot_timer > 0 :
        shoot_timer -= 1
    if shoot_flash > 0:
        shoot_flash -= 1
    if shake > 0 :
        shake -= 1

    if mouse[0] and shoot_timer == 0:
        angle = angle_to(x, y, mx, my)
        vx = math.cos(angle) * 8
        vy = math.sin(angle) * 8
        bullets.append([x,y,vx,vy])
        shoot_timer = 20
        shoot_flash = 10
        shake = 8

    for b in bullets[:]:
        b[0] += b[2]
        b[1] += b[3]
        if b[0] < -20 or b[0] > 820 or b[1] < -20 or b[1] > 620:
            bullets.remove(b)

    if shake > 0:
        ox = (shake // 2) * (1 if shake % 2 == 0 else -1)
        oy = (shake // 3) * (1 if shake % 3 == 0 else -1)
    else :
     ox, oy = 0,0

     player_color = C_SHOOT if shoot_flash > 0 else C_PLAYER

    ## Draw 
    screen.fill(C_BG)
    pygame.draw.circle(screen, player_color, (x + ox, y + oy), SIZE)
    for b in bullets:
        pygame.draw.circle(screen, C_BULLET, (int(b[0]), int(b[1])), 5)
    pygame.display.flip()
