class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for y in range(9):
            for x in range(9):
                num = board[y][x]
                if num == ".":
                    continue
                
                if num in rows[y]:
                    return False
                rows[y].add(num)

                if num in cols[x]:
                    return False
                cols[x].add(num)

                grid_indx = (y // 3) * 3 + x // 3
                if num in grids[grid_indx]:
                    return False
                grids[grid_indx].add(num)
        return True