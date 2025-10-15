# create a sliding window
# to get the longest subarray the sum of which is less than K

arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

def longest_subarray(arr, k):
    # implement the sliding window and track the sum of elements within it
    curr = 0
    left = 0
    len_of_longest_subarray = 0
    for right in range(len(arr)):
        curr += arr[right]
        while curr > k:
            curr -= arr[left]
            left += 1
        # at this point, the subarray within the window matches the condition
        len_of_longest_subarray = max(len_of_longest_subarray, right - left + 1)
    return len_of_longest_subarray

print(longest_subarray(arr, k))
