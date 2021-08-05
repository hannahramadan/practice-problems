def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
    
    lower = word.lower()
    
    for i in range(int(len(lower)/2)):
        if lower[i] != lower[-i - 1]:
            return False
        
    return True