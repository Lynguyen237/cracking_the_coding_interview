# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string, 
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, # 110

#==== Solution (O(n))
def string_compression(string):
    """ Perfoprm basic string compression using the counts of repeated characters"""
    if string == "": 
        return ""
    
    new_str = ""

    i = 0
    count = 1
    new_str += string[i]

    while i < len(string) - 1:
        if string[i+1] == string[i]:
            count +=1
            i += 1   
        else:
            new_str += str(count) + string[i+1]
            count = 1
            i += 1
    new_str += str(count)
    
    return min(string, new_str, key = len) #return the smaller string


print(string_compression("aabcccccaaa")) #a2b1c5a3
print(string_compression("")) #""
print(string_compression("abca")) #abca
print(string_compression("aBDDdca")) #a1B1D2d1c1a1

# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p06_string_compression.py