class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for x in nums:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        counter_desc = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        k_elements = []
        for x in counter_desc.keys():
            if k <= 0:
                break
            k_elements.append(x)
            k -= 1
        return k_elements
