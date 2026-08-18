class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = list(s)
        sorted_s.sort()
        sorted_t = list(t)
        sorted_t.sort()

        if sorted_s == sorted_t:
            return True
        else:
            return False