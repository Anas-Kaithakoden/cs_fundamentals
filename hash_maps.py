def count_frequency():
    nums = [4, 2, 4, 7, 2, 4]
    freq = {}

    for i in nums: # freq[i] = freq.get(i, 0) + 1
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    print(freq)


def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i
print(two_sum([5, 1, 8, 6, 3], 9))
# count_frequency()