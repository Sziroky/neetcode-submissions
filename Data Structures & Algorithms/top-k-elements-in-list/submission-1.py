class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for n in nums:
            h_map[n] = h_map.get(n,0) + 1
        top_k = sorted(h_map, key=h_map.get, reverse=True)[:k]
        return top_k

            