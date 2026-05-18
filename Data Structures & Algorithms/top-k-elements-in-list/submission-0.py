class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for n in nums:
            num_counts[n] = num_counts.get(n, 0) + 1

        sorted_by_freq = sorted(
            num_counts, 
            key=num_counts.get, 
            reverse=True
        )

        return sorted_by_freq[:k]