def find_single_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage
arr = list(map(int, input("Enter elements (all in pairs except one): ").split()))
print("Element that appears only once:", find_single_element(arr))