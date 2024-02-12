import pygame 
import Connexion_Screen as cs


class Display():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Discord')
        self.text = cs.Text(self)
        self.picutre = cs.Picture(self)
        self.screen_display = cs.Connexion_Screen_display(self)
        self.state = "Inscription"




    def get_screen(self):
        return self.screen


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if self.state == "Connexion":
                self.screen_display.screen_connection()
            elif self.state == "Inscription":
                self.screen_display.screen_inscription()
            
            
    
    