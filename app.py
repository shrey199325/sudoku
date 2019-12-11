from flask import Flask, jsonify, request, render_template
from src.sudoku_solver import Sudoku

app = Flask(__name__, template_folder='template')
# Status Codes #
OK = 200
INVALID_SUDOKU_METHOD = 301
INVALID_SUDOKU_SEQUENCE = 302
#


@app.route("/", methods=["GET", "POST"])
def get_sudoku():
    """
    Accepts GET and POST requests from the browser as Content-type JSON :
    GET: The default request by the browser which should return default puzzle.
    POST: There can be two POST requests:
          1. Set a given new puzzle.
          2. Solve the current puzzle.
    Returns the HTML template with respective data.
    """
    if request.method == "GET":
        sudoku_obj = Sudoku()
        sudoku_ans = Sudoku("." * 81)
        return render_template("sudoku.html", status="passed",
                               cell=sudoku_obj.template_printable(),
                               cell_ans=sudoku_ans.template_printable(),
                               time_taken="0 seconds")
    else:
        posted_data = request.get_json()
        sudoku_str = posted_data["sudoku_str"]
        method_invoked = posted_data["method"]
        if not Sudoku.validator(sudoku_str):
            return jsonify({"status": INVALID_SUDOKU_SEQUENCE,
                            "message": "Invalid Sudoku sequence given"})
        sudoku_obj = Sudoku(sudoku_str)
        if method_invoked.lower() == "set":
            sudoku_ans = Sudoku("." * 81)
            return render_template("sudoku.html", status="passed",
                                   cell=sudoku_obj.template_printable(),
                                   cell_ans=sudoku_ans.template_printable(),
                                   time_taken="0 seconds")
        elif method_invoked.lower() == "solve":
            sudoku_ans = Sudoku(sudoku_str)
            time_taken, is_sudoku_solved = sudoku_ans.sudoku_solution()
            time_taken = f"{str(time_taken.total_seconds())} seconds"
            if is_sudoku_solved:
                return render_template("sudoku.html", status="passed",
                                       cell=sudoku_obj.template_printable(),
                                       cell_ans=sudoku_ans.template_printable(),
                                       time_taken=time_taken)
            else:
                return render_template("sudoku.html", status="failed",
                                       cell=sudoku_obj.template_printable(),
                                       cell_ans=Sudoku("." * 81).template_printable(),
                                       time_taken=time_taken)
        else:
            return jsonify({"status": INVALID_SUDOKU_METHOD,
                            "message": "Unrecognised Method Name given"})


if __name__ == "__main__":
    app.run(host="0.0.0.0")
