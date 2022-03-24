def getMovies():
    movies = []
    try:
        with open("examples/march24/movies.txt") as file:
            for line in file:
                movies.append(line.strip())
    except FileNotFoundError:
        print("Sorry your movies could not be loaded.")
    return movies

myMovies = getMovies()
for movie in myMovies:
    print(movie)