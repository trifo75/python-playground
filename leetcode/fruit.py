# 904. Fruit into baskets
import timeit


class Solution_nemjo:
    def totalFruit(self, fruits: list[int]) -> int:

        # when the input list is empty, no fruit can be harvested
        if len(fruits) == 0: return 0 


        # compress "fruits" list into "fruitgroups"
        # tuples as ( fruit,  number_of_same_type_neighbors)
        prevfruit = fruits[0]
        fruitgroups=[]
        fruitcount=0

        for fruit in fruits:
            
            if fruit == prevfruit:
                fruitcount +=1
            else:
                fruitgroups.append((prevfruit,fruitcount))
                fruitcount = 1

            prevfruit = fruit

        fruitgroups.append((fruit,fruitcount))

        
        # find longest sequence of max 2 types
        max = 0
        for i in range(len(fruitgroups)):
            baskets = list()
            curr = 0

            for fruitgroup in fruitgroups[i:]:
                if not fruitgroup[0] in baskets:
                    baskets.append(fruitgroup[0])

                if len(baskets) > 2: break
                curr += fruitgroup[1]

            if curr > max:
                max = curr


        return max




    def totalFruit_nemjo(self, fruits: list[int]) -> int:
        """
        try to start from every item in input list and count number of collectable fruits
        collect fruit types in "baskets" list. break cycle when list length gets longer than 2

        """

        max = 0
        curr = 0


        for i in range(len(fruits)):

            baskets = list()
            curr = 0
            numbaskets = 0

            for fruit in fruits[i:]:
                if not fruit in baskets: 
                    baskets.append(fruit)
                    numbaskets += 1

                if numbaskets > 2: break
                curr += 1

            if curr > max:
                max = curr
                max = max + 1

        return max 

from collections import defaultdict
class Solution:



    def totalFruit(self, fruits: list[int]) -> int:

        buckets = []
        trackbuckets = []

        max = 0
        for fruit in fruits:
            if not fruit in trackbuckets:
                trackbuckets.append(fruit)
                buckets.append(defaultdict(lambda: 0))
                if len(trackbuckets) > 2:
                    trackbuckets.pop(0)

            for j, bucket in enumerate(buckets):
                buckets[j][fruit] +=1

                if len(buckets[j]) > 2:
                    curr = sum(list(dict(buckets[j]).values())[:2])
                    if curr > max: max = curr
                    buckets.pop(j)
                 
        pass


        return max 




testcases = [
    [3,3,3,1,2,1,1,2,3,3,4],
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
    [0,1]*100000 ,
]


s = Solution()

for c in testcases:
    print("Testcase input: {}".format(c))
    print("Output: ",end='')
    print(s.totalFruit(c))


print("TimeIt session")
starttime = timeit.default_timer()
out = s.totalFruit([0,1]*100000 + [5,6])

print( "Time diff is ", timeit.default_timer() -starttime )