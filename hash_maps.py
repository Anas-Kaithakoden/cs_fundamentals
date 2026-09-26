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

def prefix_longest_subarray_sum(nums, target):
    seen = {0: -1}
    prefix = 0
    longest = 0
    

    for i, num  in enumerate(nums):

        prefix += num

        needed = prefix - target
        if needed in seen:
            longest = max(longest, i-seen[needed])
        if prefix not in seen:
            seen[prefix] = i

    return longest

def number_of_contiguous_subarrays(nums, target):
    seen = {0: 1}
    prefix = 0
    count = 0

    for num in nums:

        prefix += num
        needed = prefix-target
        if needed in seen:
            count += seen[needed]

        seen[prefix] = seen.get(prefix, 0) + 1

    return count


print(number_of_contiguous_subarrays(nums = [1, 2, 1, 2, 1], target = 3))
# print(prefix_longest_subarray_sum(nums = [2, 3, -2, 4, 1], target = 5))
# print(two_sum([5, 1, 8, 6, 3], 9))
# count_frequency()