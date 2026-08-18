class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        maxHeap
        1. iterate through the points list:
            - compute the euclidean distance of each point with the origin
            - store the distance as a tuple with its point
            - ensure the size of the heap is k by popping when it exceeds
        2. return the points left in the heap via list comprehension

        time: O(n * log k)
        space: O(k)
        '''

        maxHeap = []
        for x, y in points:
            dist = -(x**2 + y **2)
            heapq.heappush(maxHeap, (dist, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[x, y] for dist, x, y in maxHeap]