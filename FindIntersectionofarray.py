def array_intersection(arr1, arr2):
    freq = {}
    result = []

    # Store frequency of elements in arr1
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1

    # Check common elements in arr2
    for num in arr2:
        if freq.get(num, 0) > 0:
            result.append(num)
            freq[num] -= 1  # Avoid duplicates

    return result

# Example
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(array_intersection(arr1, arr2))  # Output: [2, 2]
