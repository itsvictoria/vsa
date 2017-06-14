

# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

print 'Welcome to the game of Hangman!'
print ' '

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def hangman():
    word = choose_word(wordlist)
    #print word , 'is the word'
    return word

word = hangman()

word_length = len(word)
print "The word is" , word_length , "letters long."

guesses=int(6)

list = ["_ "] * word_length
print list


while guesses>0:
    print 'Your available letters: ' , alphabet
    lettr = raw_input("Enter a letter: ")
    print ' '

    lettr = lettr.lower()

    wordlst = []
    for letter in word:
        wordlst.append(letter)
    #print wordlst

    for letter in lettr:
        if letter in wordlst:
                for num in range(len(list)):
                    if lettr == wordlst[num]:
                        list[num] = lettr
                print list

                alphabet = alphabet.replace(lettr, "/")
                print "You got a letter right!"
        else:
            print "Nope, try again!"
            alphabet = alphabet.replace(lettr, "/")
            guesses = guesses - 1
            print "You have", guesses, "guesses left."
    if list == wordlst:
        print "Yay, you win!"
        break

if guesses == 0:
    print 'You lose! The word was' , word

