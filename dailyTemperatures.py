class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = [] # stores indices of days

        for i, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)
        
        return answer
