from collections import OrderedDict

def first_non_repeating_char(s):
    char_count = OrderedDict()
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char, count in char_count.items():


        
        if count == 1:
            return char

    return None




# Example usage
s = input("Enter a string: ")
result = first_non_repeating_char(s)
if result:
    print("First non-repeating character:", result)
else:
    print("None")
