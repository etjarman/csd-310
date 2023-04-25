# Eric Jarman		22 Apr 2023			Module7.2

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "movies_user",
	"password": "popcorn",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)

	print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\n  Press confirm key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")

	else:
		print(err)

#finally:
#	db.close()

cursor = db.cursor()
#selecting fields for studio
cursor.execute("SELECT studio_id, studio_name FROM studio;")  

studio = cursor.fetchall()

print("\n -- DISPLAYING Studio RECORDS --")

for studio in studio:
	print(" Studio ID: {}\n Studio:{}\n  ".format(studio[0], studio[1]))  # two fields

cursor = db.cursor()
#selecting fields for genre
cursor.execute("SELECT genre_id, genre_name FROM genre;")  

genre = cursor.fetchall()

print(" -- DISPLAYING Genre RECORDS --")

for genre in genre:
	print(" Genre ID: {}\n Genre:{}\n  ".format(genre[0], genre[1]))  # two fields

cursor = db.cursor()
#selecting fields for film
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")  

films = cursor.fetchall()

print(" -- DISPLAYING Short Film RECORDS --") #short films meaning less than 2 hours

for film in films:
	print(" Film Name: {}\n Runtime:{}\n  ".format(film[0], film[1]))  # two fields

cursor = db.cursor()
#selecting fields for directors
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")  

directors = cursor.fetchall()

print(" -- DISPLAYING Director RECORDS in Order --") #in order by director names

for director in directors:
	print(" Film Name: {}\n Directed By:{}\n  ".format(director[0], director[1]))  # two fields