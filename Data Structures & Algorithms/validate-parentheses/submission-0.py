class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brakcets = {'(': ')', '{': '}', '[':']'}
        for i in s:
            if i in brakcets:
                stack.append(i)
            else:
                if i == brakcets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False