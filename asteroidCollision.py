class Solution(object):
    def asteroidCollision(self, asteroids):
        stack =[]
        for asteroid in asteroids:
            # Handle collisions for asteroids moving to the left
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid: #Top asteroid is smaller
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid: # Both asteroids are the same size
                    stack.pop()
                break # Current asteroid is destroyed
            else:
                # No collision, push the asteroid onto the stack
                stack.append(asteroid)
        return stack
