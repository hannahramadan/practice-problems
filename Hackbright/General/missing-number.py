def missing_number(lst, max_num):
        """Given a list of numbers 1...max_num, find which one is missing."""

    lst.append(max_num + 1)
    lst.sort()
    current = 1
    
    for item in lst:
        if item == current:
            current += 1
        else:
            return current

    raise Exception("None are missing!")