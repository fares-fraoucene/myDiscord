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

def check_user_id(email):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM utilisateurs WHERE email = '{email}'")
    user_id_tuple = cursor.fetchone()
    cursor.close()
    conn.close()
    if user_id_tuple:
        return user_id_tuple[0]
    else:
        return None
def check_user_id_by_username(username):
    conn = mysql.connector.connect(host="localhost", user="root", password="toto", database="my_Discord")
    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM utilisateurs WHERE prenom = '{username}'")
    user_id_tuple = cursor.fetchone()
    cursor.close()
    conn.close()


