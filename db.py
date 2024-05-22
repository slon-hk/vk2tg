import sqlite3

def db_start():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER UNIQUE," \
                " vk_id TEXT UNIQUE, page_numb INTEGER DEFAULT 1 CHECK(page_numb > 0))")
    conn.commit()
    cur.close()
    conn.close()

def send_vk_token(user: int, token: str):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (user_id, vk_id) VALUES ('%s', '%s')" % (user, token))
    conn.commit()
    cur.close()
        
def filtr_db(user: int):
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    info = cur.execute(f"SELECT user_id FROM users WHERE user_id = {user}")
    cur.close()
    conn.close()
    if info is None: 
        return False
    return True

def return_db():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    call = cur.fetchall()
    cur.close()
    
    info = ""
    for i in call:
        info += f"id: {i[0]}\nuser id: {i[1]}\ntoken: {i[2]}\n\n"
    
    return info