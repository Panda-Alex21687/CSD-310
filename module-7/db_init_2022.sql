-- ========================================
-- movies_database.sql
-- Author: Alexander Baldree
-- Assignment: Module-7
-- Description: Creates the movies database, tables, and sample data
-- ========================================

-- ----------------------------------------
-- Create the movies database
-- ----------------------------------------
CREATE DATABASE IF NOT EXISTS movies;
USE movies;

-- ----------------------------------------
-- Create the studio table
-- ----------------------------------------
CREATE TABLE IF NOT EXISTS studio (
    studio_id INT AUTO_INCREMENT PRIMARY KEY,
    studio_name VARCHAR(100) NOT NULL
);

-- Insert data into studio
INSERT INTO studio (studio_name) VALUES 
('Pixar'),
('Warner Bros'),
('Universal Pictures');

-- ----------------------------------------
-- Create the genre table
-- ----------------------------------------
CREATE TABLE IF NOT EXISTS genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL
);

-- Insert data into genre
INSERT INTO genre (genre_name) VALUES 
('Animation'),
('Action'),
('Comedy'),
('Drama');

-- ----------------------------------------
-- Create the film table
-- ----------------------------------------
CREATE TABLE IF NOT EXISTS film (
    film_id INT AUTO_INCREMENT PRIMARY KEY,
    film_name VARCHAR(100) NOT NULL,
    runtime INT,           -- runtime in minutes
    director VARCHAR(100),
    studio_id INT,
    genre_id INT,
    FOREIGN KEY (studio_id) REFERENCES studio(studio_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

-- Insert data into film
INSERT INTO film (film_name, runtime, director, studio_id, genre_id) VALUES
('Toy Story', 81, 'John Lasseter', 1, 1),
('Inception', 148, 'Christopher Nolan', 2, 2),
('Shrek', 90, 'Andrew Adamson', 3, 1),
('The Dark Knight', 152, 'Christopher Nolan', 2, 2),
('Up', 96, 'Pete Docter', 1, 1),
('Jurassic Park', 127, 'Steven Spielberg', 3, 2),
('The Hangover', 100, 'Todd Phillips', 3, 3),
('La La Land', 128, 'Damien Chazelle', 2, 4);
