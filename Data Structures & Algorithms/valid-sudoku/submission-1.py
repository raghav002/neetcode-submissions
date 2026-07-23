class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: 9x9 sudoku board in form of 2d array
        # output: true if sudoku is valid, otherwise false
        # constraints for 'valid' condition:
            # each row has nums 1 - 9 without dupes
            # each col has nums 1 - 9 without dupes
            # each 3 x 3 subboxes has nums 1 - 9 without dupes
                # the 'start' indices of these subboxes are as follows:
                    # 0,0 | 0,3 | 0,6
                    # 3,0 | 3,3 | 3,6
                    # 6,0 | 6,3 | 6,6

        # Key notes:
        # Every row and col has to be checked, but not the indices 'in between' excluding subboxes
        # Every subbox starting at the indices above has to be checked, but we need a proper
        # 'formula' for doing so
        # 0,0 box -> 0,0 ; 0,1 ; 0,2
                #    1,0 ; 1,1 ; 1,2
                #    2,0 ; 2,1 ; 2,2
        # 6,6 ->     6,6 ; 6,7 ; 6,8
                #    7,6 ; 7,7 ; 7,8
                #    8,6 ; 8,7 ; 8,8
        # We notice that for a starting subbox point x,x -> we check everything within the bounds of 
        # x,x to x+2, x+2

        # row checks
        for row in range(len(board)): # num rows
            seen = set()
            for col in range(len(board)):
                #print(row, col, board[row][col])
                if board[row][col] in seen and board[row][col] != ".":
                    #print(row, col, board[row][col])
                    return False
                else:
                    seen.add(board[row][col])
        
        # col checks
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                if board[row][col] in seen and board[row][col] != ".":
                    #print(row, col, board[row][col])
                    return False
                else:
                    seen.add(board[row][col])

        # subbox:
        for row in range(0, len(board), 3): # makes sure we get the right row starts
            for col in range(0, len(board), 3): # makes sure we get the right col starts
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] in seen and board[row+i][col+j] != ".":
                            print(row+i, col+j, board[row+i][col+j])
                            return False
                        else:
                            seen.add(board[row+i][col+j])

        return True