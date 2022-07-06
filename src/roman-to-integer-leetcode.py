# Anthony Leotta
# 2022-07-06
# This is what I submitted to leetcode.

class Solution:
    def romanToInt(self, s: str) -> int:
        decoder = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        values = [] # keep track of decoded values
        length=len(s)
        letters = list(reversed(s))

        for index2, letter in enumerate(letters):
            value = decoder[letter]
            if index2>0:
                value2 = decoder[letters[index2-1]]
                if value2 > value:
                    values.append(-value)
                else:                    
                    values.append(value)
            else:
                values.append(value)

        total = sum(values)
        return total
