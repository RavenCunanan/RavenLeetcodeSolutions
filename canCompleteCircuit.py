class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If we run out of gas at station i, we can't start from start_index
            if curr_tank < 0:
                # Start fresh from the next station
                start_index = i + 1
                curr_tank = 0
        
        return start_index if total_tank >=0 else -1
        
