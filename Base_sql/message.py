import mysql.connector

def displaymessage():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM message_public")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return messages


def get_username_from_message_id():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT u.prenom FROM message_public m INNER JOIN utilisateurs u ON m.id_utilisateur = u.id")
    usernames = cursor.fetchall()

    cursor.close()
    conn.close()
    return usernames


def addmessage_publique(user_id, content):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO message_public (id_utilisateur, content) VALUES ({user_id}, '{content}')")
    conn.commit()
    conn.close()

def addmessage_prive(content):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO messages (content) VALUES ('{content}')")
    conn.commit()
    conn.close()