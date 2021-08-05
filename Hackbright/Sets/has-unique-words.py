def has_unique_chars(word):
    """Does word contains unique set of characters?"""
    
    if len(word) == len(set(word)):
        return True
    else:
        return False