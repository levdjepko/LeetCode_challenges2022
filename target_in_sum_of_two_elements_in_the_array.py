# find the target sum in the array

def target_in_array_sum(array, target):
    # the array is already sorted. If not, the complexity goes from O(n) to O(n*ln n)
    #array.sort()
    left, right = 0, len(array) - 1
    while left < right:
        if array[left] + array[right] == target:
            return True
        elif array[left] + array[right] > target:
            # too large sum. Move the right pointer to the left
            right -= 1
        elif array[left] + array[right] < target:
            # the sum is too small, move the left pointer
            left += 1
    return False

print(target_in_array_sum([1,2,3,4,5], 5))
print(target_in_array_sum([2,3,7,8,10], 5))
print(target_in_array_sum([2,3,7,8,10], 2))
