class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if abs(y-x) > 0:
                heapq.heappush(stones, y-x)

        return abs(stones[0]) if len(stones) == 1 else 0