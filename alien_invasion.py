import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    #It Initializes a Game And Create A Screen Object and settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #set bg colour
    # bg_colour = (230,230,230)

    #starting the main loop
    while True:
        
        #for watching the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #redrawing the screen colour each pass through the loop
        screen.fill(ai_settings.bg_color)


        pygame.display.flip()
run_game()