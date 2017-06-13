# Name:
# Date:

# proj05: functions and lists

# Part I

def divisors(num):
    """
    Takes a number and returns all divisors of the number, ordered least to greatest
    :param num: int
    :return: list (int)
    """
    ans_list = []
    for n in range (1, num+1):      #n - number that could divide the parameter num
        print "num =", num, "n =", n
        if num % n == 0:    #checking to see if n divides into num
            print "is divisor"
            ans_list.append(n)  # n goes into num, then add n to ans_list

    return ans_list

def prime(num):
    """
    Takes a number and returns True if the number is prime, otherwise False
    :param num: int
    :return: bool
    """

    prime_list = []
    for n in range (1, num+1):
        if num % n == 0:    #if one of those numbers is a divisor

            prime_list.append(n)
            # print "length of prime list is ",
            len(prime_list)
    length = len(prime_list)
    if length == 2:
        return True
    else:
        return False

    # return False

# Part II

def intersection(lst1, lst2):
    """
    Takes two lists and returns a list of the elements in common between the lists
    :param lst1: list, any type
    :param lst2: list, any type
    :return: list, any type
    """
for 
# Part III

def find_ab(side1, side2, side3):
    """
    Takes three side lengths an returns two smallest in a list
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: list of 2 ints or floats
    """

    if side3 > side1 and side3 > side2:
        return [side1, side2]
    if side1 > side2 and side1 > side3:
        return [side2, side3]
    if side2 > side1 and side2 > side3:
        return [side1, side3]

def find_c(side1, side2, side3):
    """
    Takes three side lengths an returns the largest
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: int or float
    """
    if side3 > side1 and side3 > side2:
        return side3
    if side1 > side2 and side1 > side3:
        return side1
    if side2 > side1 and side2 > side3:
        return side2

def square(side):
    """
    Takes a side length and returns the side length squared
    :param side: int or float
    :return: int or float
    """
    return side **2

def pythagorean(a,b,c):
    """
    Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: bool
    """
    if square(a) + square(b) == square(c):
        return True
    else:
        return False

def is_right(side1, side2, side3):
    """
    Takes three side lengths and returns true if triangle is right
    :param side1: int or float
    :param side2: int or float
    :param side3: int or float
    :return: bool
    """
    small_list = find_ab(side1, side2, side3)
    a = small_list[0]
    b= small_list [1]
    c=find_c(side3, side2, side1)
    ans = pythagorean(a,b,c)
    return ans

# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
