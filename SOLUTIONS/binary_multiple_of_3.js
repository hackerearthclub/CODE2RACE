// run it with node.js
'use strict';
let readline = require('readline');

// solution to the problem
function isBinaryDivisibleBy3 (bNumber) {
  let value = parseInt(bNumber,2)
  return value % 3 === 0 && value >=3 ? 1 : 0
}

// from here is input hanling / validation
const ri = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


const params = {
  T: null,
  inputs: []
}

function processInput (line) {
  let question = 'How many test [1-100] (CTRL+C to exit)?'
  if (typeof params.T !== 'number') {
    const n = parseInt(line,10);
    if (n !== NaN && n >= 1 && n <= 100) {
      params.T = n;
      question = "Enter Binary Number #" + (params.inputs.length + 1);
    }
  } else {
    
    // binary input
    let isBinary = line.match('^[01]{1,100}$');
    if (isBinary) {
      console.log( line, ' => ', isBinaryDivisibleBy3(line))
      params.inputs.push(line);
    }
    question = "Enter Binary Number #" + (params.inputs.length + 1);
  }
  return question;
}

ri.on('line', function (line) {
  let question = processInput(line);
  if (typeof params.T === 'number' && params.T === params.inputs.length) {
    process.exit()
  } 
  console.log(question);
  ri.prompt();
})
ri.write('\n')
ri.prompt()
