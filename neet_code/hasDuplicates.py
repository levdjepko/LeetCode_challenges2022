def hasDuplicate(self, nums: List[int]) -> bool:
        # use a hashset to keep track of seen items in an array
        seen_items = {}
        for item in nums:
            if item in seen_items:
                return True
            else:
                seen_items[item] = 1  
        return False 
