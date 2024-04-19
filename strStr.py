#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range (0, len(haystack)):
            if haystack[i] == needle[0] and len(haystack) - i >= len(needle):
                # found a first letter match, continue the check:
                for j in range (0, len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return -1         
