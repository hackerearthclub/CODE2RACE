// This code was written by Quino Terrasa (@espetro)
// for the 2018 Hacktoberfest BCN challenge

/**
 * Writes an octal number as decimal.
 * Currently, only octal integrals are accepted
 * @param   {integer} oct A number written in octal format 
 * @returns {integer} dec A number written in octal format 
 */
const octalToDecimal = (oct) => {
    return (oct+"").split('')
                .reverse()
                .map(x => parseInt(x))
                .reduce((acc,curr,idx) => acc + (curr * 8**idx));
}


/**
 * Writes a decimal number as an octal. Currently only supports
 * integral input.
 * @param   {integer} dec A number written in decimal format
 * @returns {integer} oct A number written in octal format
 */
const decimalToOctal = (dec) => {
    let lgth = (dec + "").length,
        res  = [],
        curr = dec;

    while(lgth >= 0) {
        res.push(Math.floor(curr / (8**lgth)));
        curr = curr % (8**lgth);
        lgth -= 1;
    }

    let int = parseInt(res.map(x => x+"").join(''));
    // var float = ("0").split('').map(x => parseInt(x)).reduce((acc,curr,idx) => acc + curr);

    return int;
}