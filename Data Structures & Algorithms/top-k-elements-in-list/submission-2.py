class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for x in nums:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        return list(dict(sorted(counter.items(), key=lambda x: x[1], reverse=True)).keys())[:k]