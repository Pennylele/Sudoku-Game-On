class Solver:
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def unassigned(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == "":
                    return i, j
        return -1, -1

    def validate(self, i, j, e):
        rowvalid = all([e != self.board[i][x] for x in range(9)])
        if rowvalid:
            colvalid = all([e != self.board[y][j] for y in range(9)])
            if colvalid:
                rowbox, colbox = 3 * (i // 3), 3 * (j // 3)
                for m in range(rowbox, rowbox + 3):
                    for n in range(colbox, colbox + 3):
                        if self.board[m][n] == e:
                            return False
                return True
        return False

    def solve(self):
        i, j = self.unassigned()
        if i == j == -1:
            return True
        for n in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.validate(i, j, n):
                self.board[i][j] = n
                if self.solve():
                    return True
                self.board[i][j] = ""
        return False

