from datetime import datetime

EMPTY_ENTRY: int = 0


class Sudoku:
    def __init__(self, board):
        self.board = self.convert_sudoku(board)
        self.totalBands, self.totalStacks = len(self.board), len(self.board[0])
        self.subGridSize = int(self.totalBands ** 0.5)
        self.allowedRange = range(1, self.totalBands + 1)

    def sudoku_solution(self):
        start_time = datetime.now()
        sudoku_solved = self.can_solve_sudoku_from_cell(0, 0)
        end_time = datetime.now()
        return (end_time - start_time), sudoku_solved

    def convert_sudoku(self, board):
        if isinstance(self, self.__class__):
            print(True)
        return board

    def can_solve_sudoku_from_cell(self, row, col):
        if col == self.totalStacks:
            col, row = 0, row + 1
            if row == self.totalBands:
                return True
        if self.board[row][col] != EMPTY_ENTRY:
            return self.can_solve_sudoku_from_cell(row, col + 1)
        for value in self.allowedRange:
            if self.can_place_value(row, col, value):
                self.board[row][col] = value
                if self.can_solve_sudoku_from_cell(row, col + 1):
                    return True
            self.board[row][col] = EMPTY_ENTRY
        return False

    def can_place_value(self, row, col, value_to_place):
        if value_to_place in self.board[row]:
            return False
        for row_num in range(self.totalStacks):
            if value_to_place == self.board[row_num][col]:
                return False
        if self.value_present_in_sub_grid(row, col, value_to_place):
            return False
        return True

    def value_present_in_sub_grid(self, row, col, value_to_place):
        vertical_grid_index, hor_grid_index = (row // self.subGridSize,
                                               col // self.subGridSize)
        top_left_row, top_left_col = (self.subGridSize * vertical_grid_index,
                                      self.subGridSize * hor_grid_index)
        for inc_row in range(self.subGridSize):
            for inc_col in range(self.subGridSize):
                if value_to_place == self.board[top_left_row + inc_row][top_left_col + inc_col]:
                    return True
        return False
