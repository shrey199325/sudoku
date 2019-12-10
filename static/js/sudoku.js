window.addEventListener('load', function () {
  alert("It's loaded!")

var button = $("div.form > button#new");

button.addEventListener('click', async _ => {
  try {
    var response = await fetch(window.location.href, {
      method: 'post',
      body: {
        "sudoku_str": "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});

});