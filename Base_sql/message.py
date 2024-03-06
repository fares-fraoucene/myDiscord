import mysql.connector

def displaymessage():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM message_public ORDER BY date_creation ASC")    
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return messages
def display_time_message_privé():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT date_creation FROM message_public ORDER BY date_creation ASC")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()

def get_username_from_message_id():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT u.prenom FROM message_public m INNER JOIN utilisateurs u ON m.id_utilisateur = u.id ORDER BY m.date_creation ASC")
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