import pygame
import random

# Ekran boyutu
WIDTH = 800
HEIGHT = 600
 
# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (237, 237, 237)

pygame.init()
icon = pygame.image.load("icon.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gobrosko")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Yılan blokları için özellikler
BLOCK_SIZE = 20
snake_speed = 20

# Skor için özellikler
score = 0
font = pygame.font.Font('freesansbold.ttf', 25)
text_x = 10
text_y = 10

# Yemek için rastgele koordinatlar oluştur
food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

# Yılanın başlangıç koordinatları
x = WIDTH / 2
y = HEIGHT / 2

FPS = 15

# Yılanın başlangıç yönü ve blokları
direction = ''
snake_blocks = []
snake_length = 1

def display_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (text_x, text_y))

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def speed_up():
    global FPS, score
    if 0 <= score and 5 >= score: FPS = 17
    elif 4 <= score and 10 >= score: FPS = 20
    elif 9 <= score and 15 >= score: FPS = 22
    elif 14 <= score and 20 >= score: FPS = 25

def game_over():
    global FPS
    font = pygame.font.Font('freesansbold.ttf', 50)
    game_over_text = font.render("Game Over", True, RED)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (WIDTH / 2, HEIGHT / 2)
    screen.blit(game_over_text, game_over_rect)

    hight_score_r = open("hight_score.txt", "r", encoding="utf-8")
    fds = hight_score_r.read()
    if score >= int(fds):
        hight_score_r.close()
        hight_score_w = open("hight_score.txt", "w", encoding="utf-8")
        hight_score_w.write(str(score))
        hight_score_w.close()

    last_hight_score = open("hight_score.txt", "r", encoding="utf-8")
    hight_score = last_hight_score.read()
    last_hight_score.close()

    font = pygame.font.Font('freesansbold.ttf', 17)
    dsa = font.render("Hight Score: "+str(hight_score), True, BLACK)
    screen.blit(dsa, ((WIDTH-dsa.get_width())/2, HEIGHT/2+dsa.get_height()+10))

    pygame.display.update()
    pygame.time.wait(2500)
    pygame.quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Klavye tuşları dinleniyor
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = 'RIGHT'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                direction = 'UP'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                direction = 'DOWN'

    # Yılanın yönünü kontrol et
    if direction == 'LEFT':
        x -= snake_speed
    elif direction == 'RIGHT':
        x += snake_speed
    elif direction == 'UP':
        y -= snake_speed
    elif direction == 'DOWN':
        y += snake_speed

    # Yılan bloklarının koordinatlarını güncelle
    snake_head = [x, y]
    snake_blocks.append(snake_head)
    if len(snake_blocks) > snake_length:
        del snake_blocks[0]
    # Yılanın kendine çarpmasını kontrol et
    for block in snake_blocks[:-1]:
        if block == snake_head:
            game_over()

    # Yılanın ekranın dışına çıkmasını kontrol et
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        game_over()

    # Yılanın yemek yemesini kontrol et
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
        snake_length += 1
        score += 1

    # Ekranı temizle ve nesneleri yeniden çiz
    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
    draw_snake(snake_blocks)
    display_score()
    speed_up()


    # Ekranı güncelle
    pygame.display.update()

    # Oyun hızını belirle
    clock.tick(FPS)