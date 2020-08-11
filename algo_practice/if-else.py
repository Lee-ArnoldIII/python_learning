def avg(*args):
    inputs = [*args]
    length = len(inputs)
    total = sum(inputs)/ length
    return float(total)



print(avg(1,2,3))
