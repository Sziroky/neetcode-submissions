class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h_s = {}
        h_t = {}

        for n,m in zip(s,t):
            h_s[n] = h_s.get(n,0) + 1
            h_t[m] = h_t.get(m,0) + 1

        print(h_s)
        print(h_t)
        return h_s == h_t