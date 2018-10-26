let reversedWord = function reverse(word){
  let splitWord = word.split(' ')
  let reversed = [];
  for (let i = 0; i<=splitWord.length; i++){
      reversed.unshift(splitWord[i]);
  }
  console.log(reversed.join(' '))
}
reversedWord('My name is Michele')  // Michelle is name My





