const reverseWord = word => {
  let wordArray = word.split('');
  let reverseWord = "";
  for (var i = wordArray.length - 1; i >= 0; i--) reverseWord+= wordArray[i]
  return reverseWord;
}

console.log(reverseWord('I love JS!'));
