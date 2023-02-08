# 904. Fruit into baskets

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        d = defaultdict(lambda: 0)

        #print( sorted(fruits)[::-1 ])

        for i in fruits:
            d[i] +=1

        sorted_dict = sorted(d.items(), key = lambda x:x[1], reverse=True)
        
        if len(sorted_dict) >= 2:
            return sorted_dict[0][1] + sorted_dict[1][1]
        elif len(sorted_dict) == 1:
            return sorted_dict[0][1]
        else:
            return 0
        



testcases = [
    [3,3,3,1,2,1,1,2,3,3,4],
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
]

s = Solution()

for c in testcases:
    print("Testcase input: {}".format(c))
    print("Output: ",end='')
    print(s.totalFruit(c))
