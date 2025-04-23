import heapq
class SmallestInfiniteSet(object):

    def __init__(self):
        self.current = 1 # The next smallest number we haven't popped
        self.added_back = []
        self.added_set = set()

    def popSmallest(self):
        if self.added_back:
            smallest = heapq.heappop(self.added_back)
            self.added_set.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest
    
    def addBack(self, num):
        # Only add back if the number is less than current (i.e., it was popped),
        # and it's not already in the heap
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)
        
