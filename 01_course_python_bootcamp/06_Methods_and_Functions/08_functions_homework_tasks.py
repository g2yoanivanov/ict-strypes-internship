import math
import string

# Functions and Methods Homework

# Task 1
def vol(rad):
    return (4 / 3.0) * math.pi * (rad ** 3)


# Task 2
def ran_check(num, low, high):
    return num >= low and num <= high

# Task 3
def up_low(s):
    sample = s
    s.strip()
    chars = list(s)

    ups = 0
    lows = 0

    for x in chars:
        if x.isupper():
            ups = ups + 1

        elif x.islower():
            lows = lows + 1

    print('Sample string: {0}'.format(sample))
    print('No of Upper case chars: {0}'.format(ups))
    print('No of Lower case chars: {0}'.format(lows))    


# Task 4
def unique_list(lst):
    return list(set(lst))

def unique_list2(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)

    return res


# Task 5
def multiply(nums):
    res = 1

    for x in nums:
        res = res * x

    return res


# Task 6
def is_palindrome(s):
    original = s
    original.strip()

    strip = s.strip()
    reversed = strip[::-1]

    return original == reversed


# Task 7
def is_pangram(s, alphabet=string.ascii_lowercase):
    new = s.lower()
    new = new.strip()

    if len(new) < 26:
        return False

    split = list(s)

    for x in split:
        new = new.replace(x, "")

    if len(new) != 0:
        return False

    return True

print(is_pangram('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'))
print(is_pangram('abcdefghijklmnopqrstuvwxy'))
