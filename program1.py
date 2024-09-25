class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping.keys():  # If it's a closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
                
        return not stack  # True if no unmatched opening brackets are left


