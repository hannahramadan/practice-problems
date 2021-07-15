def pig_latin(phrase):
    """Turn a phrase into pig latin.
    """
    # declare the new string
    # declare vowels = 'aeiou'
    # loop through the string
    # look at the first character, 
        # if first character is in vowels:
            # remove first character + rest + "yay"
        #else:
            # remove first character + rest + "ay"
            
    new_string = []
    vowels = "aeiouAEIOU"
    words = phrase.split()
    
    for word in words:
        if word[0] in vowels:
            new_string.append(word[1:] + "yay")
        else:
            new_string.append(word[1:] + "ay")
    
    return " ".join(new_string)