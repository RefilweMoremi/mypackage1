def sum_array(array):
    '''Return sum of all items in array'''

    for i in array:
        Sum = sum(array)

    return Sum


#fibonacci sequence function
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#factorial function
def factorial(n):
    '''Return n!'''

    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num



    #Function to return a word in reverse
def reverse(word):
    '''Return word in reverse'''

    return word[::-1]
