class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            dictionary[i] = 1 + dictionary.get(i, 0)
        for ke, v in dictionary.items():
            freq[v].append(ke) 

        res = []
        for i in range(len(freq) - 1 , 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k :
                    return res