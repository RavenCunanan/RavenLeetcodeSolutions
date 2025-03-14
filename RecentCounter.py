from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.queue =deque() # Queue to store request timestamps
        

    def ping(self, t):
        self.queue.append(t) # Add new request timestamp

        #Remove outdated requests (older than t -3000)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
    
        return len(self.queue) # Return the number of requests in the last 3000ms       


