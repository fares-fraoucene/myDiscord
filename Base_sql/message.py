import mysql.connector

def displaymessage():
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM message_public")
    messages = cursor.fetchall()
    return messages
def addmessage_publique(content):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO message_public (content) VALUES ('{content}')")
    conn.commit()
    conn.close()
def addmessage_prive(content):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO messages (content) VALUES ('{content}')")
    conn.commit()
    conn.close()