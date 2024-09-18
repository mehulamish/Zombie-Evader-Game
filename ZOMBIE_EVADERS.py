import pygame
from math import sqrt, pow
from random import randrange
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1200, 600))

# Background
background = pygame.image.load('background.png')

# Background music
mixer.music.load("backgroundsound.mp3")
mixer.music.play(-1)

# Title and logo
pygame.display.set_caption("ZOMBIE EVADERS")
logo = pygame.image.load('soldier.png')
pygame.display.set_icon(logo)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 30)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 215, 0))
    screen.blit(score, (x, y))

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)

def game_over_text():   
    over_text = over_font.render("GAME OVER", True, (255, 215, 0))
    screen.blit(over_text, (400, 250))

# Player
playerimg = pygame.image.load('player.png')
playerX = 0
playerY = 200
playerYchange = 0

def player(x, y):
    screen.blit(playerimg, (x, y))

# Enemy
enemyimg = []    
enemyX = []
enemyY = []
enemyXchange = []
numofenemies = 3

for i in range(numofenemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(950)
    enemyY.append(randrange(-40, 400))
    enemyXchange.append(-3)

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))
    
# Bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 160
bulletY = 200
bulletXchange = 15
bulletYchange = 0
bullet_state = "ready"  # Bullet is not visible in ready state

def fire_bullet(x, y):                
    global bullet_state
    bullet_state = "fire"  # Bullet is visible in fire state
    screen.blit(bulletimg, (x + 60, y + 130))
 
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt(pow(enemyX - bulletX, 2) + pow(enemyY - bulletY, 2))
    if distance < 30:
        return True
    else:
        return False
    
# Game loop
running = True
while running:
    
    # Screen color RGB
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False
          pygame.quit()
          
       # Keys for movement   
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
             playerYchange = -10
          if event.key == pygame.K_DOWN:
             playerYchange = 10 
          
          # Bullet key
          if event.key == pygame.K_SPACE:
              if bullet_state == "ready":
                  '''bullet_sound=mixer.load("gunshot.mp3")
                  bullet_sound.play()'''
                  bulletY = playerY
                  fire_bullet(bulletX, bulletY)    
              
       if event.type == pygame.KEYUP:    
          if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
              playerYchange = 0
          
    # Boundaries for player
    playerY += playerYchange
    if playerY <= -45:
        playerY = -45
    elif playerY >= 400:
        playerY = 400 
    
    # Enemy movement
    for i in range(numofenemies):
        
        # Game Over
        if enemyX[i] < 100:
            for j in range(numofenemies):
                enemyX[j] = 2000  # Move all enemies off-screen
            game_over_text()
            running = False
            break
        
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 100:
            enemyX[i] = 100
        
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletX = 160
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = 950
            enemyY[i] = randrange(-40, 400)
      
        enemy(enemyX[i], enemyY[i], i)
        
    # Bullet movement 
    if bulletX >= 1000:
        bulletX = 160
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletX += bulletXchange
    
    # Draw player and score
    player(playerX, playerY)
    show_score(textX, textY)
    
    pygame.display.update()
