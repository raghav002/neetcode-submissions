class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m x n 2d matrix
        # integer
        # within m rows -> non-decreasing
        # 1st element of nth row greater than mth element of n-1th row
        # return true if target in soln 
        # what if we do a double binary search
        for i in range(len(matrix)):
            row = matrix[i]
            il = 0
            ir = len(matrix[0])-1
            found = self.innerbSearch(row, target, il, ir)
            if found==True:
                return True
                break
        return found

    def innerbSearch(self, mlist, target, l, r):
        if l>r:
            return False
        mid = (l+r)//2
        if mlist[mid]==target:
            return True
        elif mlist[mid]<target:
            return self.innerbSearch(mlist, target, mid+1, r)
        else:
            return self.innerbSearch(mlist, target, l, mid-1)

