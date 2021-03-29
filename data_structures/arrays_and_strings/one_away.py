# Cracking the coding interview. Prob 1.5 (Array)
# There are three types of edits that can be performed on strings: insert a character, 
# remove a character, or replace a character. Given two strings, write a function to check 
# if they are one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true 
# pales. pale -> true 
# pale. bale -> true 
# pale. bake -> false 
# Hints: #23, #97, #130

#==== Solution 1 - O(n) ====
def one_away(str1, str2):

    if len(str1) == len(str2) == 0:
        return True
    
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    # replace a char
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
            if count > 1:
                return False
        return True

    # insert a char OR remove a char are the reverse of each other
    # if we start with the longer string, it will always be "removal" to convert it into the longer string
    # find the longer string
    start_str_len = max(len(str1), len(str2))
    if len(str1) == start_str_len:
        start_str = str1
        end_str = str2
    else:
        start_str = str2
        end_str = str1

    # loop through each character in the first, longer string
    for i in range(len(start_str)-1):
        if start_str[i] != end_str[i]: # if the characters are different
            if start_str[i+1] != end_str[i]: # use the next character in the longer string to compare instead
                return False # if the characters are also different, return False
    return True


#==== Test cases
# # edge cases
# print(one_away("","")) # True
# print(one_away("pale", "pa")) # False
# print(one_away("pale", "palebk")) # False

# # same length
# print(one_away("pale", "bake")) # False
# print(one_away("pale", "pade")) # True, middle 3rd character different

# # len(str1) > len(str2)
# print(one_away("pale", "ale")) # True
# print(one_away("pale", "ald")) # False

# # len(str1) < len(str2)
# print(one_away("ale", "pale")) # True
# print(one_away("ale", "pade")) # False

# print(one_away("palex", "paex")) # True, str2 missing the middle character
# print(one_away("palex", "pulexu")) # False, str2 are 2 edits away
# print(one_away("alex", "xel")) # False, permutation with 1 difference

# Alternative solution using zip(): https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p05_one_away.py