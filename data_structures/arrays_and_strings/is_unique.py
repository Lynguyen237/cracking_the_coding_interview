# Cracking the coding interview | Array & Strings
# Is Unique (p102pdf): Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# Examples
# "red" #true (unique)
# "book" #false (not unique)

# Edge cases
# "" #true (edge case)
# Does the string have numbers or space?

# Method - Dictionary
def is_unique_0(string):
    string_dict = {}
    # use set

    for char in string:
        if char not in string_dict:
            string_dict[char] = 1
        else:
            return False
    
    return True


# Method: Set
def is_unique_1(string):
    string_set = set()
    # use set

    for char in string:
        if char not in string_set:
            string_set.add(char)
        else:
            return False
    
    return True


# Method - Unique String No Data Structure
# https://www.geeksforgeeks.org/determine-string-unique-characters/
def is_unique_2(string):

    # sort the string
    string = sorted(string)

    for i in range(len(string)-1):
        if string[i] == string [i+1]:
            return False
    
    return True

# Method - Using ORD
def is_unique(string):
    # Assuming the string is ASCII (128 characters)
    if len(string) > 128:
        return False
    
    char_set = []
    for _ in range(128):
        char_set.append(False)
    
    for char in string:
        ascii_val = ord(char)
        if char_set[ascii_val]: # if char_set[ascii_val] is False, never enter the if statement
            return False
        char_set[ascii_val] = True
    
    return True


print(is_unique("dog")) # True
print(is_unique("book")) # False
print(is_unique("ab s")) # True
print(is_unique("ab s y")) # False