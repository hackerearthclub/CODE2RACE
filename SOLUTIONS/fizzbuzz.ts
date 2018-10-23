function fizzBuzz(n: number) {
    let result = '';

    if (!(n % 3)) {
        result += 'Fizz';
    } else if (!(n % 5)) {
        result += 'Buzz';
    }

    console.log(result);
  }