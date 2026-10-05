class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for n in nums:
            if n in result:
                result[n] += 1
            else:
                result[n] = 1
        final = sorted(result, key=result.get, reverse=True)[:k]
        return final 
            