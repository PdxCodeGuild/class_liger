let name_input = document.querySelector('#name_input');
let run_bt = document.querySelector('#run_bt');
let output_div = document.querySelector('#output_div');
run_bt.onclick = function() {
  let name = name_input.value;
  //alert(name);
  output_div.innerText = 'Hello, ' + name + '!';
  //output_div.innerHTML = '<b>Hello, ' + name + '!</b>';
  console.log(output_div)
  console.log(output_div.innerText)
}
