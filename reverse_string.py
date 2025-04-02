# This must be without using built in functions

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

s = "Hello, World!"
print(reverse_string(s))