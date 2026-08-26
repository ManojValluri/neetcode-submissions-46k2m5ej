class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        for i in strs:
            if tuple(sorted(i)) in anagramDict:
                anagramDict[tuple(sorted(i))].append(i)
                
            else:
                anagramDict[tuple(sorted(i))] = [i]
        
        anagramList = []

        for i in anagramDict.values():
            anagramList.append(i)

        return anagramList