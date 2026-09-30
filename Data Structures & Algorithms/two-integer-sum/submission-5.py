class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            to_search = target - n
            if to_search in hashmap:
                return [hashmap[to_search], i]
            hashmap[n] = i
        
       