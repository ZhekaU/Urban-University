import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users 
(id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL

)   ''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
cursor.execute('SELECT COUNT(*) FROM Users')
record_count = cursor.fetchone()[0]
if record_count == 0:
    for i in range(1, 11):
        cursor.execute('INSERT OR IGNORE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (f'User{i}', f'example{i}@gmail.com', 10 * i, 1000))
    connection.commit()

cursor.execute('SELECT id FROM Users')
b = cursor.fetchall()
for i, b in enumerate(b):
    if i % 2 == 1:
        cursor.execute('UPDATE Users SET balance = 500  WHERE id = ?', (i,))

cursor.execute('SELECT id FROM Users')
rows = cursor.fetchall()
for i in range(len(rows) + 1):
    if i % 3 == 1:
        cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

cursor.execute('SELECT username,email,age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute('DELETE FROM  Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total_user = cursor.fetchone()
print(total_user)

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()
print(total_balance)

cursor.execute('SELECT AVG(balance) FROM Users')
average_balance = cursor.fetchone()
print(average_balance)
connection.commit()
connection.close()
