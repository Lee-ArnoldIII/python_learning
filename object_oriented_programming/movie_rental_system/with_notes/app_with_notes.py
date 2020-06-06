from user import User
import json
import os

# user = User('Lee')

'''
code below uses add_movie method found in user.py
'''
# my_movie = Movie("The Matrix", "Sci-Fi", True)

# user.movies.append(my_movie)


# print(user.watched_movies())
# user.add_movie('The Cannonball Run', 'Comedy')
# print(user.movies)

'''
Code below is setting up to save to csv
'''
# user.add_movie('The Matrix', 'Sci-Fi')
# user.add_movie('The Interview', 'Comedy')

# user.save_to_file()

'''
Code below is testing open from file method in user.py
'''
# user = User.load_from_file('Lee.txt')

# print(user.name)
# print(user.movies)
'''
Code below shows how to save a json to a file. Code was commented out to show how to load from a JSON file.
'''
# user = User('Lee')

# user.add_movie("The Matrix", "Sci-Fi")
# user.add_movie("The Interview", "Comedy")

# with open('my_file.txt', 'w') as f:
#     json.dump(user.json(), f)
'''
Code below is loading from a JSON file
'''
# with open('my_file.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())
 

def menu():
    # Ask for the user's name.
    name = input('Please enter your name: ')
    filename = f"{name}.txt"
    # Check if a file exists for that user.
    if file_exists(filename):
       # If it already exists, welcome them and load their data. 
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
        # If not, create a User object
    else:
        user = User(name)

    # Give them a list of options:
    #     Add a movie 
    #     See list of movies
    #         Set a movie as watched
    #         Delete a movie by name 
    #     See list of watched movies
    #     Save and Quit 
    selection = input("Enter 'a' to add a movie, 's' to see the list of movies," 
                      "'w' to set a movie as watched," 
                      "'d' to delete a movie, 'l' to see the list of watched movies,"
                      "'f' to save or 'q' to quit: ")    
    while selection != 'q':

        if selection == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter movie genre: ")
            user.add_movie(movie_name, movie_genre)

        elif selection == 's':
            for movie in user.movies:
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")

        elif selection == 'w':
            movie_name = input("Enter the movie to set as watched: ")
            user.set_watched(movie_name) 

        elif selection == 'd':
            movie_name = input("Enter the movie you want to delete: ")
            user.delete_movie(movie_name)

        elif selection == 'l':
            for movie in user.watched_movies():
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")

        elif selection == 'f':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        selection = input("Enter 'a' to add a movie, 's' to see the list of movies," 
                      "'w' to set a movie as watched," 
                      "'d' to delete a movie, 'l' to see the list of watched movies,"
                      "'f' to save or 'q' to quit: ")

def file_exists(filename):
    return os.path.isfile(filename)

menu()