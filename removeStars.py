class Solution(object):
    def removeStars(self, s):
        stack =[]
        for char in s:
            if char=='*':
                if stack: # Only pop if the stack is not empty
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
