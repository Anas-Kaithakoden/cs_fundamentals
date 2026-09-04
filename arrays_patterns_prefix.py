# Create another array where each position stores the sum of everything before it.
# range sum = prefix[right] - prefix[left - 1]
# Range-sum queries

def build_prefix():
    arr = [3, 2, 5, 1, 4, 6]
    prev_sum = 0

    prefix = []

    for i in range(len(arr)):
        prev_sum += arr[i]
        prefix.append(prev_sum)

    print(prefix)



def range_sum(left, right):
    prefix = [3, 5, 10, 11, 15, 21]
    
    if left == 0:
        total = prefix[right]
    else:
        total = prefix[right] - prefix[left-1]

    print(total)

def answer_queries(arr, queries):
    prev_sum = 0
    prefix = []
    total = []

    for element in arr:
        prev_sum += element
        prefix.append(prev_sum)

    for query in queries:
        if query[0] == 0:
            total.append(prefix[query[1]])
        else:
            total.append(prefix[query[1]]- prefix[query[0] - 1])

    print(total)

def longest_subarray_prefix():
    arr = [1, 2, 3, -2, 5, 1]
    target = 6
    max_length = 0

    prev_sum = 0
    prefix = []
    prefix.append(0)
    for element in arr:
        prev_sum += element
        prefix.append(prev_sum)

    for i in range(len(prefix)):
        for j in range(i+1, len(prefix)):
            current_sum = prefix[j] - prefix[i]    

            if current_sum == target:
                max_length = max(max_length, j-i)
    print(max_length)

# longest_subarray_prefix()
# answer_queries([2, 4, 1, 5, 3, 6],[[1, 3],[0, 4],[2, 5],[3, 3]])
# range_sum(0,4)
# build_prefix()