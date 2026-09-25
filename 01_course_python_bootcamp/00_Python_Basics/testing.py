print('Hello World!')

# arithmetic operators
print((66 + 33) + 81 % 2)

# variables
my_income = 500
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)

# strings
greet = "Hello world"
print(greet)

greet_len = len(greet)
print(greet_len)

# index
h = greet[0]
l = greet[-2]

# slicing
alphabet = 'abcdefghijklmno'
print(alphabet[2:]) # cdefghijklmno
print(alphabet[:3]) # abc
print(alphabet[1:3]) # bc

# jumping
print(alphabet[::3])
print(alphabet[::-1]) # reversing a string

# string methods
alphabet.lower()
alphabet.upper()
greet.split()

# formatting
result = 100/777
print("Result is: {r:1.3f}".format(r=result))
print(f"Result is: {result:1.3f}")

# lists & dicts & tuples & sets

# I/O
with open('textfile.txt', mode='r') as file:
    print(file.read())
    file.seek(0)