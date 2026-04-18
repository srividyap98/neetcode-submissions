# string = "[{[()]}]"
# if { in 0 than } -1 
# 0+1 -1-1 
# i -(i+1)
# 2 -(2+1)
# 2 -3


# 0 to len() -1 
# 1 to len()-(1+1)
# i to len() - (i+1)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False




        