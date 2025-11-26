# movies_queries.py
# Author: Alexander Baldree
# Assignment: Module-7
# Description: Query the movies database and display results for studios, genres, movies under 2 hours, and directors with their films.

import mysql.connector

# ------------------------------
# Connect to the MySQL database
# ------------------------------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",          # Replace with your MySQL username
        password="Gillmore21",  # Updated password
        database="movies"       # Ensure your database is named 'movies'
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
# Query 3: Select movies with run time less than 2 hours
# ------------------------------
print("Query 3: Movies with run time < 2 hours")
cursor.execute("SELECT film_name, length FROM film WHERE length < 120;")
for film_name, length in cursor.fetchall():
    print(f"Film Name: {film_name}\nRuntime: {length} minutes\n")


# ------------------------------
# Query 4: List films and directors grouped by director
# ------------------------------
print("Query 4: Films grouped by Director")
cursor.execute("""
    SELECT director, GROUP_CONCAT(film_name SEPARATOR ', ') AS films
    FROM film
    GROUP BY director;
""")
for director, films in cursor.fetchall():
    print(f"Director: {director}\nFilms: {films}\n")
print("-" * 40)

# ------------------------------
# Close the database connection
# ------------------------------
cursor.close()
db.close()
print("Database connection closed.")
