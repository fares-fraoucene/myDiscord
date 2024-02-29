import pygame

class Text():
    def __init__(self,display):
        pygame.font.init()
        self.display = display
        self.screen = self.display.screen
        self.text_area = ""
        self.text_active =  False
        
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
            self.text_active = True
        else:
            self.text_active = False
            for self.event in pygame.event.get():
                if self.event.type == pygame.KEYDOWN and self.text_active:
                    if self.event.key == pygame.K_BACKSPACE:
                        self.text_area = self.text_area[:-1]
                    else:
                        self.text_area += self.event.unicode

    def is_mouse_inside_text_area(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)
