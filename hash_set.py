def check_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False



def distinct_values():
    a = [1, 2, 2, 3, 4]
    b = [2, 2, 4, 5, 6]

    s1 = set()
    s2 = set()
    for i in a:
        s1.add(i)
    for j in b:
        s2.add(j)

    return len(s1 & s2)

print(distinct_values())


# print(check_duplicates([1, 2, 3, 4]))