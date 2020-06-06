import random
# user_input = "1,2,3,4,5,6"

# user_numbers = user_input.split(",")
# user_numbers

# user_numbers_as_int = []
# for number in user_numbers:
#     user_numbers_as_int.append(int(number))



'''
List comprehension approach
'''
# print([int(number) for number in user_numbers])

'''
Using sets
'''
# numbers = set()
# numbers.add(3)
# print(numbers)

# lottery_values = {3,5,17,6}
# print(lottery_values)

# user_values = {3,5,11,2}
# print(user_values)

# print(lottery_values.intersection(user_values))

def menu():
    # Ask player for numbers
    user_numbers = get_player_numbers()

    # Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()

    # Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched {} numbers and won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))

# User can pick 6 numbers
def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    # Create a set of intergers from this number_csv
    user_values = number_csv.split(",")
    integer_set = {int(number) for number in user_values}
    return integer_set

# Lotter calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values

# print(create_lottery_numbers())
menu()