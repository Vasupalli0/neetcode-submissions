class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
           return False
        
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i in t:
            if freq.get(i, 0) == 0:
                return False
            freq[i] -= 1
        return True