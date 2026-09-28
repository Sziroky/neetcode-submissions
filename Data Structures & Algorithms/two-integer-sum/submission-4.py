class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            rest = target - n
            if rest in hashmap:
                return [hashmap[rest], i]

            hashmap[n] = i 