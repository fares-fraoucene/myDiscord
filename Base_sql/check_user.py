import mysql.connector

def check_user(email, password):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    query = "SELECT email, mot_de_passe FROM utilisateurs WHERE email = %s AND mot_de_passe = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return True
    else:
        return False

