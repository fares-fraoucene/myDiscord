import pygame 
import Connexion_Screen as cs


class Display():
    def __init__(self):
        # self.text = cs.Text()
        # self.picutre = cs.Picture()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Discord')

    def update(self):
        pygame.display.update()

    def get_screen(self):
        return self.screen

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.fill("White")
            # self.text.draw_text(self.screen,"Discord",10, 400, 300)
            # self.picutre.draw_picture(self.screen, "Asset\image\Serveur_Discord.png", 300, 500, 50, 100)
            self.update()
    
    