
# Task 1
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
words = st.split()

for word in words:
    if word[0] == 's':
        print(word)

# Task 2
# Use range() to print all the even numbers from 0 to 10.
print(list(range(0, 11, 2)))

# Task 3
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
result = [x for x in range(1, 51) if x % 3 == 0]
print(result)

# Task 4
# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
words = st.split()

for word in words:
    if len(word) % 2 == 0:
        print(f'even!: {word}')

# Task 5
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" 
# instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz".
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

# Task 6
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
words = st.split()

result = [x[0] for x in words]
print(result)