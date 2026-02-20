import sqlite3

# 1. Connect to (or create) the database
conn = sqlite3.connect("internship.db")
cur = conn.cursor()

# 2. Create the interns table
cur.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);
""")

# 3. Insert sample data
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Aarav', 'Data Science', 12000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Meera', 'Web Development', 10000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Rohan', 'AI & ML', 15000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Sanya', 'Cyber Security', 11000)")
cur.execute("INSERT INTO interns (name, track, stipend) VALUES ('Kiran', 'Data Analytics', 13000)")

conn.commit()

# 4. SELECT only name and track (NOT SELECT *)
print("Intern Names and Tracks:")
cur.execute("SELECT name, track FROM interns")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()