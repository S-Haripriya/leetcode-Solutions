
'''Given a roman numeral, convert it to an integer'''

class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0
        prev = 0

        for ch in s:
            value = roman[ch]

            if value > prev:
                number += value - 2 * prev
            else:
                number += value

            prev = value

        return number
    