let x = function HelloWorld(Name?) {
    let hellow = "Hello World "
    Name ? hellow+=` ${Name}`:""
    return hellow
}

console.log(x())