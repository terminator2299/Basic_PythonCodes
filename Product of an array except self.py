def product_except_self(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    for i in range(n):
        output[i] = left[i] * right[i]

    return output

# Example usage
nums = list(map(int, input("Enter array elements: ").split()))
print("Product array:", product_except_self(nums))
