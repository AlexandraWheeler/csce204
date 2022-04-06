# Author: Alexandra Wheeler
# Movie List

from movie import Movie


def getMovies():
    movies = []
    
    with open("assignments/assignment24/movies.txt") as file:
        for line in file:
            data = line.split(",")
            movieTitle = data[0].strip()
            description = data[1].strip()
            #actors = []
            actor = data[2].split('*')
            #actors.append(actor)
            genre = data[3].strip().lower()
            rating = data[4].strip()
            movies.append(Movie(movieTitle, description,actor, genre, rating))
    return movies



movie_list = getMovies()

print("Movie Program! ")
while True:
    command = input("(L)ist Movies, Get Movie (D)etails, or (Q)uit: ").strip().lower()
    if command == "q":
        break
    elif command == "l":
        for movie in movie_list:
            movie.display()
    elif command == "d":
        movieName = input("Enter movie name: ")
        for movie in movie_list:
            if movie.isMatch(movieName):
                movie.display()
    else:
        print("Invalid Command")

print("Goodbye")


    


