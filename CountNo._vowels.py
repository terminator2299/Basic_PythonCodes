def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))




