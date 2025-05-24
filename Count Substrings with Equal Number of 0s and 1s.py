def count_equal_0_1_substrings(s):
    count = 0
    for i in range(len(s)):
        zero = one = 0
        for j in range(i, len(s)):
            if s[j] == '0':
                zero += 1
            else:
                one += 1
            if zero == one:
                count += 1
    return count

# Example usage
s = input("Enter a binary string: ")
print("Number of substrings with equal 0s and 1s:", count_equal_0_1_substrings(s))
