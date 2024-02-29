import pygame
import Tools as tools
class Connexion_Screen_display():
    def __init__(self,display):
        self.display = display
        self.screen = self.display.screen
        self.state = 1
        self.picture = tools.Picture(self.display)
        self.text = tools.Text(self.display)
        self.button = tools.Button(self.display)
        self.shapes = tools.Shapes(self.display)

        
    def update(self):
        pygame.display.update()
    def get_state(self):
        return self.state
    def go_screen_connexion(self):
        self.state = 1
    def go_screen_inscription(self):
        self.state = 2
    def go_screen_private_message(self):
        self.state = 3
    def go_screen_public_message(self):
        self.state = 4
    
    def main_screen(self):
        self.screen.fill("gray23")
        self.picture.draw_picture("Asset\image\Serveur_Discord.png", 200, 20, 100, 400)
        self.button.draw_button(200, 140, 200, 50, "gray23", "Connexion", "ghostwhite", 15, self.go_screen_connexion)
        self.button.draw_button(400, 140, 200, 50, "gray23", "Inscription", "ghostwhite", 15, self.go_screen_inscription)
        
    def main_message_screen(self):
        self.screen.fill("gray23")
        self.button.draw_button(250, 30, 200, 50, "gray23", "Message Privé", "ghostwhite", 15, self.go_screen_private_message)
        self.button.draw_button(450, 30, 200, 50, "gray23", "Message Général", "ghostwhite", 15, self.go_screen_public_message)
        self.button.draw_button(30, 540, 100, 50, "gray23", "Déconnexion", "ghostwhite", 15, self.go_screen_connexion)
        

    def screen_connection(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","ghostwhite", 15, 250, 220)
        self.text.draw_text("Mot de Passe :", "ghostwhite",15, 250, 280)
        self.button.draw_button(290, 350, 200, 50, "gray23", "Connexion", "ghostwhite", 17, self.go_screen_private_message)
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_email_connexion)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_email_connexion),(250,240))
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_password_connexion)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_password_connexion),(250,300))
        self.update()

    def screen_inscription(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","ghostwhite", 15, 250, 220)
        self.text.draw_text("Mot de Passe :","ghostwhite", 15, 250, 280)
        self.text.draw_text("Nom :","ghostwhite", 15, 250, 340)
        self.text.draw_text("Prénom :","ghostwhite", 15, 250, 400)
        self.button.draw_button(290, 470, 200, 50, "gray23", "Inscription", "ghostwhite", 17)
        # self.text.area_text(250, 240, 300, 25, "ghostwhite")
        # self.text.area_text(250, 300, 300, 25, "ghostwhite")
        # self.text.area_text(250, 360, 300, 25, "ghostwhite")
        # self.text.area_text(250, 420, 300, 25, "ghostwhite")
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_email_inscription)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_email_insription),(250,240))
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_password_inscription)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_password_inscription),(250,300))
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_name_inscription)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_name_inscription),(250,360))
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_surname_inscription)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_surname_inscription),(250,420))
        self.update()

    def private_mesage(self):
        self.main_message_screen()
        self.text.draw_text("Amis","ghostwhite", 15, 50, 50)
        self.shapes.draw_rect(20, 100, 140, 400, "ghostwhite")
        self.text.draw_text("Message :","ghostwhite", 15, 200, 520)
        self.text.area_text(200, 550, 500, 25, "ghostwhite")
        self.shapes.draw_rect(200, 100, 550, 400, "ghostwhite")
        self.button.draw_button(670, 535, 100, 50, "gray23", "Envoyer", "ghostwhite", 17, None)
        self.text.draw_text("Appel","Black", 15, 680, 110)
        self.update()

    def public_message(self):
        self.main_message_screen()
        self.text.draw_text("Message :","ghostwhite", 15, 150, 520)
        self.text.area_text(150, 550, 500, 25, "ghostwhite")
        self.shapes.draw_rect(50, 100, 700, 400, "ghostwhite")
        self.button.draw_button(670, 535, 100, 50, "gray23", "Envoyer", "ghostwhite", 17, None)
        self.update()
        
    