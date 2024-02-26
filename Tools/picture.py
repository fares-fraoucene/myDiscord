import pygame

class Picture():
    def __init__(self,display) -> None:
        self.display = display
        self.screen = self.display.screen

    def draw_picture(self,picture, x, y, height, width):
        self.picture = pygame.image.load(picture)
        self.picture_transorm = pygame.transform.scale(self.picture, (width,height))
        self.draw = self.screen.blit(self.picture_transorm, (x, y))
        return self.draw