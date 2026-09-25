class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        print(nums)
        consec = []
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            if nums[i] == 0 or i == (len(nums)-1):
                consec.append(counter)
                counter = 0
        return max(consec)
            

            
        