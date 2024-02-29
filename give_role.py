import sqlite3

def attribuer_role(username, role):
    conn = sqlite3.connect('my_discord.sql')
    cursor = conn.cursor()
    cursor.execute("UPDATE utilisateurs SET role = ? WHERE username = ?", (role, username))
    conn.commit()
    conn.close()
