def reverse_kth_rows(matrix, k):
    """
    Reverse every k-th row in the matrix.

    Args:
        matrix (list of lists): Input matrix.
        k (int): Row reversal frequency.

    Returns:
        list of lists: Modified matrix.
    """
    for i in range(0, len(matrix), k):
        matrix[i] = matrix[i][::-1]
    return matrix

# Example usage:

# Define a sample matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Define k (the frequency of row reversal)
k = 2

# Call the function to reverse every k-th row
result_matrix = reverse_kth_rows(matrix, k)

# Print the modified matrix
for row in result_matrix:
    print(row)
