import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Fill initial heaps
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1
        
        total_cost = 0

        for _ in range(k):
            if not left_heap:
                chosen = heapq.heappop(right_heap)
            elif not right_heap:
                chosen = heapq.heappop(left_heap)
            else:
                # Compare tops of both heaps
                if left_heap[0][0] <= right_heap[0][0]:
                    chosen = heapq.heappop(left_heap)
                else:
                    chosen = heapq.heappop(right_heap)
            
            cost, idx = chosen
            total_cost += cost

            # Refill the heap you took from
            if left <= right:
                if idx < left:
                    heapq.heappush(left_heap, (costs[left], left))
                    left +=1
                else:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1
        
        return total_cost
