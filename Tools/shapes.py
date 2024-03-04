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
    def draw_line(self, start_pos, end_pos, color, width):
        pygame.draw.line(self.screen, color, start_pos, end_pos, width)