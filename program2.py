class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0

        for char in s:
            current_value = roman_map[char]
            total += current_value
            
            
            if prev_value < current_value:
                total -= 2 * prev_value  # Subtract the previous value twice (once added, once to negate)
                
            prev_value = current_value
        
        return total
solution = Solution()
print(solution.romanToInt("III"))      
print(solution.romanToInt("LVIII"))      
print(solution.romanToInt("MCMXCIV"))    
print(solution.romanToInt("IV"))         
print(solution.romanToInt("IX"))        



