# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <William_I_sMeLl_ Luer>
# Collaborators : <Meg_Farts_a_LOT>
# Time spent    : <INFINITY... and beyond>

import math
import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
   '*':0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """


    word_length_coef = max(1, (7*len(word) - 3*(n - len(word))))
    letter_pts = sum (SCRABBLE_LETTER_VALUES.get(i, 0) for i in word.lower())
    
    return word_length_coef * letter_pts


# Make sure you understand how this function works and what it does!

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    hand_list = []
    hand_display = ''
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            hand_list.append(letter)

    return hand_display.join(hand_list)
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = 1
   
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    new_hand = copy.deepcopy(hand)
    
    for letter in word:
        if letter in new_hand and new_hand[letter] > 0:
            new_hand[letter] -= 1
    
    #Create new 
    cleaned_hand = copy.deepcopy(new_hand)
    
    for letter in new_hand:
        if cleaned_hand[letter] == 0:
            del cleaned_hand[letter]
    
    return cleaned_hand

    
    
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
   
    word = word.lower()
    hand_copy = copy.deepcopy(hand)
    
    # Returns False if the word is in word_list but not valid
    if word in word_list:
        counter = len(word)
        for letter in word:
            if letter in hand_copy and hand_copy[letter] > 0:
                hand_copy[letter] -= 1
                counter -= 1
                if counter == 0:
                    return True
            else:
                return False
    
# Returns True if valid word found from the wild possibilities
#... otherwise passes returns False if no valid word found
    elif '*' in word:
        for v in VOWELS:
            if word.replace('*', v) in word_list:
                counter = len(word)
                for letter in word:
                    if letter in hand_copy and hand_copy[letter] > 0:
                        hand_copy[letter] -= 1
                        counter -= 1
                        if counter == 0:
                            return True
                    else:
                        break
        return False
    
#Returns False in cases word isn't in word_list and does not contain an *
    else:
        return False
    
   
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    handlen = 0
    for letter in hand:
        handlen += hand[letter]
    
    return handlen

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # Keep track of the total score and round score
    round_score = 0 
    hand_copy = copy.deepcopy(hand)
    
    # As long as there are still letters left in the hand:
    while hand_copy != {}: 
        # Display the hand
        print ('Current hand:', display_hand(hand_copy))
        # Ask user for input
        word = input ('Please play a word or enter !! to end the round: ').lower()
        # If the input is two exclamation points:
        if word == '!!':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points):
        else: 
            # If the word is valid:
            if is_valid_word(word, hand_copy, word_list) == True:
                #Update update round score
                round_score += get_word_score(word, len(word))
                # Tell the user how many points the word earned,
                print ('Nice, that word is worth', get_word_score(word, len(word)), 'points' )
                # and the updated total score
                print ('Your score this round is now:', round_score, 'points')

            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print ('Smh... that is not a valid word')
            # update the user's hand by removing the letters of their inputted word
        hand_copy = update_hand(hand_copy, word)   

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print ('The hand is over. Your score this round is', round_score, 'points')
    # Return the total score as result of function
    return round_score



#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    
    #Create copy of hand 
    sub_hand = copy.deepcopy(hand)
    #Create string of all possible letters that can be substituted into hand
    possible_letters = string.ascii_lowercase
    #Remove letters from alphabet string that are already in hand
    for i in sub_hand:
        possible_letters.replace(i, "")
    #Find a random letter to add to hand
    x = random.choice(possible_letters)
    #Add random letter to hand same number of times that substituted letter in hand
    sub_hand[x] = (sub_hand[letter])
    #Remove the letter that is being substituted out
    del sub_hand[letter]
    #Return dictionary with updated hand
    return sub_hand      
  
              
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    # Introduce game
    print ("""
           Yo, welcome to the word game. It's like scrabble with no board. You get dealt 
           a hand in each round and are asked to play words or give up on the round. *'s 
           are vowel wild letters. Words are scored based on a combination of letter values 
           and word length. You also get one time chances to substitute a letter or replay 
           an entire round, but you cannot use a replay and then substitute in the same round. 
           Good luck.
           """)
    # Asks user to input a total number of hands to be played
    rounds_to_play = int (input ('How many rounds would you like to play? '))
    print ("Okay. Let's begin.")
#    Initialize hand counter, total score, substition & replay trackers
    rounds_played = 0
    total_score = 0
    substitute = 0
    replay = 0
    
    # Continue game while rounds played is less than rounds to be played
    while rounds_played != rounds_to_play:
        #Deal and display a new hand for the round
        hand = deal_hand(HAND_SIZE)
        #Display hand to user
        print ('Current hand: ', display_hand(hand))
        #If user hasn't used their substitution
        if substitute == 0:
            subbing = input ('Would you like to use your substitution this round? Enter yes or no. ').lower()
            if subbing == 'yes':
                substitute = 1
                subbed_letter = input ('Which letter would you like to substitute? ')
                subbed_hand = substitute_hand(hand, subbed_letter)
                print ('Here\'s your new hand:', display_hand(subbed_hand)) #this line may be unnecc
                round_score = play_hand(subbed_hand, word_list)
                
                
                #Replay option block
                if replay == 0:
                    replay_round = input ('Would you like to use your replay this round? Enter yes or no. ').lower()
                    #User chooses to replay round
                    if replay_round == 'yes':
                        #Update replay counter to prevent block from running again
                        replay = 1
                        #replay hand and get new potential score
                        replay_score = play_hand(subbed_hand, word_list)
                        #Adjust total score based on highest of the two scores
                        total_score += max(round_score, replay_score)
                        #Update number of rounds played
                        rounds_played += 1
                    #User chooses not to replay round
                    else:
                        #Update total score based on round score
                        total_score += round_score
                        #Update number of rounds played
                        rounds_played += 1
                
            #User chooses not to use their substitution...
            else: 
                round_score = play_hand(hand, word_list)
                #Replay option block
                if replay == 0:
                    replay_round = input ('Would you like to use your replay this round? Enter yes or no. ').lower()
                    #User chooses to replay round
                    if replay_round == 'yes':
                        #Update replay counter to prevent block from running again
                        replay = 1
                        #replay hand and get new potential score
                        replay_score = play_hand(hand, word_list)
                        #Adjust total score based on highest of the two scores
                        total_score += max(round_score, replay_score)
                        #Update number of rounds played
                        rounds_played += 1
                    #User chooses not to replay round
                    else:
                        #Update total score based on round score
                        total_score += round_score
                        #Update number of rounds played
                        rounds_played += 1
               
                    
        #User has used substition already        
        else:
            #Play hand and get round score
            round_score = play_hand(hand, word_list)
            #Replay option block
            if replay == 0:
                    replay_round = input ('Would you like to use your replay this round? Enter yes or no. ').lower()
                    #User chooses to replay round
                    if replay_round == 'yes':
                        #Update replay counter to prevent block from running again
                        replay = 1
                        #replay hand and get new potential score
                        replay_score = play_hand(hand, word_list)
                        #Adjust total score based on highest of the two scores
                        total_score += max(round_score, replay_score)
                        #Update number of rounds played
                        rounds_played += 1
                    #User chooses not to replay round
                    else:
                        #Update total score based on round score
                        total_score += round_score
                        #Update number of rounds played
                        rounds_played += 1
            #Provide user their total score            
            print ('Your total score is now', total_score, 'points.')
            #Increment number of rounds played
            rounds_played += 1
            #Provide user how many rounds are left
            print ('There are', (rounds_to_play - rounds_played), 'rounds left.')
            
    print ('The game is over. Your total score over', rounds_to_play, 'rounds is:', total_score, 'points.'
           
           ' GG.')
#    
#    1. Ask the user if they want to substitute any of the letters in their hand (can only be done once per game)
#        a) If yes, then prompt them for the letter they want to sub out
#        b) Give them updated hand
#    2. Play hand
#    3. Ask user if they would like to replay the hand and keep better of 2 the scores (once/game)
#        a) If yes, replay hand
#    4) Returns total score for series of hands
#    
#    This isn't the cleanest way by far. I should have split the code immediately along sub/replay dimensions and handled 
#    the really smooth cases
    # Should have thought more about the POTENTIAL PATHWAYS AND PROBLEM STRUCTURE.
    
    
    
    
    
    
    
    
    
    
    
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
