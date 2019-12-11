var button_new = document.getElementById("new");
var button_solve = document.getElementById("solve");
var temp = null;


button_new.addEventListener('click', async _ => {
  try {
  var sudoku_str = "";
  var prompt_str = "Please enter sudoku numbers";
    while(sudoku_str!=null){
      sudoku_str = prompt(prompt_str, sudoku_str);
      var pattern = /[1-9.]/g;
      sudoku_str = sudoku_str.match(pattern);
      sudoku_str = sudoku_str.join("");
      if (sudoku_str.length==81){
        break;
  } else{
    prompt_str = "Length should be equal to 81. Current length"+ sudoku_str.length.toString() +"Please enter sudoku numbers.";
  };
  };
  var response = await fetch(window.location.href, {
      method: 'post',
      headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "method": "set",
        "sudoku_str": sudoku_str
      })
    }).then(function(response) {
    return response.text();
}).then(function(string) {
    console.log(string);
    document.body.innerHTML = "";
    document.write(string);
});
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});

button_solve.addEventListener('click', async _ => {
  try {
    var sudoku_str = "";
    for (i of document.getElementsByTagName("tr")) {
        for (j of i.getElementsByTagName("input")){
            if (j.value==="") {
                sudoku_str = sudoku_str + ".";
            } else {
                sudoku_str = sudoku_str + j.value;
            };
        }
    };
    var response = await fetch(window.location.href, {
      method: 'post',
      headers: {
      "Content-Type":"application/json"
      },
      body: JSON.stringify({
        "method": "solve",
        "sudoku_str": sudoku_str
      })
    }).then(function(response) {
    return response.text();
}).then(function(string) {
    console.log(string);
    if (string.includes("failed")) {
        alert("This sudoku cannot be solved");
        window.location.pathname = "/";
    } else {
    document.body.innerHTML = "";
    document.write(string);
    };
});
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});
