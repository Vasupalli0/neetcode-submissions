class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {} #A hashamp to store the value and index of each element in the array
        for i,n in enumerate(nums): #enumerating the all the indices in the hashmap
            diff = target - n  
            if diff in need: #check if the complement is in the hashmap
                return [need[diff], i] 
            need[n] = i #else return empty array

                