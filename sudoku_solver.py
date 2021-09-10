from collections import defaultdict
import time
class Solution(object):
    def isValidMove(self,board, i,j,num):
        if any (board[i][y]==num for y in range(9)):return False
        if any (board[x][j]==num for x in range(9)):return False
        if any (board[x][y]==num for x in range(i//3*3,i//3*3+3) for y in range(j//3*3,j//3*3+3)):return False
        return True
    def solve(self, board, i, j):
        while (board[i][j]!='.'):
            j+=1
            if j==9:
                j=0
                i+=1
            if i==9:
                return True
        for k in range(1,10):
            if self.isValidMove(board, i, j,str(k)):
                board[i][j]=str(k)
                if self.solve(board,i,j):
                    return True
        board[i][j]='.'
        return False
            
    def solveSudoku(self, board):
        self.solve(board,0,0)
        for i in range(len(board)):
            print(board[i])



c=Solution()
c.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])


        