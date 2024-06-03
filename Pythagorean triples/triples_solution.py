"""
Find all Pythagorean triples up to a given limit.

A Pythagorean triple is a set of three positive integers a, b, and c, such that a^2 + b^2 = c^2.

Parameters:
limit (int): The upper limit for the values of a, b, and c.

Returns:
list of tuple: A list of tuples, each containing a Pythagorean triple (a, b, c).

Ensure that a < b < c.

Ensure that the tuples are sorted ascended based on the first element, then the second element if the first elements are equal, 
and then the third element if the first two elements are equal.

Example:
If limit == 10, the expected result is [(3, 4, 5), (6, 8, 10)], since all the members of the tuples are under the limit and a^2 + b^2 = c^2.
The tuples are also sorted correctly and a < b < c.
"""
def find_pythagorean_triples(limit):
    triples = []

    for a in range(1, limit):  # Check all values a from 1 to limit
        for b in range(a, limit):  # For each value a, check values b from a to limit
            c = (a**2 + b**2) ** 0.5  # c = (a^2 + b^2)^0.5
            if c.is_integer() and c <= limit:  # If c is an integer and under the limit, we have a pythagorean triple
                triples.append((a, b, int(c)))

    return triples