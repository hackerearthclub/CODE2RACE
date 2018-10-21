const ACIIIproduct = (wording: string = ''): number => {
    return [...wording].reduce((sum: number, str: string) => sum * str.charCodeAt(0), 1)
}

console.log( ACIIIproduct('IS') )
console.log( ACIIIproduct('GfG') )
