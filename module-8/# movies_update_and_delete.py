# movies_update_and_delete.py
# Author: Alexander Baldree
# Assignment: Module-8
# Description: Display, insert, update, and delete films in the movies database.

import mysql.connector

# ---------------------------------------------------
# Function to display films using INNER JOINs
# ---------------------------------------------------
def show_films(cursor, title):
    # Inner join query to pull film, genre, and studio names
    cursor.execute("""
        SELECT film.film_name AS Name,
               film.film_director AS Director,
               genre.genre_name AS Genre,
               studio.studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("\nFilm Name: {}"
              "\nDirector: {}"
              "\nGenre Name: {}"
              "\nStudio Name: {}".format(
                  film[0], film[1], film[2], film[3]
              ))


# ---------------------------------------------------
# Connect to database
# ---------------------------------------------------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gillmore21",
        database="movies"
    )
    cursor = db.cursor()
    print("Connected successfully!\n")
except mysql.connector.Error as err:
    print("Error: ", err)
    exit()


# ---------------------------------------------------
# DISPLAY ORIGINAL FILMS
# ---------------------------------------------------
show_films(cursor, "DISPLAYING FILMS")


# ---------------------------------------------------
# INSERT a new film — choose ANY film except Star Wars
# ---------------------------------------------------
insert_query = """
    INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
new_film_data = ("Inception", "2010", 148, "Christopher Nolan", 1, 1)  
# Studio_id 1 and genre_id 1 must exist!

cursor.execute(insert_query, new_film_data)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")


# ---------------------------------------------------
# UPDATE film Alien → change genre to Horror
# ---------------------------------------------------
update_query = """
    UPDATE film
    SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
    WHERE film_name = 'Alien';
"""

cursor.execute(update_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE– Changed Alien to Horror")


# ---------------------------------------------------
# DELETE Gladiator
# ---------------------------------------------------
delete_query = "DELETE FROM film WHERE film_name = 'Gladiator';"

cursor.execute(delete_query)
db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")


# ---------------------------------------------------
# Close DB connection
# ---------------------------------------------------
cursor.close()
db.close()
print("\nDatabase connection closed.")
