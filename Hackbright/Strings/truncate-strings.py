def truncate(string):
    """Truncate repeating characters in a string."""

    new_s = ""
    
    if string:
        current = 0
        for i in range(len(string)):
            if string[i] != current:
                new_s = new_s + string[i]
            current = string[i]
    
    return new_s