import sqlite3
import mysql.connector

def inserer_utilisateur(username, nom, email, password):
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "toto", database = "my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO utilisateurs (prenom, nom, email, mot_de_passe) VALUES ('{username}', '{nom}', '{email}', '{password}')")

    conn.commit()
    conn.close()
def ajouter_ami(id_utilisateur, prenom_ami):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO amis (id_utilisateur, prenom_ami) VALUES (%s, %s)", (id_utilisateur, prenom_ami))
    conn.commit()
def display_ami(id_utilisateur):
    conn = mysql.connector.connect(host = "localhost", user = "root", password = "toto", database = "my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT utilisateurs.prenom FROM utilisateurs INNER JOIN amis ON utilisateurs.id = amis.id_utilisateur WHERE amis.id_utilisateur = %s", (id_utilisateur,))

    amis = cursor.fetchall()
    cursor.close()
    conn.close()
    return amis