class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # for i in range (0, len(s)//2):
        #     temp = s[i]
        #     s[i] = s[len(s) - 1 - i]
        #     s[len(s) - 1 - i] = temp
        
        # OR: using two pointer method instead:
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right],s[left]
            left += 1
            right -= 1
            
