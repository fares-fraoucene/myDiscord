import sqlite3

def inserer_utilisateur(username, prenom, email, password):
    conn = sqlite3.connect('my_discord.sql')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO utilisateurs (username, prenom, email, password) VALUES (?, ?, ?, ?)", (username, prenom, email, password))
    conn.commit()
    conn.close()