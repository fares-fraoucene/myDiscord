import pygame
from Connexion_Screen import Display
class Text(Display):
    def __init__(self,display):
        pygame.font.init()
        self.display = display
        self.screen = self.display.screen
        
    def draw_text(self,text,taille,x,y):
        self.font = pygame.font.Font('freesansbold.ttf', taille)
        self.config_text = self.font.render(text, True, (0, 0, 0))
        self.draw = self.screen.blit(self.config_text, (x, y))
        return self.draw