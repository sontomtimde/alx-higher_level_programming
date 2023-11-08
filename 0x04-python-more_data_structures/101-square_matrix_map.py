#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not all(isinstance(row, list) and all(isinstance(i, (int, float)) for i in row) for row in matrix):
        print("Error: Invalid input. Please provide a matrix with numeric elements.")
        return None
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
