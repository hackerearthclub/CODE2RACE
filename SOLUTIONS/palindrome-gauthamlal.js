let palindrome = word => {
  for (let i = 0, j = word.length - 1; i <=j; i++, j--) {
    if(word[i] !== word[j]) {
      return false;
    }
  }
  return true;
}

let word = 'malayalam';

if (palindrome(word.toLowerCase())) {
  console.log(`${word} is a palindrome`);
} else {
  console.log(`${word} is not a palindrome`);
}
