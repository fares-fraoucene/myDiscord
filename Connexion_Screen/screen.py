import pygame
import Connexion_Screen as cs

class Connexion_Screen_display():
    def __init__(self,display):
        self.display = display
        self.screen = self.display.screen
        self.picture = cs.Picture(self.display)
        self.button = cs.Button(self.display)
        self.text = cs.Text(self.display)
    def update(self):
        pygame.display.update()
    def main_screen(self):
        self.screen.fill("White")
        self.picture.draw_picture("Asset\image\Serveur_Discord.png", 230, 0, 150, 350)
    def screen_connection(self):
        self.main_screen()
        self.text.draw_text("Adresse email :", 15, 250, 220)
        self.text.draw_text("Mot de Passe :", 15, 250, 300)
        self.update()

    def screen_inscription(self):
        self.main_screen()
        self.text.draw_text("Adresse email :", 15, 250, 220)
        self.text.draw_text("Mot de Passe :", 15, 250, 300)
        self.text.draw_text("Nom :", 15, 250, 380)
        self.update()