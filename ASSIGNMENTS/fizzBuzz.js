 function fizzBuzz(n) {
    if (n % 3 === 0 && n % 5 === 0) {
      console.log('FizzBuzz')
    } else {
      if (n % 5 === 0) {
        console.log('Buzz')
      }
      else {
        if (n % 3 === 0) {
          console.log('Fizz')
        }
      }
    }
  }
