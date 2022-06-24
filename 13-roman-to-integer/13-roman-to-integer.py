class Solution:
    def romanToInt(self, s: str) -> int:
            map_romans = {
                "I": 1,
                "V": 5, 
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500, 
                "M": 1000
            }
            num = 0
            value = 0
            for letter in s[::-1]:
                preValue = value
                value = map_romans.get(letter)
                if value < preValue:
                        num -= value
                else:
                    num += value
            return num 