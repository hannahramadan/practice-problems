def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # palidrones are made up of even sets of numbers, plus a potential single odd number. 
    # this algo uses a dictionary to keep track of the times each letter shows up. If more than 1 letter
    # shows up an odd number of times, it can't be a palindrome. 

    d = {}
    
    for char in word:
        d[char] = d.get(char, 0) + 1
    
    odds = 0
    
    for value in d.values():
        if value % 2 == 1:
            odds += 1
        if odds >= 2:
            return False
    
    return True