class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        # s is a string that contains lowercase english letters
        # matrix called shift 
        # is shifting left is s[-1] to left and shifting right is the s[0] to right?


        for direction, amount in shift:
            amount %= len(s)

            if direction == 0:
                s = s[amount:] + s[:amount]
            else:
                s = s[-amount:] + s[:-amount]
        return s


            


        