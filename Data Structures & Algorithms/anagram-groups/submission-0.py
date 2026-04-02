class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            if tuple(sorted(x)) in d:
                d[tuple(sorted(x))].append(x)
            else:
                d[tuple(sorted(x))] = [x]
        
        result = []
        for x in d:
            result.append(d[x])
        return result