# Author: Alexandra Wheeler
# Movie List

from turtle import title
from movie import Movie

movie_list = {
    Movie("Avengers","A 2012 American superhero film based on the Marvel Comics superhero team of the same name.","Robert Downey Jr.", "Adventure", "8.1"),
    Movie("Captain America", "World War II hero Steve Rogers fights for American ideals as one of the world's mightiest heroes", "Chris Evans", "Action", "6.9"),
    Movie("Spiderman: Homecoming", "Under the watchful eye of mentor Tony Stark, Parker starts to embrace his newfound identity as Spider-Man.", "Tom Holland", "Action", "7.4"),
    Movie("Black Panther", "T'Challa returns home to the African nation of Wakanda to take his rightful place as king", "Chadwick Boseman", "Action", "7.3" )
}

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


    


