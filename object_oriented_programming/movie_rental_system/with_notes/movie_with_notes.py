class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

# You can use __str__ for more informal string creation...the __repr__ is used to find the "offical"
# string representation of an object
    def __repr__(self):
        return "{} is a {} movie".format(self.name, self.genre)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    '''
    Code below is initial method for pulling from json. 
    '''
    # @classmethod
    # def from_json(cls, json_data):
    #     return Movie(json_data['name'], json_data['genre'], json_data['watched'])

    '''
    Code below is using setting up discussion about argument unpacking
    '''
    # if you have a named parameter, the ones following it must be named as well
    # @classmethod
    # def from_json(cls, json_data):
    #     return Movie(genre=json_data['genre'], watched=json_data['watched'], name=json_data['name'])
    '''
    Continuation of argument unpacking
    '''
    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data)