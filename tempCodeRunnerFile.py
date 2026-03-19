    if mouse[0] and shoot_timer == 0:
        angle = angle_to(x, y, mx, my)
        vx = math.cos(angle) * 8
        vy = math.sin(angle) * 8
        bullets.append([x, y, vx, vy])
        shoot_timer = 10