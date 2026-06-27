class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for i in range(len(s)):
            mp1[s[i]]+=1
            mp2[t[i]]+=1
        for i in range(len(s)):
            if mp1[s[i]] != mp2[s[i]]:
                return False
        return True