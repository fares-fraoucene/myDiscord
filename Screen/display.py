import pygame 
import Tools as tools
import Screen as cs


class Display():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Discord')
        self.text = tools.Text(self)
        self.picutre = tools.Picture(self)
        self.screen_display = cs.Connexion_Screen_display(self)
        self.button = tools.Button(self)
        self.text_area_email_connexion = ''
        self.text_area_password_connexion = ''
        self.text_area_rect_email_connexion = pygame.Rect(250, 240, 300, 25)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if self.screen_display == 1:
                        if self.text_area_email_active == True:
                            if event.key == pygame.K_RETURN:
                                print("Text Area 5:", self.text_area_email_connexion)
                            if event.type == pygame.K_BACKSPACE:
                                self.text_area_email_connexion = self.text_area_email_connexion[:-1]
                            else:
                                self.text_area_email_connexion += event.unicode
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.is_mouse_inside_text_area(self.text_area_rect_email_connexion):
                                self.text_area_email_active = True
                                self.text_area_password_active = False
                        
            if self.screen_display.get_state() == 1:
                self.screen_display.screen_connection()
            elif self.screen_display.get_state() == 2:
                self.screen_display.screen_inscription()  
            elif self.screen_display.get_state() == 3:
                self.screen_display.private_mesage()
            elif self.screen_display.get_state() == 4:
                self.screen_display.public_message()
    def get_event(self):
        return self.event
    
    def is_mouse_inside_text_area(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)


            
            
            
            
    
    