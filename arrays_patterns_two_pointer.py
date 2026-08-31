
#! Two pointers: 
#* Opposite-end pointers
# Properties : Sorted array
#? 1)
def twoPointer_two_sum_sorted():
    arr = [1,4,6,8,9,12,15]
    target = 21

    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            print([arr[left], arr[right]])
            return

        elif total < target:
            left += 1

        else:
            right -= 1

    print [""]
                    # Complexity O(n) time, O(1) space

# Reasoning:
# Sorted array
#      ↓
# Put one pointer at each end
#      ↓
# Calculate sum
#      ↓
# Too small → move left
# Too large → move right
# Equal     → found

#? 2)
# Reverse an array in-place.
def twoP_reverse_array():
    arr = [1,4,6,7,8,9,12,15]
    left = 0
    right = len(arr) - 1

    temp = arr[left]

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    print(arr)

#? 3)
# Palindrome
def twoP_palindrome():
    arr = [1,3,5,7,5,3,1]
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True

#* read/write pointer pattern
#? 4) 
# Remove Duplicates  
def twoP_remove_duplicates():
    arr = [1,1,3,5,5,6,8,9,9]

    left = 0
    right = left + 1

    unique_count = 1

    while right < len(arr):
        if arr[left] == arr[right]:
            right += 1
        else:
            left += 1
            arr[left] = arr[right]
            right += 1
            unique_count += 1
    print(arr[0:unique_count], unique_count)

#? 5)
def twoP_move_zeros():
    arr = [0, 1, 0, 3, 12]
    position = 0

    for scanner in range(len(arr)):
        if arr[scanner] != 0:
            arr[position] = arr[scanner]
            position += 1

    while position < len(arr):
        arr[position] = 0
        position += 1

    print(arr)



# twoPointer_two_sum_sorted()
# twoP_reverse_array()
# print(twoP_palindrome())
# twoP_remove_duplicates()
# twoP_move_zeros()