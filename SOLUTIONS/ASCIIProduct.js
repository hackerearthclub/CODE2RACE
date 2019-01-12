function product_ascii(input) {
    let product = input.charCodeAt(0);
    for (let index = 1; index < input.length; index++) {
        product = product * input.charCodeAt(index);
    }
    console.log(product);
}


//product_ascii("IS")
//6059
//product_ascii("GfG")
//514182