import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption('Break it')

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bullet_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Gun:
    
    def __init__(self):
        pygame.draw.circle(screen, "white", player_pos, 5)

    def shoot(self):
        bullet_pos = player_pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet_pos.y -= 300 * dt
            if event.key == pygame.K_DOWN:
                bullet_pos.y += 300 * dt
            if event.key == pygame.K_LEFT:
                bullet_pos.x -= 300 * dt
            if event.key == pygame.K_RIGHT:
                bullet_pos.x += 300 * dt
    

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Game Logic
    pygame.draw.circle(screen, "red", player_pos, 20)
    
    bullet = Gun()

    bullet.shoot()

    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    

    # flip() updates screen 
    pygame.display.flip()

    # limit to 60 fps
    dt = clock.tick(60) / 1000

pygame.quit()
