def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    s_nums = str(num)

    for i in range(len(s_nums)):
        print(int(s_nums[-i - 1]))

# Alternate solution:
def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    while num:
        next_digit = num % 10
        print(next_digit)
        num = (num - next_digit) // 10