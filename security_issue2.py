from security_issue import connect_db

def get_user(username):
    # Vulnerable to SQL injection
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result