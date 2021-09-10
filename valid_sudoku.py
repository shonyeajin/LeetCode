from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        colset=defaultdict(set)
        rowset=defaultdict(set)
        subset=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in colset[j] or board[i][j] in rowset[i] or board[i][j] in subset[(i//3,j//3)]:
                    return False
                colset[j].add(board[i][j])
                rowset[i].add(board[i][j])
                subset[(i//3,j//3)].add(board[i][j])
        return True

c=Solution()
ans=c.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]])
print(ans)