# Problem 1 — Duplicate Detection
# Return True if any value appears more than once, otherwise return False.
def contains_duplicate(nums):
    s = set()

    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False

""" create a set, go through every element, check if it exists in set, else add it to set, but if its in set, return True
    because sets can remove duplicates
    we will get O(n) and O(n) time and space in worst case we have to store n elements and go through n elements """



#Problem 2 — Find the Most Frequent Value
# Return the value that appears most frequently.

def most_frequent(nums):
    freq = {}
    highest_value = 0
    most_frequent_value = None

    for i in nums:
        freq[i] = freq.get(i, 0) + 1
        if freq[i] > highest_value:
            highest_value = freq[i]
            most_frequent_value = i
        

    return most_frequent_value

print(most_frequent([4, 2, 4, 7, 2, 4, 9])) 

""" we can use a dictionary to solve this, because it can store the element and its frequency.first we go through every element, 
    we if check it is already in the dict, if yes, increment its frequency also compare its frequency with the highest frequency variable to store the highest value 
    if it does not exist , add it and give its value as 1. after loop ends return the highest frequency variable
    we will get O(n) and O(n) time and space in worst case """



# Problem 3
# Return the number of contiguous subarrays whose sum equals 3.

def number_of_contiguous_subarrays(nums, target):
    seen = {0: 1}
    count = 0
    prefix = 0

    for i in nums:
        prefix += i
        needed = prefix - target

        if needed in seen:
            count += seen[needed]
        seen[prefix] = seen.get(prefix, 0) + 1

    return count

""" we can use  prefix + map, prefix helps us find the sum of the window and map helps us store the needed value, which is derived from current_prefix - target
we go through every element , we  calculate the needed, check if needed is in the seen,
if we found a sub array whose sum is the target, we increment the count
we also add/increment the current prefix to the seen
complexity will be O(n) and O(n), since we go through every element and store the prefix in worst case """