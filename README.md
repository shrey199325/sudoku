# SUDOKU
This is a Flask based SUDOKU puzzle solver. It performs three operations:
1. Provides a default Sudoku puzzle.
1. Lets the users add a new Sudoku puzzle.
1. Solves the current Sudoku puzzle.

Resource Method Table for the API is as follows:

PATH | METHOD | DESCRIPTION | PARAMETERS | STATUS CODE(S)
--- | --- | ---| --- | ---
/ | GET | Homepage requested by the browser with default sudoku problem. | None | 200 OK
/ | POST | A new sudoku puzzle to be added by user request. Recognized by the method value `set`. | `sudoku_str`(string), `method`(string) | 200 OK, 301 INVALID_SUDOKU_METHOD, 302 INVALID_SUDOKU_SEQUENCE 
/ | POST | Solve the sudoku puzzle as requested by the user. Recognized by the method value `solve`. | `sudoku_str`(string), `method`(string) | 200 OK, 301 INVALID_SUDOKU_METHOD, 302 INVALID_SUDOKU_SEQUENCE 

**Rules**:
1. The puzzles (grids) are configured as read-only.
1. `Add new` and `Solve` buttons can be used to add a new puzzle or get the solution of the existing one.
1. Left grid shows the puzzle in its initial state.
1. The right grid would be empty initially but it would be filled with the solution of the puzzle (if the puzzle can be solved) in the left grid once `Solve` button is clicked.
1. If a new puzzle is added then the string passed should only contain numbers **`[1-9]`** and **`.`** to represent empty cells in the grid.
1. If the puzzle cannot be solved, an alert would be displayed on the browser and the user would be redirected to the homepage.

**Screenshots**:

* 
    ![First Page](/images/1.%20First%20page.PNG) 
* 
    ![First Page Solution](/images/2.%20First%20Page%20Solution.PNG) 
* 
    ![Add new puzzle](/images/3.%20Add%20new.PNG)
* 
    ![Incorrect Input](/images/4.%20Adding%20incorrect%20input.PNG) 
* 
    ![Adding the hardest sudoku puzzle](/images/5.%20Adding%20the%20hardest%20puzzle.PNG)
* 
    ![New Puzzle Added](/images/6.%20New%20puzzle%20added.PNG) 
* 
    ![Hardest sudoku puzzle solved](/images/7.%20Hardest%20sudoku%20puzzle%20solved.PNG)


**Tests**:

Used UNITTEST framework to add testcases. Below is the code coverage report:

Name | Statements | Missed | Covered
--- | --- | --- | --- 
__init__.py | 0 | 0 | 100%
app.py | 31 | 1 | 97%
src\__init__.py | 0 | 0 | 100%
src\sudoku_solver.py | 82 | 1 | 99%
tests\tests.py | 70 | 1 | 99%
**TOTAL** | **183** | **3** | **98%**

The complete code coverage is present [here](/CodeCoverage/index.html).


**Setup**:

* With Docker:
Make sure that docker and docker-compose is installed on the system. Move to the project directory (default: `sudoku`) and run the below command:

    `docker-compose build; docker-compose up`

* Without Docker:
Make sure python 3.x is installed in the system. Latest version 3.8 is preferable. Move to the project directory (default: `sudoku`) and run the below command:

    `pip install -r requirements.txt; python app.py`
    
In both the cases, the page can be accessed at `http://localhost:5000` from the local system.