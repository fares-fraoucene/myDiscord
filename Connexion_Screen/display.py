import pygame 
import Tools as tools
import Connexion_Screen as cs


class Display():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Discord')
        self.text = tools.Text(self)
        self.picutre = tools.Picture(self)
        self.screen_display = cs.Connexion_Screen_display(self)
        self.button = tools.Button(self)
    def run(self):
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
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


            
            
            
            
    
    