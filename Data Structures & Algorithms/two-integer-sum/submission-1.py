class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, x in enumerate(nums):
            for y in dict.keys():
                if x == y[1]:
                    dict[(target-x, x)].append(i)
                    return list(dict[(target-x, x)])
            dict[(x,target-x)] = [i]
