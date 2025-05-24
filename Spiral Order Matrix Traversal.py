def spiral_order(matrix):
    result = []
    if not matrix:
        return result

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top < bottom and left < right:
        # Traverse from left to right
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1

        # Traverse down
        for i in range(top, bottom):
            result.append(matrix[i][right - 1])
        right -= 1

        if top < bottom:
            # Traverse from right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

        if left < right:
            # Traverse up
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Spiral order:", spiral_order(matrix))
