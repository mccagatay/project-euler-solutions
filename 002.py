"""
Problem:
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million
find the sum of the even-valued terms.
"""


def fibonacci(limit):
    term_1 = 1
    term_2 = 2
    total_even_number = 0

    while term_1 < limit or term_2 < limit:
        if term_1 % 2 == 0:
            total_even_number += term_1
        if term_2 % 2 == 0:
            total_even_number += term_2
        term_1 = term_1 + term_2
        term_2 = term_1 + term_2

    return total_even_number


print(fibonacci(4000000))
