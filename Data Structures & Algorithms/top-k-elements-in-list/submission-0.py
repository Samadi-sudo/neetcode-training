class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            dictionary[i] = 1 + dictionary.get(i, 0)
        test = sorted(dictionary.keys(), key=lambda x: dictionary[x], reverse=True)
        return [test[i] for i in range(k)]
