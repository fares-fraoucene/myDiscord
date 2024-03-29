import pygame 
import Tools as tools
import Screen as cs
import Base_sql as base
import time


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
        self.text_area_name_inscription = ''
        self.text_area_surname_inscription = ''
        self.text_area_password_inscription = ''
        self.text_area_email_insription = ''
        self.text_area_chat_private = ''
        self.text_area_chat_public = ''
        self.text_area_rect_email_connexion = pygame.Rect(250, 240, 300, 25)
        self.text_area_rect_password_connexion = pygame.Rect(250, 300, 300, 25)
        self.text_area_rect_name_inscription = pygame.Rect(250, 360, 300, 25)
        self.text_area_rect_surname_inscription = pygame.Rect(250, 420, 300, 25)
        self.text_area_rect_password_inscription = pygame.Rect(250, 300, 300, 25)
        self.text_area_rect_email_inscription = pygame.Rect(250, 240, 300, 25)
        self.text_area_chat_private_rect = pygame.Rect(200, 550, 500, 25)
        self.text_area_chat_public_rect = pygame.Rect(150, 550, 500, 25)
        self.text_add_friends = ''
        self.text_area_rect_add_friends = pygame.Rect(250, 240, 300, 25)
        self.base = base
        self.user_found = True
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    
                    if 350 <= self.pos[0] <= 450 and 470 <= self.pos[1] <= 500 and self.screen_display.get_state() == 2:
                        self.base.inserer_utilisateur(self.text_area_surname_inscription, self.text_area_name_inscription, self.text_area_email_insription, self.text_area_password_inscription)
                        self.text_area_surname_inscription = ''
                        self.text_area_name_inscription = ''
                        self.text_area_email_insription = ''
                        self.text_area_password_inscription = ''
                    elif 350 <= self.pos[0] <= 450 and 350 <= self.pos[1] <= 380 and self.screen_display.get_state() == 1:
                        if self.base.check_user(self.text_area_email_connexion, self.text_area_password_connexion):
                            self.screen_display.go_screen_private_message()
                            self.text_area_password_connexion = ''
                            self.user_found = True
                        else:
                            self.user_found = False
                    elif self.screen_display.get_state() == 5 and 570 <= self.pos[0] <= 600 and 245 <= self.pos[1] <= 575:
                        self.base.ajouter_ami(self.base.check_user_id(self.text_area_email_connexion), self.text_add_friends)
                        self.text_add_friends = ''
                    elif self.screen_display.get_state() == 3 and 570 <= self.pos[0] <= 740 and 245 <= self.pos[1] <= 575:
                        if self.text_area_chat_private != '':
                            self.base.addmessage_prive(self.text_area_chat_private)
                            self.text_area_chat_private = ''
                    elif self.screen_display.get_state() == 4 and 670 <= self.pos[0] <= 730 and 550 <= self.pos[1] <= 561:
                        if self.text_area_chat_public != '':
                            self.base.addmessage_publique(self.base.check_user_id(self.text_area_email_connexion),self.text_area_chat_public)
                            self.text_area_chat_public = ''
                if event.type == pygame.KEYDOWN:
                    if self.text_area_email_active == True and self.screen_display.get_state() == 1:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_email_connexion = self.text_area_email_connexion[:-1]
                        else:
                            self.text_area_email_connexion += event.unicode
                    elif self.text_area_password_active == True and self.screen_display.get_state() == 1:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_password_connexion = self.text_area_password_connexion[:-1]
                        else:
                            self.text_area_password_connexion += event.unicode
                    elif self.text_area_name_active == True and self.screen_display.get_state() == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_name_inscription = self.text_area_name_inscription[:-1]
                        else:
                            self.text_area_name_inscription += event.unicode
                    elif self.text_area_surname_active == True and self.screen_display.get_state() == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_surname_inscription = self.text_area_surname_inscription[:-1]
                        else:
                            self.text_area_surname_inscription += event.unicode
                    elif self.text_area_password_inscription_active == True and self.screen_display.get_state() == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_password_inscription = self.text_area_password_inscription[:-1]
                        else:
                            self.text_area_password_inscription += event.unicode
                    elif self.text_area_email_inscription_active == True and self.screen_display.get_state() == 2:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_area_email_insription = self.text_area_email_insription[:-1]
                        else:
                            self.text_area_email_insription += event.unicode
                    elif self.text_area_chat_private_active == True and self.screen_display.get_state() == 3:
                        if event.key == pygame.K_RETURN:
                            if self.text_area_chat_private != '':
                                self.base.addmessage_prive(self.text_area_chat_private)
                                self.text_area_chat_private = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_area_chat_private = self.text_area_chat_private[:-1]
                        else:
                            self.text_area_chat_private += event.unicode
                    elif self.text_area_chat_public_active == True and self.screen_display.get_state() == 4:
                        if event.key == pygame.K_RETURN:
                            if self.text_area_chat_public != '':
                                self.base.addmessage_publique(self.base.check_user_id(self.text_area_email_connexion),self.text_area_chat_public)
                                self.text_area_chat_public = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_area_chat_public = self.text_area_chat_public[:-1]
                        else:
                            self.text_area_chat_public += event.unicode
                    elif self.text_area_add_friends_active == True and self.screen_display.get_state() == 5:
                        if event.key == pygame.K_RETURN:
                            if self.text_add_friends != '':
                                self.base.ajouter_ami(self.base.check_user_id(self.text_area_email_connexion), self.text_add_friends)
                                self.text_add_friends = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_add_friends = self.text_add_friends[:-1]
                        else:
                            self.text_add_friends += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_mouse_inside_text_area(self.text_area_rect_email_connexion) and self.screen_display.get_state() == 1:
                        self.text_area_email_active = True
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_password_connexion) and self.screen_display.get_state() == 1:
                        self.text_area_email_active = False
                        self.text_area_password_active = True
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_name_inscription) and self.screen_display.get_state() == 2:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = True
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_surname_inscription) and self.screen_display.get_state() == 2:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = True
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_password_inscription) and self.screen_display.get_state() == 2:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = True
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_email_inscription) and self.screen_display.get_state() == 2:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = True
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_chat_private_rect) and self.screen_display.get_state() == 3:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = True
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_chat_public_rect) and self.screen_display.get_state() == 4:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = True
                        self.text_area_add_friends_active = False
                    elif self.is_mouse_inside_text_area(self.text_area_rect_add_friends) and self.screen_display.get_state() == 5:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = True
                    else:
                        self.text_area_email_active = False
                        self.text_area_password_active = False
                        self.text_area_name_active = False
                        self.text_area_surname_active = False
                        self.text_area_password_inscription_active = False
                        self.text_area_email_inscription_active = False
                        self.text_area_chat_private_active = False
                        self.text_area_chat_public_active = False
                        self.text_area_add_friends_active = False
                    
            if self.screen_display.get_state() == 1:
                self.screen_display.screen_connection()
            elif self.screen_display.get_state() == 2:
                self.screen_display.screen_inscription()  
            elif self.screen_display.get_state() == 3:
                self.screen_display.private_mesage()
            elif self.screen_display.get_state() == 4:
                self.screen_display.public_message()
            elif self.screen_display.get_state() == 5:
                self.screen_display.friends()
    def get_event(self):
        return self.event
    
    def is_mouse_inside_text_area(self, rect):
        self.mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(self.mouse_pos)
