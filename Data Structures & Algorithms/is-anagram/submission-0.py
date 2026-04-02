class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        for x in s:
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1

        for x in t:
            if x in d1:
                d1[x] -= 1
            else:
                return False

        for x in d1:
            if d1[x] != 0:
                return False

        return True