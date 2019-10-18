# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:01:07 2019

@author: alexk
"""


import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    '''
    total = len(secret_word) 
    counter = 0
    for i in secret_word:
        if i in letters_guessed:
             counter += 1
        else:
            break
    if counter == total:
        return True
    else:
        return False        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    '''    
    guessed_word = ''
    for char in secret_word:
        if char not in letters_guessed:
            guessed_word += '_ '
        else: 
            guessed_word += char
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
    '''
    
    available_letters = string.ascii_lowercase
    for i in letters_guessed:
        available_letters = available_letters.replace(i,'')
    return available_letters

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
    corresponding letters of other_word, or the letter is the special symbol
    _ , and my_word and other_word are of the same length;
    False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else: 
        for i in range(len(my_word)):
            if my_word[i] != '_' and my_word[i] != other_word[i]:
                return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    '''
    possible_words = []
    for i in wordlist:
        if match_with_gaps(my_word, i) == True:
            possible_words.append(i)
    print ('Possible matches are: ', possible_words)
    
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    '''
    guesses = 6
    warnings = 3
    letters_guessed = []
    alphabet = string.ascii_letters
    vowels = 'aeiou'
    
    print ('Welcome to the game Hangman. Goodluck!')                            
    print ('I"m thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print ('FYI: Vowels cost 2 guesses, consonants cost 1 guess, and guess * for a hint.')
    
  
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print ('------------------------------')
    # Loop to continue playing game until run out of guesses or word is guessed
        print ('You have', guesses, 'guesses left.')
        print ('Available letters:', get_available_letters(letters_guessed))
        print ('Letters guessed:', letters_guessed) #troubleshooting 

        guess = input ('Please enter a guess: ') 

        
        if guess == '*':   # Asking for hint case
            show_possible_matches(get_guessed_word(secret_word, letters_guessed).replace(' ',''))
        
        elif guess in alphabet:
            if guess in letters_guessed: # Repeated letter guess case
                if warnings > 0:
                    warnings -= 1
                    print('Warning! You already guessed that letter. You have', warnings, 'warnings left:', 
                          get_guessed_word(secret_word, letters_guessed))
                else: #No warnings left
                    print('Yikes. You already guessed that letter and you have no warnings left '
                        'so you lose a turn:', get_guessed_word(secret_word, letters_guessed))
                    guesses -= 1
            else:    # Valid and unique guess case
                letters_guessed += guess.lower()            
                if guess in secret_word:   #Correct guess case
                    print ('Good guess:', get_guessed_word(secret_word, letters_guessed))
                else: # Valid unique incorrect guess case
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                    if guess in vowels:
                        guesses -= 2
                    else:
                        guesses -= 1
            
        else:
            if warnings > 0:
                warnings -= 1
                print('Warning! That is not a valid guess. You have', warnings, 'warnings left:', 
                     get_guessed_word(secret_word, letters_guessed))
            else: #No warnings left
                print ('Yikes! That is not a valid guess and you have no warnings left so you '
                        'lose a turn:', get_guessed_word(secret_word, letters_guessed))
                guesses -= 1
                
    if guesses > 0:
        print ('GG, you won!')
        print ('You total score for this game is:', (guesses * int(len(secret_word))))
    
    else:
        print ('You lose... the word was ' + secret_word +'.')

    
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)