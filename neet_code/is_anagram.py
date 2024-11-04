class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        for char in s:
            if char in characters:
                count = characters[char]
                count += 1
                characters[char] = count
            else:
                characters[char] = 1
        for char in t:
            if char in characters:
                count = characters[char]
                count -= 1
                characters[char] = count            
            else:
                return False
        for char in characters:
            if characters[char] != 0:
                return False
        return True                   
