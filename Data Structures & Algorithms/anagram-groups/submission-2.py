class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for i,s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            tupled_s = tuple(sorted(s))
            result.setdefault((tupled_s),[]).append(s)
        
        return list(result.values())

            