import sqlite3

def init_db():
    conn = sqlite3.connect('voyage_ai.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS trips 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, user_email TEXT, departure TEXT, 
                  destination TEXT, content TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def save_trip(email, depart, dest, content):
    conn = sqlite3.connect('voyage_ai.db')
    c = conn.cursor()
    c.execute("INSERT INTO trips (user_email, departure, destination, content) VALUES (?, ?, ?, ?)",
              (email, depart, dest, content))
    conn.commit()
    conn.close()

def get_user_trips(email):
    conn = sqlite3.connect('voyage_ai.db')
    c = conn.cursor()
    c.execute("SELECT destination, content, date FROM trips WHERE user_email = ? ORDER BY date DESC", (email,))
    data = c.fetchall()
    conn.close()
    return data