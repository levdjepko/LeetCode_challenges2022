# let's find out the largest sum of a subarray of fixed size k

arr = [1,6,9,2,3,6, 1, 2,54, 2]

def largest_sum_in_subarray_of_size_k(arr, k):
    # we will use the sliding window of a fixed size k
    # and slide in across the input while keeping a track of sum under it
    left, right = 0, k
    sum = 0
    for i in range(k):
        sum += arr[i]
    max_subarray = sum
    for i in range(k, len(arr)):
        sum += arr[i]
        sum -= arr[i - k]
        max_subarray = max(max_subarray, sum)
    return max_subarray

print(largest_sum_in_subarray_of_size_k(arr, 3))
