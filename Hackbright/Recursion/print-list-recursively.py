def print_recursively(lst):
    """Print items in the list, using recursion."""
    if len(lst) == 0:
        return
    
    else:
        print(lst[0])
        print_recursively(lst[1:])
        

#Alternate solution passing a second paramter
def print_recursively(lst, index = 0):
    """Print items in the list, using recursion."""
    
    if len(lst) == 0:
        return
    
    if len(lst) == index:
        return 
    
    else:
        print(lst[index])
        print_recursively(lst, index + 1)