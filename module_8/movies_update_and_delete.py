#Eric Jarman			22 Apr 2023			Module8.2

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

def show_films(cursor, title):

     cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

     films = cursor.fetchall()

     print("\n -- {} --".format(title))

     for film in films:

          print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

cursor.execute("INSERT into film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (4, 'Star Wars', '1977', 121, 'George Lucas', 1, 2)")

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

cursor.execute("UPDATE film SET genre_id = 1 WHERE film_id = 2")

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

