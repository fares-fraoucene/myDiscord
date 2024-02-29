import sqlite3

def supprimer_utilisateur(username):
    conn = sqlite3.connect('my_discord.sql')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM utilisateurs WHERE username = ?", (username,))
    conn.commit()
    conn.close()
