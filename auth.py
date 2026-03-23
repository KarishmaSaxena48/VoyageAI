import hashlib
import sqlite3

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def signup_user(email, password):
    conn = sqlite3.connect('voyage_ai.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (email, password) VALUES (?,?)", (email, make_hashes(password)))
        conn.commit()
        return True
    except: return False
    finally: conn.close()

def login_user(email, password):
    conn = sqlite3.connect('voyage_ai.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE email = ?", (email,))
    data = c.fetchone()
    conn.close()
    if data and data[0] == make_hashes(password): return True
    return False