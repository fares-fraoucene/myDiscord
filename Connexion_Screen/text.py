import pygame
class Text():
    def __init__(self,display):
        pygame.font.init()
        self.display = display
        self.screen = self.display.screen

        
    def draw_text(self,text,color,taille,x,y):
        self.font = pygame.font.Font('freesansbold.ttf', taille)
        self.config_text = self.font.render(text, True, color)
        self.draw = self.screen.blit(self.config_text, (x, y))
        return self.draw
    def area_text(self):
        pass
