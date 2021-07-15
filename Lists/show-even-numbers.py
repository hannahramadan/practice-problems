def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""
    
    evens =  []
    for index, num in enumerate(nums):
        if num % 2 == 0:
            evens.append(index)
    
    return evens