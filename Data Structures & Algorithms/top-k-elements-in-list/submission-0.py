class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        #Sort dictionary
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

        res = list(freq.keys())[:k]
        return res
