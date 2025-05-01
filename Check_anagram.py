def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")