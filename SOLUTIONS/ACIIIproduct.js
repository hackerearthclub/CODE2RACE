const ACIIIproduct = (wording='') => {
    return [...wording].reduce( (sum, str) => sum * str.charCodeAt(0) , 1 )
}

console.log( ACIIIproduct('IS') )
console.log( ACIIIproduct('GfG') )
