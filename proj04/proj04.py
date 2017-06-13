# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

palindrome = str(raw_input("Please enter a word: "))
lowercase = palindrome.lower()

remove_space = lowercase.translate(None, ' ')

# palindrome_list =[]
# for letter in palindrome:
#     palindrome_list.append(letter)
#
# print palindrome_list
#
#
# p_list = palindrome_list
# reverse = palindrome[:: -1]
# for letter in palindrome_list:
#     reverse.append(letter)
#     p_list = palindrome_list[-1:0]
#
# print p_list

# palindrome_reverse_list = reversed(palindrome_list)
# for letter in palindrome_list:
#     reverse = palindrome_reverse_list


if remove_space == remove_space[:: -1]:
    print (palindrome + " is a palindrome.")
else: print (palindrome + " is not a palindrome.")