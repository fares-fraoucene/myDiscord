import pygame
import Connexion_Screen as cs

class Connexion_Screen_display():
    def __init__(self,display):
        self.display = display
        self.screen = self.display.screen
        self.picture = cs.Picture(self.display)
        self.text = cs.Text(self.display)
        self.button = cs.Button(self.display)
        self.state = 1
    def update(self):
        pygame.display.update()
    def get_state(self):
        return self.state
    def change_state(self, state):
        self.state = state
        return self.state
    def go_screen_connexion(self):
        self.state = 1
    def go_screen_inscription(self):
        self.state = 2
    def main_screen(self):
        self.screen.fill("White")
        self.picture.draw_picture("Asset\image\Serveur_Discord.png", 200, 20, 100, 400)
        self.button.draw_button(200, 140, 200, 50, "White", "Connexion", "Black", 15, self.go_screen_connexion)
        self.button.draw_button(400, 140, 200, 50, "White", "Inscription", "Black", 15, self.go_screen_inscription)
        

    def screen_connection(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","Black", 15, 250, 220)
        self.text.draw_text("Mot de Passe :", "Black",15, 250, 280)
        self.button.draw_button(290, 350, 200, 50, "White", "Connexion", "Black", 17)
        self.update()

    def screen_inscription(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","Black", 15, 250, 220)
        self.text.draw_text("Mot de Passe :","Black", 15, 250, 280)
        self.text.draw_text("Nom :","Black", 15, 250, 340)
        self.text.draw_text("Prénom :","Black", 15, 250, 400)
        self.button.draw_button(290, 470, 200, 50, "White", "Inscription", "Black", 17)
        self.update()