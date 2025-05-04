def count_frequencies(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Example usage
arr = list(map(int, input("Enter list elements: ").split()))
frequencies = count_frequencies(arr)
print("Frequencies:", frequencies)