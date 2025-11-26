# movies_queries.py
# Author: Alexander Baldree
# Assignment: Module-7
# Description: Query the movies database and display results for studios,
#              genres, movies under 2 hours, and directors with their films.

import mysql.connector

# ------------------------------
# Connect to the MySQL database
# ------------------------------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gillmore21",
        database="movies"
    )
    cursor = db.cursor()
    print("Connected to the movies database successfully!\n")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# ------------------------------
# Query 1: Select all fields from the studio table
# ------------------------------
print("Query 1: All Studios")
cursor.execute("SELECT studio_id, studio_name FROM studio;")
for studio_id, studio_name in cursor.fetchall():
    print(f"Studio ID: {studio_id}\nStudio Name: {studio_name}\n")
print("-" * 40)

# ------------------------------
# Query 2: Select all fields from the genre table
# ------------------------------
print("Query 2: All Genres")
cursor.execute("SELECT genre_id, genre_name FROM genre;")
for genre_id, genre_name in cursor.fetchall():
    print(f"Genre ID: {genre_id}\nGenre Name: {genre_name}\n")
print("-" * 40)

# ------------------------------
# Query 3: Movies with runtime < 2 hours
# ------------------------------
print("Query 3: Movies with runtime < 2 hours")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;")

for film_name, film_runtime in cursor.fetchall():
    print(f"Film Name: {film_name}\nRuntime: {film_runtime} minutes\n")
print("-" * 40)

# ------------------------------
# Query 4: Films grouped by director
# ------------------------------
print("Query 4: Films grouped by Director")
cursor.execute("""
    SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') AS films
    FROM film
    GROUP BY film_director;
""")

for film_director, films in cursor.fetchall():
    print(f"Director: {film_director}\nFilms: {films}\n")
print("-" * 40)

# ------------------------------
# Close the database connection
# ------------------------------
cursor.close()
db.close()
print("Database connection closed.")
