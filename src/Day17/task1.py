import sqlite3
conn = sqlite3.connect("internship.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);
""")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Aarav', 'Data Science', 12000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Meera', 'Web Development', 10000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Rohan', 'AI & ML', 15000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Sanya', 'Cyber Security', 11000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Kiran', 'Data Analytics', 13000)")

conn.commit()
print("Intern Names and Tracks:")
cur.execute("SELECT name, track FROM interns")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()