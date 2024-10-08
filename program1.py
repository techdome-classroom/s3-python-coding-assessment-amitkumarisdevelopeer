class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  
                stack.append(char)
            elif char in mapping.keys(): 
                if not stack or stack.pop() != mapping[char]:
                    return False
                
        return not stack 
solution = Solution()
print(solution.isValid("()"))        
print(solution.isValid("()[]{}"))    
print(solution.isValid("(]"))        
print(solution.isValid("([)]"))      
print(solution.isValid("{[]}"))      





