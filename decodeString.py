class Solution(object):
    def decodeString(self, s):
        stack =[]

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # Pop characters until '[' is found
                current_string=''
                while stack[-1] != '[':
                    current_string = stack.pop() + current_string
                # Pop the '['
                stack.pop()
                # Pop the number
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # Push the decoded string back to the stack
                stack.append(int(k) * current_string)

        #combine all elements in the stack to get the final result
        return ''.join(stack)              
