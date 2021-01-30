# Cracking the coding interview | Array & Strings
# Is Unique (p102pdf): Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# Examples
# "red" #true (unique)
# "book" #false (not unique)

# Edge cases
# "" #true (edge case)
# Does the string have numbers or space?

def is_unique(string):
    string_dict = {}

    for char in string:
        if char not in string_dict:
            string_dict[char] = 1
        else:
            return False
    
    return True


print(is_unique("dog")) # True
print(is_unique("book")) # False
print(is_unique("ab s")) # True
print(is_unique("ab s y")) # False
    
    