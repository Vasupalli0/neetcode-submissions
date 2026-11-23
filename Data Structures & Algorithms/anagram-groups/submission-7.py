class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #c is character and s is string in the dictionary
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #a to z

            for c in s: 
                count[ord(c) - ord('a')] += 1 #ascii of c minus ascii of lowercase a

            res[tuple(count)].append(s) #lists cannot have keys so tuples.
        return list(res.values())
        