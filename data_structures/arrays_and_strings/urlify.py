# URLify: Write a method to replace all spaces in a string with '%20: 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input:  "Mr John Smith    ", 13 
# Output: "Mr%20John%20Smith"


# Method 0 - if we are allowed to write a new string - (O(n))
def urlify_0(string, length):

    final_str = ""

    for char in string[0:13]:
        if char != " ":
            final_str += char
        else:
            final_str += "%20"
    
    return final_str


# If the actual length is not given, then we can calculate it as follows
    # # Count the number of spaces at the end
        # space_count = 0
        # for char in reversed(string):
        #     if char == " ":
        #         space_count += 1
        #     else:
        #         break

        # last_char_idx = len(string) - space_count
        # for char in string[0:last_char_idx]

# Method 2: Replace the string in place
def urlify_solution(string, length):

    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

    # idx = len(string)

    # for i in reversed(range(length)):
    #     if string[i] != " ":
    #         string[idx] = string[i]
    #         idx -= 1
    #     else:
    #         string[idx-3:idx] = "%20"
    #         idx -= 3
    
    # return string

# Method 3 - use .replace
def urlify(string, length):

    string = string[0:length].replace(" ","%20")

    return string

print(urlify("Mr John Smith    ", 13))
