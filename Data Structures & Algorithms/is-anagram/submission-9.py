class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # appearing the same number of times
        if len(s) != len(t):
            return False
        
        s_map = {}
        for n in s:
            if n in s_map:
                s_map[n] += 1
            else:    
                s_map[n] = 1
        
        t_map = {}
        for m in t:
            if m in t_map:
                t_map[m] += 1
            else:
                t_map[m] = 1
        
        return s_map == t_map

         

        