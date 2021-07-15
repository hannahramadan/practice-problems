#nested for loop, quadratic O(n^2)
def does_add_up(lst, target_num):
    """# Given a list of integers, find a matching pair (2 nums) that added up, equal to a given sum.
    Can assume the list items are always intergers, and negative integers can occur.
    
    [1,2,3,9], 8 => False
    [0,0,0,0,0,1,1,2,4,4,6,8,9], 5 => True

    """
    for i in range(0,len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target_num:
                return True
    return False

# check for complement, quadratic O(n^2)
def does_add_up(lst, target_num):
    
    for num in lst: # O(n)
        if target_num - num in lst: # O(n)
            return True
    return False

# High & Low comparison. Linear O(n)
def does_add_up(lst, target_num):

    low = 0
    high = len(lst) -1
    
    while lst:
        if low == high or lst[high] < target_num/2 or lst[low] > target_num/2:
            return False
        if lst[low] + lst[high] < target_num:
            low += 1
        if lst[low] + lst[high] > target_num:
            high -= 1
        if lst[low] + lst[high] == target_num:
            return True
     
    return False 














