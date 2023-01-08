
# %%

class Solution:
    def isValid(self, s: str) -> bool:

        count = [0,0,0]

        b1 = {
            '(': 1,
            ')': -1
        }
        b2 = {
            '[': 1,
            ']': -1
        }
        b3 = {
            '{': 1,
            '}': -1
        }

        for c in s:
            if c in b1.keys(): count[0] += b1[c]
            if c in b2.keys(): count[1] += b2[c]
            if c in b3.keys(): count[2] += b3[c]

            if len(list(filter(lambda x: x!=0,count))) > 1: return False
             

        if len(list(filter(lambda x: x!=0,count))) > 0: return False
        return True
            




testcases = [
    '()[]{}',
    '[](',
    '(])',
    '{}'
]

s = Solution()

for case in testcases:
    if s.isValid(case):
        print(case, "megfelel")
    else:
        print(case, "bajos")

# %%