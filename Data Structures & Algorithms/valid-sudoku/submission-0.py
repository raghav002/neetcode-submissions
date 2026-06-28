class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def boxer(board, startrow, startcol):
            check = [0]*9
            for i in range(3):
                row = startrow + i
                for j in range(3):
                    col = startcol + j
                    num = board[row][col]
                    if num==".":
                        continue
                    check[int(num)-1] += 1
                    if check[int(num)-1]>1:
                        return False
            return True
        # Rows (brute force)
        check = [0]*9
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                check[int(num)-1]+=1
                if check[int(num)-1]>1:
                    return False
            check = [0]*9
        for i in range(9):
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                check[int(num)-1]+=1
                if check[int(num)-1]>1:
                    return False
            check = [0]*9
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not boxer(board, i, j):
                    return False
        return True