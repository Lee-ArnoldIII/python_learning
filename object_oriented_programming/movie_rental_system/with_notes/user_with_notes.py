from movie import Movie

class User:
    def __init__(self, name):
       self.name = name
       self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # The code below is using filter with a lambda function (think annoymous function like in JS)
        # that simplifies the code below to a single line 
        return list(filter(lambda x: x.watched, self.movies))     

        # The code below is the traditional/initial way learned to execute the watched_movies function
        # user_watched = []

        # for movie in self.movies:
        #     if movie.watched:
        #         user_watched.append(movie)

        # return user_watched
    
    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    def json(self):
        return{
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user
    '''
    CSV saving is considered outdated and is replaced by saving to JSON object. Code below
    is kept to show how to create the method if it was required for different projects later.
    '''        
    # def save_to_file(self):
    #     with open(f"{self.name}.txt", 'w') as f:
    #         f.write(self.name + "\n")
    #         for movie in self.movies:
    #             f.write(f"{movie.name},{movie.genre},{str(movie.watched)}\n")
    '''
    below is a class method that allows for class to be used and creates better functionality (look this up later)
    '''

    # @classmethod
    # def load_from_file(cls, filename):
    #     with open(filename, 'r') as f:
    #         content = f.readlines()
    #         username = content[0]
    #         movies = []
    #         for line in content[1:]:
    #             movie_data = line.split(",")
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
            
    #         user = cls(username)
    #         user.movies = movies
    #         return user
