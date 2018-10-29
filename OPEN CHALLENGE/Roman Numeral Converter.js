function convert(num) {

  var converted = '';
  var roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  var numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];

    for(var i = 0; i < roman.length; i++){
      while(num >= numbers[i]){
        converted += roman[i];
        num -= numbers[i];
      }
    }
    console.log(converted);
    return converted;

}

convert(3200)
