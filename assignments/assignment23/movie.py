# Author: Alexandra Wheeler
# Movie List

class Movie:
    def __init__(self,title,description,actors,genre,rating):
        self.title = title
        self.description = description
        self.actors = actors
        self.genre = genre
        self.rating = rating

    def display(self):
            print(f"""
                *** {self.title} ***
                {self.description}
                Stars:
                -{self.actors}
                Genre: {self.genre}
                Rating: {self.rating} stars
            """)
        
    def isMatch(self,title):
            if title == self.title:
                return True
            else:
                return False
