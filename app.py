from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
# Status Codes #
OK = 200
INVALID_SUDOKU = 301
INCOMPLETE_INFO = 302
#


class SudokuSolver(Resource):
    def post(self):
        posted_data = request.get_json()
        ret_json = {
            "status": OK, "msg": "Successfully signed in",
            "data": posted_data
        }
        return jsonify(ret_json)


api.add_resource(SudokuSolver, "/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
