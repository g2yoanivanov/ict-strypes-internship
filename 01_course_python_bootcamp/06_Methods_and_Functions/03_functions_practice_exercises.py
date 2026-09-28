# Function Practice Exercises

# WARMUP SECTION
# Task 1
def lesser_of_two_evens(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x < y:
            return x
        else:
            return y
    else:
        if x > y:
            return x
        else:
            return y


# Task 2
def animal_crackers(word):
    split = word.split()

    if len(split) != 2:
        return '2-word string expected!'

    if split[0][0].lower() == split[1][0].lower():
        return True

    return False


# Task 3
def makes_twenty(x, y):
    if x + y == 20 or 20 in [x, y]:
        return True

    return False


# LEVEL 1 PROBLEMS
# Task 1
def old_macdonald(name):
    name_list = list(name)

    name_list[0] = name_list[0].upper()
    name_list[3] = name_list[3].upper()

    result = ''

    for x in name_list:
        result = result + x

    return result


# Task 2
def master_yoda(sentence):
    split = sentence.split()

    split.reverse()
    return " ".join(split)


# Task 3
def almost_there(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True

    return False


# LEVEL 2 PROBLEMS
# Task 1
def has_33(given_list):
    for i in range(0, len(given_list) - 1):
        if given_list[i] == 3 and given_list[i + 1] == 3:
            return True

    return False


# Task 2
def paper_doll(word):
    res = ''

    splitted = list(word)
    for i in range(0, len(splitted)):
        res = res + (splitted[i] * 3)

    return res


# Task 3
def blackjack(x, y, z):
    total = x + y + z

    if total > 21 and 11 in [x, y, z]:
        total = total - 10

    if total <= 21:
            return total

    else:
        return 'BUST'


# Task 4
def summer_69(nums):
    stopped = False
    res = 0

    for x in nums:
        if x == 6:
            stopped = True

        if x == 9:
            stopped = False
            continue

        if stopped:
            continue

        res = res + x

    return res


# CHALLENGING PROBLEMS
# Task 1
def spy_game(nums):
    first_0 = False
    second_0 = False
    first_7 = False

    for x in nums:
        if x == 0:
            first_0 = True

        if x == 0 and first_0:
            second_0 = True

        if x == 7 and first_0 and second_0:
            first_7 = True
            break

    return first_0 and second_0 and first_7


# Task 2
def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False

    return True

def count_primes(num):
    count = 0

    for x in range(2, num + 1):
        if is_prime(x):
            count += 1

    return count
