import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO dons (titre, nom, prenom, mail, montant) VALUES (?, ?, ?, ?, ?)",
            ('Mme.', 'alice', 'bob', 'bobalice@hotmail.com', 1)
            )

cur.execute("INSERT INTO dons (titre, nom, prenom, mail, montant) VALUES (?, ?, ?, ?, ?)",
            ('Mx.', 'charles', 'damien', 'charlesdamien@hotmail.com', 1)
            )
connection.commit()
connection.close()