class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_l = list(s)
        s_l.sort()
        t_l = list(t)
        t_l.sort()
        for i in range(len(s)):
            if s_l[i] != t_l[i]:
                return False
        return True