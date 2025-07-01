def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

# Example usage
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Is rotation:", is_rotation(s1, s2))