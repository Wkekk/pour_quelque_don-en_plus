import mysql.connector as mysqlpyth



bdd = None
cursor = None


def connexion():
	global bdd
	global cursor
	bdd = mysqlpyth.connect(user='root', password='root', host='localhost',
	port="8081", database='flask_don')
	cursor = bdd.cursor()


def deconnexion():
	global bdd
	global cursor
	cursor.close()
	bdd.close()



def ecrire_dons(titre, nom, prenom, mail, montant):
	global cursor
	global bdd
	connexion()
	query = 'INSERT INTO dons(titre, nom, prenom, mail, montant) VALUES("'+titre+'","'+nom+'", "'+prenom+'", "'+mail+'", "'+montant+'");'
	cursor.execute(query)
	bdd.commit()
	deconnexion()



