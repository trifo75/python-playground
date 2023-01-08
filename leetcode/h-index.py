# %%

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        
        h = 0
        citations.sort(reverse=True)
        for i,cit in enumerate(citations):
            if cit > i:
                h = i + 1 
            else:
                break

        return h
        



sample = [3,0,6,1,5]
sample = [0]
s = Solution()
print(s.hIndex(sample))

# %%
