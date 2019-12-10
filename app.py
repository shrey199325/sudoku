from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='template')
# api = Api(app)
# Status Codes #
OK = 200
INVALID_SUDOKU = 301
INCOMPLETE_INFO = 302
#


@app.route("/")
def get_sudoku():
    # posted_data = request.body
    # ret_json = {
    #     "status": OK, "msg": "Successfully signed in",
    #     "data": posted_data
    # }
    data = [["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""]]
    print(data)
    return render_template("sudoku.html", cell=data, time_taken=0)


# api.add_resource(SudokuSolver, "/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
