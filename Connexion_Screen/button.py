import pygame 
import time

class Button:
    def __init__(self, display):
        self.button_clicked = False
        self.display = display
        self.screen = self.display.screen
    def draw_button(self, x, y, width, height, color, text, text_color, font_size, action = None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.font = pygame.font.Font('freesansbold.ttf', font_size)
        self.text_surface = self.font.render(text, True, text_color)
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, button_rect)
        self.screen.blit(self.text_surface, (x + (width / 2 - self.text_surface.get_width() / 2), y + (height / 2 - self.text_surface.get_height() / 2)))
        if button_rect.collidepoint(self.mouse):
            if self.click[0] == 1 and action is not None and not self.button_clicked:
                action()
                self.button_clicked = True  
                time.sleep(0.2)
                self.button_clicked = False
        else:
            self.button_clicked = False 
    


    
    