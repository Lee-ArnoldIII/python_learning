from user import User
from database import Database

Database.initialise(database='learning', user='postgres', password='Outsmart1!@', host='localhost')

user = User('j.cole@rap.com', 'J', 'Cole', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('123@123.com')

print(user_from_db)