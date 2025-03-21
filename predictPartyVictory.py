class Solution(object):
    from collections import deque
    def predictPartyVictory(self, senate):
        n = len(senate)
        radiant_queue = deque()
        dire_queue = deque()

        # Populate initial queues with senator indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        
        #Process voting rounds
        while radiant_queue and dire_queue:
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()

            # The senator with the smaller index bans the other
            if r_index < d_index:
                radiant_queue.append(r_index + n)
            else:
                dire_queue.append(d_index + n)
            
        return "Radiant" if radiant_queue else "Dire"
