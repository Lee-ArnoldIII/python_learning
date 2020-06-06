import random
'''
creating a method to ask user to give a number
'''
def ask_user_and_check_number():
    user_number = int(input('Enter a number betwen 0 and 9: '))

    if user_number not in magic_numbers:
        return 'You got it wrong!'

    if user_number in magic_numbers:
        return 'You got it right!'

magic_numbers = [random.randint(0,9), random.randint(0,9)]

'''
start with request for how many chances the user will get to find the correct answer
'''
user_attempts = int(input('How many chances do you think you need to guess the number? '))

def run_program_x_times(chances):
    
    for attempt in range(chances):
        print('This is attempt {}'.format(attempt))
        print(ask_user_and_check_number())
        
run_program_x_times(user_attempts)

minimum = 100
for index in range(10):
    random_num = random.randint(0,100)
    print(f'The number generated is {random_num}.')
    if random_num < minimum: 
        minimum = random_num
print(f'The minimum number is {minimum}.')