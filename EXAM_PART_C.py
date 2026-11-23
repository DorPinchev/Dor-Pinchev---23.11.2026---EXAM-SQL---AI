from itertools import count

from db import run_query_select, run_update_query


print("question 1:")
movies = run_query_select("SELECT * FROM Movies")
for movie in movies:
    print(movie)
print()


print("question 2:")
movie_search = input("enter movie name or part of the name: ")
movies = run_query_select("SELECT * FROM Movies where movie_name like ?", (f"%{movie_search}%",))
for movie in movies:
    print(movie)
print()


print("question 3:")
movie_name = input("enter movie name: ")
genre = input("enter genre: ")
country = input("enter country: ")
language = input("enter language: ")
year = int(input("enter year: "))
revenue = float(input("enter revenue: "))
run_update_query("INSERT INTO Movies(movie_name, genre, country, language, year, revenue) VALUES(?,?,?,?,?,?)", (movie_name, genre, country, language, year, revenue))