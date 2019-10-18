# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    #Recursive base case
    if len(sequence) <= 1: return sequence 
    else:
        #Empty list to hold permutations
        permutations = []
        #Looping over each element resulting from the Recursive call on sequence minus last char
        for e in get_permutations(sequence[:-1]):
            #Loop through range of new permuations and creat all the NEW permutations, since a new 
            #permutations has the new letter in EVERY position
            for i in range(len(e)+1):
                #New permutations are strs with last char in sequence placed in every position 
                new_perm = e[:i] + sequence[-1] + e[i:]
                #If newly created perm not in permutations list, then add it to list
                if new_perm not in permutations: 
                    permutations.append(new_perm)
    #Return list of all permutations of given sequence
    return permutations

p = 'abc'

print (get_permutations(p))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

