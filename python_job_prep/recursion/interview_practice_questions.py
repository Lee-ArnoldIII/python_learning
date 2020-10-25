# This interview question requires you to reverse a string using recursion. 
# Make sure to think of the base case here.

# Again, make sure you use recursion to accomplish this.
# Do not slice (e.g. string[::-1]) or use iteration, there must be 
# a recursive call for the function.

def reverse(s):
    
    if len(s) <= 1:
        return s

    else:
        return reverse(s[1:]) + s[0]



string = ['hello', 'hello world', '123456789', 'a']
for s in string:
    print(reverse(s))

#########################################################################################
# Given a string, write a function that uses recursion to output a 
# list of all the possible permutations of that string.

# For example, given s='abc' the function 
# should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def permute(s):

    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else: 
        # for every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3
            for perm in permute( s[:i] + s[i+1:]):
                # Add it to the output
                out += [let+perm]
    
    return out
    

print(permute('abc'))

#########################################################################################
# In this interview excercise we will begin to get a 
# feel of having to solve a single problem multiple ways!

# Implement a Fibonnaci Sequence in three different ways:
    ## Recursively
    ## Dynamically (Using Memoization to store results)
    ## Iteratively

# Your function will accept a number n and return the nth number of the fibonacci sequence
    ## Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts 
    ## off with a base case checking to see if n = 0 or 1, then it returns 1.
    ## Else it returns fib(n-1)+fib(n+2).

### Recursively
def fib_rec(n):

    # Base case
    if n == 0 or n == 1: 
        return 1

    else:
        return n + fib_rec(n-1)

print(fib_rec(10))
print(fib_rec(3))

### Dynamically
    ## Implement the function using dynamic 
    ## programming by using a cache to store results (memoization).
print('  ')
print('Memoized version')

class Memoize:
    def __init__(self, t):
        self.t = t
        self.memo = {}

    def __call__(self, args):
        if not args in self.memo:
            self.memo[args] = self.t(*args)
        return self.memo[args]

def fib_memo(n):
    
    # Base case
    if n == 0 or n == 1:
        return 1

    return n + fib_memo(n)

fib_memo = Memoize(fib_memo)

print(fib_memo(10))