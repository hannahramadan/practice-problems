def plusMinus(arr):
    """Given an array of integers, calculate the ratios of its elements that are positive, 
    negative, and zero. Print the decimal value of each fraction on a new line with 6
    places after the decimal."""
    
    positive = negative = neutral = 0
    
    for num in arr:
        if num > 0:
            positive += 1
        if num < 0:
            negative += 1
        if num == 0: 
            neutral += 1
            
    print(round(positive/len(arr),6))
    print(round(negative/len(arr),6))
    print(round(neutral/len(arr),6))