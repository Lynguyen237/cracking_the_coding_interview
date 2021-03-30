# Assume you have a method isSubstring which checks if one word is a substring of another. 
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only 
# one call to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").


#==== Solution using isSubstring ====
# s1 = xy
# rotation of s1 = yx
# yx will alway be a substring of xyxy
# Hence we can check if s2 is a substring of s1s1. If true, s2 is a rotation of s1
def checkRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True
    
    return isSubstring(s1+s1,s2)
    
def isSubstring(s1,s2):
    return s2 in s1

print(checkRotation("waterbottle", "erbottlewat")) #True


#==== Solution for simple rotation checking (O(n) time & space complexibty) ====
def isRotation(s1,s2):

    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return True

    pivot_letters =  s1[-1]+s1[0]  # if s2 is a rotation of s1, it must contains "ew" or s[-1]+s[0]

    for i in range(len(s2)-1):
        if s2[i]+s2[i+1] == pivot_letters:
            right_side_len = len(s2[i+1:])
            if s2[:i+1] == s1[right_side_len:] and s2[i+1:] == s1[:right_side_len]:
                return True
    
    return False

# print(isRotation("waterbottle", "erbottlewat")) #True
# print(isRotation("waterbottle", "erbottlewta")) #False
# print(isRotation("waterbottl", "erbottlewat")) #False
# print(isRotation("waterbottle", "watertlebot")) #False
# print(isRotation("b", "b")) #True
# print(isRotation("", "")) #True