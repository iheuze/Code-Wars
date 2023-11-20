def main_diagonal_product(matrix):
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return None

    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return None

    # Calculate the product of the main diagonal
    product = 1
    for i in range(len(matrix)):
        if len(matrix[i]) > i:  # Check if the diagonal element exists
            product *= matrix[i][i]
        else:
            return None  # Return None if the matrix is not well-formed

    return product
