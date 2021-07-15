def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    
    lsentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = set()
    
    for char in lsentence:
        if char in alphabet:
            letters.add(char)
    
    if len(letters) == 26:
        return True
    else:
        return False