import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''to manage the bullets fired from the ship'''

    def __init__(self,ai_settings,screen,ship):
        '''Create a bullet object at the ships current position'''
        super(Bullet,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0 , 0 ,ai_settings.bullet_width , ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx   
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        set.color = ai_settings.bullet_speed_factor