"""

Valid Parentheses - Given a string of brackets, 
check if it's valid.

"""

def isValid(string): # Stack
    stack = []
    closeToOpen = {")":"(", "}":"{", "]":"["}
    for s in string:
        if s in closeToOpen:
            if stack and stack[-1] == closeToOpen[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)
    
    return True if not stack else False

    

s = "(("
print(isValid(s))