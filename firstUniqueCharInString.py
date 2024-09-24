class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## return the first unique character in a string
        
        # we can do a dictionary with a key = letter and a value = its index
        # when we encounter the same character again, we set the value to -1
        # after we iterate over all the strings, we should have a few non-repeating characters with some valid indexes,
        # and some repeating characters with -1's. We grab the smallest index and return it
        dict = {}
        for i in range (0, len(s)):
            if dict.get(s[i]) is None:
                # new character
                dict[s[i]] = i     # e.g.'a' = 3
            else: 
                # we have already seen this character
                dict[s[i]] = -1
        # at this point, dictionary would have all the letters and we just need to grab the smallest index
        
        for i in range (0, len(s)):
            if dict.get(s[i]) > -1:
                return dict.get(s[i])
        return -1    
            
