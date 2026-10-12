class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # appearing the same number of times
        if len(s) != len(t):
            return False
        
        
        counts = {}

        for n in s:
            counts[n] = counts.get(n,0) + 1
        
        for m in t:
            counts[m] = counts.get(m,0) - 1

        
        return all(count == 0 for count in counts.values())

         

        