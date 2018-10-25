REF: href="https://github.com/hackerearthclub/CODE2RACE/blob/master/ASSIGNMENTS/reverse-word.md">reverse-word.md

function reverseWord(word) {
  let arr = word.split(' ');
  let reversed = arr.reverse(); 
  return reversed.join(' ');
}

console.log(reverseWord("My name is Michele"));
