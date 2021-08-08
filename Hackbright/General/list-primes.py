def list_primes(num):
    """Return list of all primes from 0 to num"""
    
    if num < 2:
        return []

    #2 is a prime number. Since later we are dividing by 2 to get rid of all even numbers,
    # it's worth getting rid of 2 upfront as a prime number so that we don't have to 
    # worry about it. 
    #  
    primes = [2]
    
    for i in range(3,num+1,2):
        prime = True
        for j in primes:
            # Since all non-prime numbers can be factored into prime numners, if a number
            # is prime, we know it can't be factored. AND since we won't find a multiple 
            # great than the sq root, we only are checking prime numbers up to the sq root 
            # of the given number. 
            if j > i ** 0.5:
                break
            if i % j == 0:
                prime = False 
        if prime == True:
            primes.append(i)
    
    return primes
