from app import app
import unittest
import os

BASE_PATH = os.path.join(os.path.dirname(__file__), "test_templates")


class TestFlask(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_base(self):
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template1.html")) as fd:
            compare_txt = fd.read()
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_post_set(self):
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template2.html")) as fd:
            compare_txt = fd.read()
        req = "2.....9..6..25..13.53..876........7452.417.8687........625..83.19..76..5..5.....7"
        request = {
            "sudoku_str": req,
            "method": "set"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_post_solve(self):
        compare_txt = None
        with open(os.path.join(BASE_PATH, "test_template3.html")) as fd:
            compare_txt = fd.read()
        req = "2.....9..6..25..13.53..876........7452.417.8687........625..83.19..76..5..5.....7"
        request = {
            "sudoku_str": req,
            "method": "solve"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)

    def test_invalid_post_method(self):
        compare_txt = '{"message":"Unrecognised Method Name given","status":301}\n'
        req = "2.....9..6..25..13.53..876........7452.417.8687........625..83.19..76..5..5.....7"
        request = {
            "sudoku_str": req,
            "method": "solveabc"
        }
        response = self.app.post("/",
                                 json=request,
                                 follow_redirects=True)
        self.assertEqual(bytes(compare_txt, 'utf-8'), response.data)


if __name__ == "__main__":
    unittest.main()