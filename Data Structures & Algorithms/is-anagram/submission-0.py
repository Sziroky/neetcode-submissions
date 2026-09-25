class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for n in s:
            if n in hash_s:
                hash_s[n] = hash_s[n] + 1
            else:
                hash_s[n] = 1
        print(hash_s)            
        
        for m in t:
            if m in hash_t:
                hash_t[m] += 1
            else:
                hash_t[m] = 1
        print(hash_t)
        return hash_s == hash_t
        