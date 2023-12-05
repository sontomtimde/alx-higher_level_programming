#!/usr/bin/python3
"""Defining Pascal's Triangle function."""


def generate_pascal_triangle(n):
    """
    Generate Pascal's Triangle of size n.

    Args:
    n (int): Size of the Pascal's Triangle to generate.

    Returns:
    list: Pascal's Triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = triangle[-1]
        next_row = [1]
        for i in range(len(row) - 1):
            next_row.append(row[i] + row[i + 1])
        next_row.append(1)
        triangle.append(next_row)
    return triangle

# Example usage:
if __name__ == "__main__":
    size = 5
    pascal_triangle = generate_pascal_triangle(size)
    for row in pascal_triangle:
        print(row)
