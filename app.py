from flask import Flask, jsonify, request, render_template, Response
from src.sudoku_solver import Sudoku
import json

app = Flask(__name__, template_folder='template')
# Status Codes #
OK = 200
INVALID_SUDOKU_METHOD = 301
INCOMPLETE_INFO = 302
#


@app.route("/", methods=["GET","POST"])
def get_sudoku():
    print("14")
    if request.method == "GET":

        sudoku_obj = Sudoku()
        return render_template("sudoku.html", status="passed",
                               cell=sudoku_obj.template_printable(),
                               time_taken="0 seconds")
    else:
        posted_data = request.get_json()
        print(posted_data)
        sudoku_str = posted_data["sudoku_str"]
        method_invoked = posted_data["method"]
        print(sudoku_str, method_invoked)
        if method_invoked.lower() == "set":
            print("29")
            sudoku_obj = Sudoku(sudoku_str)
            return render_template("sudoku.html", status="passed",
                                   cell=sudoku_obj.template_printable(),
                                   time_taken="0 seconds")
        elif method_invoked.lower() == "solve":
            print("34")
            sudoku_obj = Sudoku(sudoku_str)
            time_taken, is_sudoku_solved = sudoku_obj.sudoku_solution()
            time_taken = f"{str(time_taken.total_seconds())} seconds"
            if is_sudoku_solved:
                return render_template("sudoku.html", status="passed",
                                       cell=sudoku_obj.template_printable(),
                                       time_taken=time_taken)
            else:
                return render_template("sudoku.html", status="failed",
                                       cell=sudoku_obj.template_printable(),
                                       time_taken=time_taken)
        else:
            return jsonify({"status": INVALID_SUDOKU_METHOD,
                            "message": "Unrecognised Method Name given"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
