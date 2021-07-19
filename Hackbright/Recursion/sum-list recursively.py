def sum_list(nums):
    """Using recursion, return the sum of numbers in a list."""
    
    if len(nums)==0:
        return 0
        
    return nums[-1] + sum_list(nums[0:-1])