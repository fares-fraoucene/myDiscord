import pygame

class Shapes:
    def __init__(self, display):
        self.display = display
        self.screen = self.display.screen
    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))

    