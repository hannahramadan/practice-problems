def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"
    num_guesses = 0
    
    high_guess = 101
    low_guess = 1
    guess = None
    
    while guess != val:
        num_guesses += 1
        guess = (high_guess + low_guess)//2 
        if val > guess:
            low_guess = guess
        else:
            high_guess = guess
    
    return num_guesses 