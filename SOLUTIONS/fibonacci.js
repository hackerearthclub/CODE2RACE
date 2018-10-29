REF: https://github.com/hackerearthclub/CODE2RACE/blob/master/ASSIGNMENTS/fibonacci.md

function fib(num){
  let arr = [0, 1];
  for (let i = 2; i < num + 1; i++){
    arr.push(arr[i - 2] + arr[i -1])
  }
 return arr;
}
