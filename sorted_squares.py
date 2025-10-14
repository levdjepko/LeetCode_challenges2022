class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        from collections import deque
        # use the queue to collect the items in decreasing order
        q = deque()
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                q.appendleft(nums[right] ** 2)
                right -= 1
            else:
                q.appendleft(nums[left] ** 2)    
                left += 1
        return list(q)        
