#If we didn't care about maintaing order:

def deduped(items):
    """Return new list from items with duplicates removed."""
    
    return list(set(items))

#If we do care about maintaing order:

def deduped(items):
    
    seen = set()
    result = []
    
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result