# collections.defaultdict(set) -> Refer to DSA-from-the-Start/Important Concepts/DefaultDict.py

# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        square = collections.defaultdict(set) 
        # Each row or column divided by 3 (only in integer part) tells the square it is part of
        # For example (8,7) -> (8//3,7//3) -> (2,2) -> Last box

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if (board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[(r//3,c//3)]):
                    return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])

        return True