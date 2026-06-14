from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for row in board:
            seen = set()

            for value in row:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check columns
        for col in range(9):
            seen = set()

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        # Check 3 x 3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()

                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        value = board[k][l]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True