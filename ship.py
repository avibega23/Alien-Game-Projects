import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        '''initiliaze the ship and its starting point'''
        self.screen = screen
        self.ai_settings = ai_settings


        #FOR LOADING THE SHIP IMAGE
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #centering the ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False

        # self.ship_speed_factor = 1.5

    def update(self):
        if self.moving_right and self.rect.right < 1366:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # elif self.moving_up:
        #     # and self.rect.up > 0:
        #     self.center -= self.ai_settings.ship_speed_factor
        # elif self.moving_down: 
        # # and self.rect.down < 768:
        #     self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        '''Draw The Ship At Its Current Location'''
        self.screen.blit(self.image,self.rect)