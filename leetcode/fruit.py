# 904. Fruit into baskets
import timeit

from collections import defaultdict
class Solution:

    def totalFruit(self, fruits: list[int]) -> int:

        trackbuckets = list()
        startpositions = list()
        buckets = list()

        max = 0


        # we are collecting all the positions where a new bucket should be opened
        # * there is a new type of fruit which is NOT in the last 2 types
        # * the "buckets" list have to be trimmed to the last 2 items
        for i,fruit in enumerate(fruits):
            if not fruit in trackbuckets:
                trackbuckets.append(fruit)
                startpositions.append(i)
                buckets.append(defaultdict(lambda: 0))
                if len(trackbuckets) > 2:
                    trackbuckets.pop(0)
            
            # trying to enumerate "buckets" and throw out elements 
            for j, bucket in enumerate(buckets):
                bucket[fruit] += 1

                if len(bucket) > 2:
                    curr = sum(list(dict(bucket).values())[:2])
                    if curr > max: max = curr

                    # HERE IS THE PROBLEM: popping the item makes the
                    # next entry to be skipped!
                    # buckets.pop(j)
            buckets = list(filter(lambda x:len(x)<=2,buckets))
            
        # Handling the buckets remaining after last cycle - if the longest
        # list is at the end of the list then it is not counted

        for i, bucket in enumerate(buckets):
            curr = sum(list(dict(bucket).values())[:2])
            if curr > max: max = curr

        # and returning the result
        return max






testcases = [
    [1,0,1,4,1,4,1,2,3],
    [3,3,3,1,2,1,1,2,3,3,4],
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
    [0,1,3]*100000 ,
]


s = Solution()

for c in testcases:
    print("Testcase input: ",end='')
    if len(c) > 10:
        print(c[:10],"...")
    else:
        print(c)
    print("Output: ",end='')
    print(s.totalFruit(c))


#print("TimeIt session")
#starttime = timeit.default_timer()
#out = s.totalFruit([0,1]*100000 + [5,6])

#print( "Time diff is ", timeit.default_timer() -starttime )