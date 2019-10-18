# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:16:12 2019

@author: alexk
"""


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''    
    
    guessed_word = ("_ " * len(secret_word))
    updated_word = list(guessed_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            updated_word[i*2] = secret_word[i]
            updated_word[i*2+1] = ''
    return str(''.join(updated_word))            


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

def hangman(secret_word):
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
    print ('FYI, vowels cost 2 guesses and consonants cost 1 guess.')
    
  
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        print ('------------------------------')
    # Loop to continue playing game until run out of guesses or word is guessed
        print ('You have', guesses, 'guesses left.')
        print ('Available letters:', get_available_letters(letters_guessed))
        print ('Letters guessed:', letters_guessed) #troubleshooting 

        guess = input ('Please enter a guess: ') 
    
        if guess in alphabet:
            if guess in letters_guessed: # Repeated guess case
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
hangman(secret_word)
