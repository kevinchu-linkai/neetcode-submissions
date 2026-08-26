class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        
        buckets = [[]for _ in range(len(nums)+1)]

        for num in counts:
            buckets[counts[num]].append(num)

        result = []

        for most_frequent in range(len(buckets)-1, 0, -1):
            for num in buckets[most_frequent]:
                result.append(num)
                if len(result) == k:
                    return result