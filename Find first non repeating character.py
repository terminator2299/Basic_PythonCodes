def first_non_repeating_char(s):
    freq = {}

    # Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find the first character with frequency 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

# Example usage
s = input("Enter a string: ")
result = first_non_repeating_char(s)
print("First non-repeating character:", result if result else "None found")
