def divide_secure(number, divisor):
    assert divisor != 0, "Divided a number by a zero!"
    return number / divisor


print(divide_secure(12,12))