#Runtime: 124 ms, faster than 43.27% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
#Memory Usage: 15.2 MB, less than 45.71% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for _,i in enumerate(grid):
            for _,j in enumerate(i[::-1]):
                if j>-1:
                    break
                else:
                    count+=1
        return count
