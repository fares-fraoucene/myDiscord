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
    

    def area_text(self,x,y,width,height,color):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.text_area_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen,color,self.text_area_rect)
        if self.is_mouse_inside_text_area(self.text_area_rect):
            if self.click[0] == 1:
                self.text_active = True
        else:
            self.text_active = False
            
    def is_mouse_inside_text_area(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)
