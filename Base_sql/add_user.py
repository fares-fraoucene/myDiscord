import sqlite3
import mysql.connector

def inserer_utilisateur(username, nom, email, password):
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "toto", database = "my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO utilisateurs (prenom, nom, email, mot_de_passe) VALUES ('{username}', '{nom}', '{email}', '{password}')")

    conn.commit()
    conn.close()