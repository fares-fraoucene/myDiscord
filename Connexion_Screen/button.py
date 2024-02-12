import pygame 

class Button:
    def __init__(self, display):
        self.display = display
        self.screen = self.display.screen
    def draw_button(self):
        self.button = pygame.draw.rect(self.screen, (0, 0, 0), (300, 500, 200, 50))
        return self.button  

    