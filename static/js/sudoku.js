
var button_new = document.getElementById("new");
var button_solve = document.getElementById("solve");

button_new.addEventListener('click', async _ => {
  try {
    var response = await fetch(window.location.href, {
      method: 'post',
      json: {
        "method": "set",
        "sudoku_str": "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});

button_solve.addEventListener('click', async _ => {
  try {
    var response = await fetch(window.location.href, {
      method: 'post',
      json: {
        "method": "solve",
        "sudoku_str": "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});

