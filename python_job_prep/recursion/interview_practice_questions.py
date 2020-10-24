def reverse(s):
    
    if len(s) <= 1:
        return s

    else:
        return reverse(s[1:]) + s[0]



string = ['hello', 'hello world', '123456789', 'a']
for s in string:
    print(reverse(s))


