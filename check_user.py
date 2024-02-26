import sqlite3

def verifier_utilisateur(username):
    conn = sqlite3.connect('my_discord.sql')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user
