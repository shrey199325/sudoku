from app import app
import os
from datetime import timedelta
from src.sudoku_solver import DEFAULT_STR, Sudoku
import unittest
from unittest.mock import patch

BASE_PATH = os.path.join(os.path.dirname(__file__), "test_templates")
SUDOKU_PUZZLE = "8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4.."


class TestFlask(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        app.config["TESTING"] = False
        self.app = None

    @patch("src.sudoku_solver.Sudoku.timing_delta")
    def test_base(self, mock_timing_delta):
        """
        Checks the default puzzle rendered by the homepage and then
        checks for the solution of that puzzle by comparing rendered
        HTML files.
        """
        mock_timing_delta.return_value = timedelta(seconds=1)
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template1.html")) as fd:
            compare_txt = fd.read()
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

        with open(os.path.join(BASE_PATH, "test_template_default.html")) as fd:
            compare_txt = fd.read()
        request = {
            "sudoku_str": DEFAULT_STR,
            "method": "solve"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_post_set(self):
        """
        Checks POST request to add a new puzzle.
        """
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template2.html")) as fd:
            compare_txt = fd.read()
        request = {
            "sudoku_str": SUDOKU_PUZZLE,
            "method": "set"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    @patch("src.sudoku_solver.Sudoku.timing_delta")
    def test_sudoku_solver_instance(self, mock_timing_delta):
        """
        Tests the sudoku_solver module.
        """
        mock_timing_delta.return_value = timedelta(seconds=1)
        puzzle = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
        solution = [[5,3,4,6,7,8,9,1,2], [6,7,2,1,9,5,3,4,8], [1,9,8,3,4,2,5,6,7],
                    [8,5,9,7,6,1,4,2,3], [4,2,6,8,5,3,7,9,1], [7,1,3,9,2,4,8,5,6],
                    [9,6,1,5,3,7,2,8,4], [2,8,7,4,1,9,6,3,5], [3,4,5,2,8,6,1,7,9]]
        sudoku_object = Sudoku(puzzle)
        sudoku_object.sudoku_solution()
        self.assertEqual(sudoku_object.board, solution)

    def test_invalid_post_method(self):
        """
        Checks the response in case the method in the request is invalid.
        """
        compare_txt = '{"message":"Unrecognised Method Name given","status":301}\n'
        request = {
            "sudoku_str": SUDOKU_PUZZLE,
            "method": "solveabc"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_invalid_post_str(self):
        """
        Checks the response if invalid sudoku string is POSTed.
        """
        compare_txt = '{"message":"Invalid Sudoku sequence given","status":302}\n'
        request = {
            "sudoku_str": SUDOKU_PUZZLE[:-2],
            "method": "solve"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    @patch("src.sudoku_solver.Sudoku.timing_delta")
    def test_post_unsolvable(self, mock_timing_delta):
        """
        Checks the response of the module when an unsolvable puzzle
        is POSTed.
        """
        mock_timing_delta.return_value = timedelta(seconds=5)
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template_unsolvable.html")) as fd:
            compare_txt = fd.read()
        request = {
            "sudoku_str": SUDOKU_PUZZLE[:-1] + "1",
            "method": "solve"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)


if __name__ == "__main__":
    unittest.main()