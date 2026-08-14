class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = Counter(nums)
        heap = []

        for key in seen:
            heapq.heappush(heap, (seen[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]