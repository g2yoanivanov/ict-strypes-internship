# Errors and Exceptions Homework Tasks

# Task 1
def task1():
    try:
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except TypeError:
        print('Error: There is an element in the list that is not a number')


# Task 2
def task2():
    x = 5
    y = 0

    try:
        z = x // y
        print(z)

    except ZeroDivisionError:
        print('Cannot divide by zero')

    finally:
        print('All done')


# Task 3
def ask():
    while True:
        try:
            n = int(input('Choose a number: '))

        except ValueError:
            print('Error: The input was not a number')
            continue

        else:
            print('Thank you! Your number is {}'.format(n))
            break
