# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
        pass #delete this line and replace with your code here

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        #Simple getter method... Don't directly access attributes outside a class
        return self.message_text
        
        
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        return self.valid_words.copy()
        

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Much improved cleaner version:
        
        
        #Constrain shift to [0,25]
        shift %= 26
#       
#       Initialize keys and values for lowercase dicitionary        
        lower_base = string.ascii_lowercase
        lower_shift = lower_base[shift:] + lower_base[:shift]
        
#       Initialize keys and values for uppercase dictionary 
        upper_base = string.ascii_uppercase
        upper_shift = upper_base[shift:] + upper_base[:shift]
#       
#       Combine the keys and values in each case, to create shift dictionary 
        lower_dict = dict(zip(lower_base, lower_shift))
        upper_dict = dict(zip(upper_base, upper_shift))
#       Combine lowercase and uppercase dictionaries to create full shift dictionary
        return {**lower_dict, **upper_dict}
        
        
#--------------OLD VERSION-------------
        
        
        
## Lowercase base dictionary. Maps 0:'a', 1:'b', 2:'c'...
#        lower_base_dict = {}
#        for i in range(26):
#            lower_base_dict[i] = string.ascii_lowercase[i]
#        
#        #Create dict that maps 'a':0+shift, 'b':1+shift...
#        lower_trans_dict = {}
#        for i in range(26):
#            lower_trans_dict[string.ascii_lowercase[i]] = i + shift
#            while lower_trans_dict[string.ascii_lowercase[i]] > 25:
#                lower_trans_dict[string.ascii_lowercase[i]] -= 26 
#              
##       Create dict that maps 'a':key of base dictioary for value of 'a' in transition dict
#        lower_shift_dict = {}
#        for i in range(26):
#            lower_shift_dict[string.ascii_lowercase[i]] = lower_base_dict.get(lower_trans_dict[string.ascii_lowercase[i]])
#            
### Uppercase dictionary
#        upper_base_dict = {}
#        for i in range(26):
#            upper_base_dict[i + 26] = string.ascii_uppercase[i]
#        
#        #Create dict that maps 'a':0+shift, 'b':1+shift...
#        upper_trans_dict = {}
#        for i in range(26):
#            upper_trans_dict[string.ascii_uppercase[i]] = (i+26) + shift
#            while upper_trans_dict[string.ascii_uppercase[i]] > 51:
#                upper_trans_dict[string.ascii_uppercase[i]] -= 26 
#              
##       Create dict that maps 'a':key of base dictioary for value of 'a' in transition dict
#        upper_shift_dict = {}
#        for i in range(26):
#            upper_shift_dict[string.ascii_uppercase[i]] = upper_base_dict.get(upper_trans_dict[string.ascii_uppercase[i]])
#
###Combine Dictionaries 
#        shift_dict = {}
#        shift_dict.update(lower_shift_dict)
#        shift_dict.update(upper_shift_dict)
#            
#        return shift_dict
        
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        #Much improved version...
    
        shift_dict = self.build_shift_dict(shift)
        #return a shifted version of original message
        return ''.join(shift_dict.get(char, char) for char in self.get_message_text())
        
    
        
#-----------------------------
#        
##       Create new empty string
#        encrypted_message = ''
#        
##       Get a shift dictionary to use for the shift
#        shift_dict = self.build_shift_dict(shift)
#        
#        for i in self.get_message_text():
#            if i in shift_dict:
#                encrypted_message = encrypted_message + shift_dict[i]
#            else:
#                encrypted_message = encrypted_message + i
#
#        return encrypted_message
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''       
        Message.__init__(self, text)
        self.shift = shift % 26
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        
        Returns: nothing
        '''
#       Update self.shift with new shift value
        self.shift = shift % 26

#       Update attributes determined by shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
#        Going to have to try 26 shifts and store the number of real words associated
#        with each decryption attemp and then return the one with the most efficacy:
#            
#        Need to construct decrypted message in way that I can loop over it with the is_word function
#        and count the number of valid words in the str. Will have to split the string at whitespace.
#        I can split at whitespace because the is_word function removes all punctuation.
#        
#       
#
#       Initialize way to track whether new trial is better
        max_count = 0                      
#       Initialize best decrypted message
        max_decrypted = self.get_message_text()  
#       Initialize tracker for the best shift value 
        max_shift = 0                            
#       Try each shift value in range(0,26) 
        for shift in range(0,26):
#           Initialize tracker for words decrypted with each shift iteration 
            count = 0  
#            Apply the shift value to message
            decrypted = self.apply_shift(shift)
#            Check every word in shifted message to find how many are valid words 
            for word in decrypted.split():
#                If word is valid:
                if is_word(self.get_valid_words(), word):
#                    Increment the count for this shift
                    count += 1
#           If the count for the shift value is higher than any previous count:
            if count > max_count:
#                Reassign the max count to current count
                max_count = count
#                Reassign decrypted message to current shifted decrypt attempt
                max_decrypted = decrypted
#                Reassign the max shift to current shift value
                max_shift = shift
                
 #      Return a tuple of best shift value (from pov of decrypter, not original encrypter), and decrypted message)
        return max_shift, max_decrypted
    

if __name__ == '__main__':

##    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
#
##    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    plaintext = PlaintextMessage('yoooooo, how are you?', 3)
    print('Expected Output: brrrrrr, krz duh brx?')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print(plaintext.get_message_text())
#
    ciphertext = CiphertextMessage('Brrrrrr, krz duh brx?')
    print('Expected Output: (23, Yoooooo, how are you?)')
    print('Actual Output:', ciphertext.decrypt_message())
    print(ciphertext.get_message_text())

    #TODO: best shift value and unencrypted story 
    
   
    
    #Best shift value = 12 (to reshift the encrypted message to it's original form)
    #Unencrypted story: Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.
#    
#    encrypted_story = CiphertextMessage(get_story_string())
#
#    print (encrypted_story.decrypt_message())
#    
    