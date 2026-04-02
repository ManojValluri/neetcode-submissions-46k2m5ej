class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combo = {}
        arr = []
        for i, x in enumerate(nums):
            if target-x in combo:
               arr.append(combo[target-x])
               arr.append(i)
               return arr 
            combo[x] = i
        return arr
