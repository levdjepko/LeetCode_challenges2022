class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # return the max average subarray of fixed size
        left = 0
        right = k - 1
        subarray = sum(nums[0 : k])
        max_avg_sum = subarray
        
        for i in range (k, len(nums)):
            subarray -= nums[i - k]
            subarray += nums[i]
            max_avg_sum = max(max_avg_sum, subarray)
            
            
        return max_avg_sum  / k   
