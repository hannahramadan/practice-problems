def is_prime(num):
    """Is num a prime number?"""

    assert num >= 0, "Num should be a positive integer!"

    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    n = 3
    while n * n <= num:
        if num % n == 0:
            return False
        n += 2

    return True

def primes(count):
"""Return count number of prime numbers, starting at 2."""

    primes = []
    num = 2
    while count > 0:

        if is_prime(num):
            primes.append(num)
            count -= 1

        num += 1

    return primes