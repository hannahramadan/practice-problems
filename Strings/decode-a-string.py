def decode(s):
    """Decode a string."""
    
    decoded_s = ""
        
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            skip = int(s[i]) + 1
            decoded_s = decoded_s + (s[i+skip])
        else:
            pass
        
    return decoded_s