import sqlite3

connection = sqlite3.connect('cinema.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

users = [
    ("Arsen",),
    ("Amina",),
    ("Ben",),
    ("Bill",),
    ("Nurlan",),
]
movies = [
    ("interstellar", "Ski-Fi"),
    ("Titanic", "Drama"),
    ("Batman", "Action"),
    ("Avatar", "Fantasy"),
    ("Joker", "Thriller"),
]
reviews = [
    (1, 1, 10),
    (2, 1, 9),
    (3, 2, 8),
    (4, 3, 7),
    (5, 4, 10),
    (1, 5, 9),
    (2, 3, 8),
    (3, 4, 9),
    (4, 2, 6),
    (5, 1, 10),
    (2, 5, 7),
]
cursor.executemany("INSERT INTO users(name) VALUES (?)", users)
cursor.executemany("INSERT INTO movies(title, genre) VALUES (?, ?)", movies)
cursor.executemany(
    "INSERT INTO reviews(user_id, movie_id, rating) VALUES (?, ?, ?)",
    reviews
)
connection.commit()

print("Отзывы пользователей:\n")
cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

print("\nВсе фильмы:\n")
cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

print("\nАгрегации:\n")
cursor.execute("SELECT AVG(rating) FROM reviews")
print("Средняя оценка:", cursor.fetchone()[0])
cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])
cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])
connection.close()