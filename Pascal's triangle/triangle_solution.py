"""
Generate the first n rows of Pascal's Triangle.

Pascal's Triangle is a triangular array of numbers. Each number is the sum of the two directly above it.

Parameters:
n (int): The number of rows of Pascal's Triangle to generate.

Returns:
list of list of int: A list containing n lists, each representing a row of Pascal's Triangle.

Example:
If n == 3, the expected result is: 
[
    [1], 
    [1, 1], 
    [1, 2, 1]
].
"""
def generate_pascals_triangle(n):
    if n <= 0:
        return []

    pascals_triangle = [[1]]  # The first row

    for i in range(1, n):  # Generate rows 2 to n
        row = [1]  # First element of each row
        for j in range(1, i):  # Generate remaining elements of the row
            row.append(pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j])  # Each element is the sum of the previous row's corresponding elements
        row.append(1)  # Last element of each row
        pascals_triangle.append(row)

    return pascals_triangle