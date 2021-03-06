


def sum_array(array):
    if len(array)==0:
        return 0
    elif len(array)==1:
        return sum(array)
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''Return n!'''
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def reverse(word):
    if len(word) == 1:
        return word
    else:
        return reverse(word[1:]) + word[0]
    '''Return word in reverse'''
