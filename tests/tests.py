from app import app
import os
from datetime import timedelta
from src.sudoku_solver import DEFAULT_STR
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
    def test_post_solve(self, mock_timing_delta):
        mock_timing_delta.return_value = timedelta(seconds=1)
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template3.html")) as fd:
            compare_txt = fd.read()
        request = {
            "sudoku_str": SUDOKU_PUZZLE,
            "method": "solve"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_invalid_post_method(self):
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