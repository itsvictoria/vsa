# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your first name: ")
name_inital = name[:1]
inital_capital = name_inital.upper()
name_rest = name[1:]
rest_lowercase = name_rest.lower()

age = raw_input("Enter your age: ")
if int(age) > 100:
    print("Congratulations on already celebrating your 100th birthday!")
else:
    birthday = raw_input ("Have you had a birthday this year (yes or no)?: ")
if birthday == "yes":
    one_hundred = 2017
    n = 0
    while n < (100 - int(age)):
        one_hundred = one_hundred + 1
        n = n + 1
  # one_hundred = 100 - int(age) + 2017
    print inital_capital + rest_lowercase + " will turn 100 in the year ",
    print(one_hundred)
else:
  # one_hundred = 100 - int(age) + 2016
  # print inital_capital + rest_lowercase + " will turn 100 in the year ",
    one_hundred = 2016
    n = 0
    while n < (100 - int(age)):
      one_hundred = one_hundred + 1
      n = n + 1

if 17 > int(age) > 13:
    print("You can watch PG-13 rated movies!")
else:
    print("You can watch G and PG rated movies!")
if int(age) > 17:
    print("You can watch R rated movies!")

    print inital_capital + rest_lowercase + " will turn 100 in the year ",
    print(one_hundred)
