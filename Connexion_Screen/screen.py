import pygame
import Connexion_Screen as cs

class Connexion_Screen_display():
    def __init__(self,display):
        self.display = display
        self.screen = self.display.screen
        self.state = 1
        self.picture = cs.Picture(self.display)
        self.text = cs.Text(self.display)
        self.button = cs.Button(self.display)
        
    def update(self):
        pygame.display.update()
    def get_state(self):
        return self.state
    def go_screen_connexion(self):
        self.state = 1
    def go_screen_inscription(self):
        self.state = 2
    def main_screen(self):
        self.screen.fill("gray23")
        self.picture.draw_picture("Asset\image\Serveur_Discord.png", 200, 20, 100, 400)
        self.button.draw_button(200, 140, 200, 50, "gray23", "Connexion", "ghostwhite", 15, self.go_screen_connexion)
        self.button.draw_button(400, 140, 200, 50, "gray23", "Inscription", "ghostwhite", 15, self.go_screen_inscription)
        
    def screen_connection(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","ghostwhite", 15, 250, 220)
        self.text.draw_text("Mot de Passe :", "ghostwhite",15, 250, 280)
        self.button.draw_button(290, 350, 200, 50, "gray23", "Connexion", "ghostwhite", 17)
        self.text.area_text(250, 220, 200, 30, "ghostwhite")
        self.update()

    def screen_inscription(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","ghostwhite", 15, 250, 220)
        self.text.draw_text("Mot de Passe :","ghostwhite", 15, 250, 280)
        self.text.draw_text("Nom :","ghostwhite", 15, 250, 340)
        self.text.draw_text("Prénom :","ghostwhite", 15, 250, 400)
        self.button.draw_button(290, 470, 200, 50, "gray23", "Inscription", "ghostwhite", 17)
        self.update()
        
    