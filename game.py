import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#Colour Palate 
C_BG = (5,8,18)
C_PLAYER = (0,220,255)

x,y = 320, 240 # Spawn Position
SIZE = 15
SPEED = 3

def draw_glow_rect(surf, color, rect, radius=4, glow_size=6, alpha=60):
    glow_surf = pygame.Surface((rect[2] + glow_size*2, rect[3] + glow_size*2), pygame.SRCALPHA)
    r, g, b = color
    pygame.draw.rect(glow_surf, (r, g, b, alpha),
                     (0, 0, rect[2] + glow_size*2, rect[3] + glow_size*2), border_radius=radius+glow_size)
    surf.blit(glow_surf, (rect[0] - glow_size, rect[1] - glow_size))
    pygame.draw.rect(surf, color, rect, border_radius=radius)

while True:
    clock.tick(60)

    ## Check for Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys   = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()

    ## Handle Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: y -= SPEED
    if keys[pygame.K_s]: y += SPEED
    if keys[pygame.K_a]: x -= SPEED
    if keys[pygame.K_d]: x += SPEED

    ## Draw 
    screen.fill(C_BG)
    pygame.draw.circle(screen, C_PLAYER, (x, y), SIZE)
    pygame.display.flip()

def angle_to(ox, oy, tx, ty):
    return math.atan2(ty - oy, tx - ox)

def dist(ax, ay, bx, by):
    return math.hypot(bx - ax, by - ay)
