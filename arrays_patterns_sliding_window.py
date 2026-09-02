def sum_subarray():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    window_sum = sum(arr[:k])
    max_sum = window_sum
    print(arr[:k])
    print(f"sum={window_sum}")

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        if window_sum > max_sum:
            max_sum = window_sum

        print(arr[i-k+1:i+1])
        print(f"sum={window_sum}")

    print(f"Max sim = {max_sum}")


def sum_longest_contiguous_subarray():
    arr = [2, 1, 5, 2, 3, 2]
    target = 7    
    window_sum = 0

    left = 0
    max_length = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > target:
            window_sum -= arr[left]
            left += 1

        max_length = max(max_length, right-left + 1)

    print(max_length)

sum_longest_contiguous_subarray()
# sum_subarray()