def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    """
    if haystack == []:
        return None
        
    else:
        if haystack[-1] == needle:
            return len(haystack)-1
        else:
            haystack.pop()
            return recursive_index(needle, haystack)
    