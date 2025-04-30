# Using set

def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage with user input
user_input = input("Enter list elements separated by spaces: ")
arr = list(map(int, user_input.split()))
print("List after removing duplicates:", remove_duplicates(arr))
