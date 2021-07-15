def fit_to_width(string, max_length):
    
    character_count = 0
    fitted_string = ""
    
    words = string.split(" ")

    for word in words:
        for character in word:
            character_count += 1
        if character_count <= max_length and len(word):
            fitted_string = fitted_string + word + " "
        else:
            fitted_string = fitted_string + "\n" + word + " "
            character_count = 0
        
    return fitted_string