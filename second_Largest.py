def second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements to find second largest

    largest = second = float('-inf')  # Initialize to very small value

    for num in nums:
        if num > largest:
            second = largest  # Update second before changing largest
            largest = num
        elif largest > num > second:
            second = num  # Only update second if num is in between

    return second if second != float('-inf') else None
