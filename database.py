import sqlite3

# Creating database and connect to them
conn = sqlite3.connect('lectures.db')
c = conn.cursor()

# Create table with coloumns title, lecturer и duration
c.execute('''CREATE TABLE IF NOT EXISTS lectures
                  (title TEXT, lecturer TEXT, duration INTEGER)''')

# Adding threes lectures
lectures = [('Management', 'Donatus', 40),
            ('Python', 'Donatus', 80),
            ('Java', 'Tomas', 80)]

c.executemany('INSERT INTO lectures VALUES (?, ?, ?)', lectures)

# Print all lecturas lenght more than 50 minuts
print("lecturas lenght more than 50 minuts:")
c.execute('SELECT * FROM lectures WHERE duration > 50')
for row in c.fetchall():
    print(row)

# ОUpdating all lectures "Python" in "Python Programming"
c.execute('UPDATE lectures SET title = "Python Programming" WHERE title = "Python"')

# Deleting lecturs, readed with "Tomas"
c.execute('DELETE FROM lectures WHERE lecturer = "Tomas"')

# Print all lectures
print("\nAll lectures:")
c.execute('SELECT * FROM lectures')
for row in c.fetchall():
    print(row)

# Close connection to all databases
conn.commit()
conn.close()
