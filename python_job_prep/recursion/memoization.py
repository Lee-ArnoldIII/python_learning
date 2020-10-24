factorial_memo = {}

def factorial(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)

    return factorial_memo[k]

print(factorial_memo)
print(factorial(4))
print(factorial_memo)

# Using a class to memoize:

class Memoize: 
    def __init__(self, f):
        self.f = f
        self.memo = {}
    
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def factorial2(k):

    if k < 2:
        return 1

    return k * factorial(k-1)

factorial2 = Memoize(factorial2)

print(factorial2(6))
print(factorial2(8))
print(factorial2(2))
print(factorial2(1))
print(factorial2.memo)