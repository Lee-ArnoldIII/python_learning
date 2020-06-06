numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)

print(numbers[0])

'''
Loops
'''
for number in numbers:
    print(number)

for number in numbers:
    print(number**2)

'''
boolean & If statements
'''
for number in numbers:
    print(number > 5)

if 5 > 3:
    print('Five is greater than three!')

for number in numbers:
    if number > 5:
        print(number)

'''
Using in and not
'''
print(10 in numbers)

print(10 not in numbers)

if not 3 > 5:
    print('This is weird')

