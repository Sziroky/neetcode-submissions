class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, m in enumerate(nums):
            find = target - m
            if find in hashmap:
                return [hashmap[find], i]
            hashmap[m] = i
             
        
        
       