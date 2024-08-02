import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            # elif event.key == pygame.K_UP:
            #     ship.moving_up = True
            # elif event.key == pygame.K_DOWN:
            #     ship.moving_down = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            # elif event.key == pygame.K_UP:
            #     ship.moving_up = False
            # elif event.key == pygame.K_DOWN:
            #     ship.moving_down = False

def update_screen(ai_settings,screen,ship):
    '''to update the screen'''
      #redrawing the screen colour each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()