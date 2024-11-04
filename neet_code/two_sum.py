class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we can iterate over the list and save the indices and the values as we go
        # then, we can go over the list again and check the differences with the target
        seen_numbers = {}
        for index, value in enumerate(nums):
            seen_numbers[value] = index

        for key, value in enumerate(nums):
            # how much we "need" to match
            difference = target - value  
            if difference in seen_numbers and key != seen_numbers[difference]:
                return [key, seen_numbers[difference]]  

# runtime is O(n)
# space complexity is O(n)
