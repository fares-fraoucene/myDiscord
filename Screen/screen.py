import pygame
import Tools as tools
import Base_sql as base
class Connexion_Screen_display():
    def __init__(self,display):
        self.display = display
        self.screen = self.display.screen
        self.state = 1
        self.picture = tools.Picture(self.display)
        self.text = tools.Text(self.display)
        self.button = tools.Button(self.display)
        self.shapes = tools.Shapes(self.display)
        self.base = base
        
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
        self.text.draw_text("Connexion","ghostwhite", 20, 350, 350)
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_email_connexion)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_email_connexion),(250,240))
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_rect_password_connexion)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_password_connexion),(250,300))
        if self.display.user_found == False:
            self.text.draw_text("Adresse email ou mot de passe incorrect","red", 15, 250, 400)
        self.update()

    def screen_inscription(self):
        self.main_screen()
        self.text.draw_text("Adresse email :","ghostwhite", 15, 250, 220)
        self.text.draw_text("Mot de Passe :","ghostwhite", 15, 250, 280)
        self.text.draw_text("Nom :","ghostwhite", 15, 250, 340)
        self.text.draw_text("Prénom :","ghostwhite", 15, 250, 400)
        self.text.draw_text("Inscription","ghostwhite", 20, 350, 480)
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
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_chat_private_rect)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_chat_private),(200,550))
        self.shapes.draw_rect(200, 100, 550, 400, "ghostwhite")
        self.text.draw_text("Envoyer","ghostwhite", 15,710, 550)
        self.text.draw_text("Appel","Black", 15, 680, 110)
        self.update()

    def public_message(self):
        self.main_message_screen()
        self.text.draw_text("Message :","ghostwhite", 15, 150, 520)
        self.shapes.draw_rect(50, 100, 700, 400, "ghostwhite")
        self.text.draw_text("Envoyer","ghostwhite", 15,670, 550)
        pygame.draw.rect(self.screen,"ghostwhite", self.display.text_area_chat_public_rect)
        self.screen.blit(self.text.draw_text_area_text(self.display.text_area_chat_public),(150,550))
        self.afficher_donnees(self.base.displaymessage())
        self.afficher_donnees_public(self.base.get_username_from_message_id())
        self.update()

    def afficher_donnees(self,donnees):
        taille_case_x = 110
        taille_case_y = 20
        decalage_x, decalage_y = 100, 110
        for i, ligne in enumerate(donnees):
            for j, valeur in enumerate(ligne):
                x = j * taille_case_x + decalage_x
                y = i * taille_case_y + decalage_y
                font = pygame.font.Font(None, 20)
                texte = font.render(str(valeur), True, "black")
                self.screen.blit(texte, (x + 20, y + 20))

    def afficher_donnees_public(self, donnees):
        taille_case_x = 110
        taille_case_y = 20
        decalage_x, decalage_y = 50, 110
        for i, ligne in enumerate(donnees):
            for j, valeur in enumerate(ligne):
                x = j * taille_case_x + decalage_x
                y = i * taille_case_y + decalage_y
                font = pygame.font.Font(None, 20)
                texte = font.render((f"{valeur} :"), True, "black")
                self.screen.blit(texte, (x + 20, y + 20))

