

const decodeASCII = (array=[]) => {
    if( !Array.isArray(array) ) return false
    return array.reduce( (str='', charASCII) => str + String.fromCharCode(charASCII) , '' )
}

const encodeASCII = (wording='') => {
    if( typeof wording !== "string" ) return false
    return [...wording].map( (str) => str.charCodeAt(0) )
}

console.log( encodeASCII('GALLERIA') )
console.log( decodeASCII( [ 71, 65, 76, 76, 69, 82, 73, 65 ] ) )