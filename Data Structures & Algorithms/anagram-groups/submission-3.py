class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for s in strs:
            key = tuple(sorted(s))
            result.setdefault((key),[]).append(s)
            
        return list(result.values())

            