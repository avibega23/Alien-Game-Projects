import pygame

class Ship():

    def __init__(self,screen):
        '''initiliaze the ship and its starting point'''
        self.screen = screen

        #FOR LOADING THE SHIP IMAGE
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #centering the ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw The Ship At Its Current Location'''
        self.screen.blit(self.image,self.rect)