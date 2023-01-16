class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        ins_lo = newInterval[0]
        ins_hi = newInterval[1]
        index_lo = None
        index_hi = None

        for i, item in enumerate(intervals):
            if (index_lo == None) and (item[0] <= ins_lo <= item[1]):
                index_lo = i

            if (index_hi == None) and (item[0] <= ins_hi <= item[1]):
                index_hi = i

        intervals[index_lo][1] = intervals[index_hi][1]
        for i in range(index_lo+1,index_hi+1):
            intervals.pop(index_lo+1)

        return intervals
            
        print("Index lo: {}, index hi: {}".format(index_lo,index_hi))            
        #print("Low: {}, high: {}".format(ins_lo,ins_hi))


        


s = Solution()

testcases = [
    {
        'input_interval': [[1,2],[3,5],[6,7],[8,10],[12,16]],
        'insert_interval': [4,8]
    },
    {
        'input_interval': [[1,3],[6,9]],
        'insert_interval': [2,5]
    },

]

for i, testcase in enumerate(testcases):
    print("Teszt {}: bemeneti lista: {}, beszúrandó: {}"\
        .format(i,testcase['input_interval'],testcase['insert_interval']))
    print(s.insert(testcase['input_interval'],testcase['insert_interval']))

""" 
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]. 
"""