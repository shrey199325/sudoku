from datetime import datetime, timedelta

EMPTY_ENTRY = 0
DEFAULT_STR = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
# 2.....9..6..25..13.53..876........7452.417.8687........625..83.19..76..5..5.....7
global_timeout = None


class Sudoku:
    def __init__(self, board=None):
        if board is None:
            board = DEFAULT_STR
        self.board = self.convert_sudoku(board)
        self.totalBands, self.totalStacks = len(self.board), len(self.board[0])
        self.subGridSize = int(self.totalBands ** 0.5)
        self.allowedRange = range(1, self.totalBands + 1)

    def sudoku_solution(self):
        global global_timeout
        try:
            start_time = datetime.now()
            global_timeout = start_time + timedelta(seconds=5)
            sudoku_solved = self.can_solve_sudoku_from_cell(0, 0)
            end_time = datetime.now()
        except TimeoutError:
            return timedelta(seconds=5), False
        return (end_time - start_time), sudoku_solved

    @staticmethod
    def convert_sudoku(board):
        sudoku_board, temp = [], []
        for index, i in enumerate(board):
            if index != 0 and index % 9 == 0:
                sudoku_board.append(temp)
                temp = []
            if i != ".":
                temp.append(int(i))
            else:
                temp.append(0)
        sudoku_board.append(temp)
        return sudoku_board

    def template_printable(self):
        temp = []
        for i in range(self.totalBands):
            temp.append(list(self.board[i]))
            for j in range(self.totalStacks):
                if temp[i][j] == 0:
                    temp[i][j] = ""
        return temp

    def can_solve_sudoku_from_cell(self, row, col):
        global global_timeout
        if datetime.now() > global_timeout:
            raise TimeoutError
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
