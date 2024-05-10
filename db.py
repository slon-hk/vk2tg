import sqlite3

def db_start():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, user_id int, vk_id varchar(220))")
    conn.commit()
    cur.close()
    conn.close()

def send_vk_token(user, token):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    cur.execute("INSERT INTO users (user_id, vk_id) VALUES ('%s', '%s')" % (user, token))
    
    conn.commit()
    cur.close()

def return_db():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM users")
    call = cur.fetchall()
    cur.close()
    
    info = ""
    for i in call:
        info += f"id: {i[0]}\nuser id: {i[1]}\ntoken: {i[2]}"
    
    return info
    