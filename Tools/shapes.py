import pygame
import pygame.gfxdraw
class Shapes:
    def __init__(self, display):
        self.display = display
        self.screen = self.display.screen
    def draw_rect(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
    def draw_circle(self, x, y, radius, color):
        pygame.draw.circle(self.screen, color, (x, y), radius)
    def draw_rounded_rect(self, x, y, width, height,color, radius=0.4):
        pygame.gfxdraw.box(self.screen, (x, y, width, height), color)
        pygame.gfxdraw.filled_circle(self.screen, x+radius, y+radius, int(radius*height), color)
        pygame.gfxdraw.filled_circle(self.screen, x+width-radius-1, y+radius, int(radius*height), color)
        pygame.gfxdraw.filled_circle(self.screen, x+radius, y+height-radius-1, int(radius*height), color)
        pygame.gfxdraw.filled_circle(self.screen, x+width-radius-1, y+height-radius-1, int(radius*height), color)
        pygame.gfxdraw.box(self.screen, (x, y+radius, width, height-radius*2), color)
        pygame.gfxdraw.box(self.screen, (x+radius, y, width-radius*2, height), color)