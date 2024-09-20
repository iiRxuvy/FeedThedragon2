import pygame
# Set display surface
pygame.init()

# Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game value:  CONSTANT_NAME, value
''' 5 CONSTANTS
PLAYER_STARTING_LIVES, 5
PLAYER_VELOCITY, 10
COIN_STARTING_VELOCITY, 10
COIN_ACCELERATION, 0.5
BUFFER_DISTANCE, 100
'''
PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100


#Set Game Variables:  variable_name
''' 3 variables
score, 0
player_lives, PLAYER_STARTING_LIVES
coin_velocity, COIN_STARTING_VELOCITY
'''
score = 0
player_lives = 5
PLAYER_STARTING_LIVES = 5
coin_velocity = 5
COIN_STARTING_VELOCITY = 10


#YOU do the remaining 2 variables

#Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Set Text for Score
'''
variable names:  score_text, score_rect
render text: "Score: " + str(score)
antialias: True
color: GREEN
background: DARKGREEN
rect location: topleft = (10, 10)  
'''
score_text = font.render("Score: " + str(score), True, GREEN, DARKGREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Set Text for Title (Similar to Score)
'''
variable names:  title_text , title_rect 
render text: "Feed the Dragon"
antialias: True
color: GREEN
background: WHITE
rect location: centerx = WINDOW_WIDTH//2
rect location: y = 10 
'''
title_text = font.render("Feed the Dragon" + str(score), True, GREEN, WHITE)
title_rect = score_text.get_rect()
title_rect.centery = WINDOW_WIDTH//2

#Set Text for Lives (Similar to Score)
'''
variable names:  lives_text, lives_rect
render text: "Lives: " + str(player_lives)
antialias: True
color: GREEN
background: DARKGREEN
rect location: topright = (WINDOW_WIDTH - 10, 10) 
'''
lives_text = font.render(" Lives: " + str("player_lives"),True, GREEN, DARKGREEN)
lives_rect = score_text.get_rect()
rect_location = y = 10

#Set Text for Game Over (Similar to Score)
'''
variable names:  game_over_text , game_over_rect 
render text: "GAMEOVER"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) 
'''
game_over_text = font.render("GAMEOVER", True, GREEN, DARKGREEN)
game_over_rect = score_text.get_rect()
rect_location, center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


#Set Text for Continue (Similar to Score)
'''
variable names:  continue_text, continue_rect  
render text: "Press any key to play again"
antialias: True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)
'''
continue_text = font.render("Press any key to play again", True, GREEN, DARKGREEN)
continue_rect = score_text.get_rect()
rect_location, center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

#Set sounds and music
coin_sound = pygame.mixer.Sound("coin_sound.wav")
''' YOU do for miss_sound.  '''
''' Set the miss_sounds volume to 0.1 with .set_volume(0.1)'''
pygame.mixer.music.load("ftd_background_music.wav")

#Set images
'''
variable names:  player_image, player_rect  
image source: "dragon_right.png"
rect location: left = 32
rect location: centery = WINDOW_HEIGHT // 2
'''
player_image = pygame.image.load("dragon_right.png")
player_rect = player_image.get_rect()
player_rect.left = 32
player_rect.centery = WINDOW_HEIGHT // 2

'''
variable names:  coin_image, coin_rect  
image source: "coin.png"
rect location: x = WINDOW_WIDTH + BUFFER_DISTANCE
rect location: y = 0.   Note this will be a rando number.  Just later.  
'''
coin_image = pygame.image.load("dragon_right.png")
coin_rect = player_image.get_rect()



pygame.mixer.music.play(-1, 0.0)

















# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       #check for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.y > 64:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    #Fill the display
    display_surface.fill(BLACK)

    display_surface.blit(score_text, score_rect)
    ''' YOU DO:  blit title_text and title_rect'''
    ''' YOU DO:  blit lives_text and lives_rect'''
    display_surface.blit(player_image, player_rect)

    display_surface.blit(player_image, player_rect)
    ''' YOU DO:  blit coin_image and coin_rect'''

    #Update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()