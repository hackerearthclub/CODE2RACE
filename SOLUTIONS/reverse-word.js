function reverse_word(input) {
    let words = input.split(' ');
    let reverse_word = words.reverse();
    let word = reverse_word[0];
    for (let index = 1; index < reverse_word.length; index++) {
        word = word + ' ' + reverse_word[index];        
    }
    console.log(word); 
}

//reverse_word('My name is Michele')
//Michele is name My