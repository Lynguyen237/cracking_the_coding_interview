# Design an algorithm to find all pairs of integers within an array which sum to a specified value.
# Answer: p16.24 pg 520
# [6,6] 12 -> [(6, 6)]
# [1,2] 5 -> []
# [1,3,3,2,4,4] -> 6 => [(3,3),(2,4),(2,4)]


#==== Optimized (O(n)) using dictionary with just 1 loop ====
# This method will not use more than one instance of a number

def sum_to_target(array,target):

    no_dict = {}
    results = []
    
    for i in range(len(array)):
        cur = array[i]
        print(f'idx {i}, {array[i]}, {no_dict}')
        if target - cur in no_dict and no_dict[target-cur] != 0:
            results.append((cur, target-cur))
            no_dict[target-cur] -= 1
        else:
            if cur not in no_dict:
                no_dict[cur] = 1
            else:
                no_dict[cur] += 1
                
    return results


#==== Optimized O(n) using dictionary with 2 loops ====
# This method will not use more than one instance of a number
def sum_to_target1(array,target):
    
    if len(array) == 0:
        return []
    
    no_dict = {}
    results = []
    
    for i in range(len(array)):
        if array[i] not in no_dict:
            no_dict[array[i]] = 1
        else:
            no_dict[array[i]] += 1

    for i in no_dict:
        # if the complement value target-i is in the dictionary and there is at least 1 instance of i and or target-i
        # add a pair (i, target-i) to the results list.
        if target-i in no_dict and no_dict[i] != 0 and no_dict[target-i] != 0:
            results.append((i,target-i))
            no_dict[target-i] -= 1
            
    return results


#==== Brute Force (return duplicated value) ===
def sum_to_target0(array,target):
    
    if len(array) == 0:
        return []
    
    results = []
    
    for i in range(len(array)):
        for j in range(i,len(array)):
            if i != j and array[i] + array[j] == target:
                results.append((array[i],array[j]))
            
    return results
                               
# print(sum_to_target([],1)) #[]
# print(sum_to_target([6,6],12)) #[(6,6)]
# print(sum_to_target([1,2],5)) #[]
# print(sum_to_target([1,3,3,2,4,4],6)) #[(3,3),(2,4),(2,4)] w brute force, [[(3,3),(2,4)] with optimized
print(sum_to_target([8,3,3,-2,4,4,3],6)) #[(8,-2)(3,3)] w optimized
print(sum_to_target([8,3,3,-2,4,4,8,-2,3,3],6)) #[(8,-2),(-2,8),(3,3),(3,3)] w optimized
