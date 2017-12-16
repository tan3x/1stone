#hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()

    # wordlist: list of strings
    wordlist = line.split()
    print(str(len(wordlist))+" words loaded.")

    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for e in secretWord:
        if e not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res = ''
    for e in secretWord:
        if e in lettersGuessed:
            res = res +e
        else:
            res = res +'_'
    return res




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for ch in lettersGuessed:
        alphabet.remove(ch)

    available_letters = ' '.join(alphabet)

    return ' '.join(alphabet)

def welcome(secretWord):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %s letters long' % str(len(secretWord)))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    mistakes = 0
    welcome(secretWord)
    used_letters = []

    while mistakes <= 8:
        print('------------------')
        if getGuessedWord(secret,used_letters) == secretWord:
            print('Congradulations! You won')
            break

        if mistakes == 8:
            print('Sorry, you ran out of guesses. The word was %s.' % secret)
            break

        print('You have %i guesses left' % (8-mistakes))
        print('Available Letters: %s' % getAvailableLetters(used_letters))
        guess = (raw_input('Please guess a letter: ')).lower()
        used_letters.append(guess)


        used_letter_list = ''.join(used_letters)

        if guess in secretWord:
            print('Good guess: '+ getGuessedWord(secretWord,used_letters) )

        elif guess not in secretWord:
            print('Oops! That letter is not in my word:' + getGuessedWord(secretWord,used_letters))
            mistakes += 1

        elif guess in used_letters:
            print('Oops! You have already guessed that letter:' + getGuessedWord(secretWord,used_letters))


secret = 'araba'
hangman(secret)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
