class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):

            look = target - num #Calc the remaining
            
            #Check if the remaining is in the hashmap and its not the same element
            if look in hashmap and hashmap[look] != i:
                return [hashmap[look], i] #return the remaining and the index of current element (always i > hashmap[look])
            
            hashmap[num] = i #if nothing found add the value and index into hashmap
