package main

import "fmt"
import "os"

func main() {
    inputStrings := os.Args[1:]
    if (len(inputStrings) != 1) {
        fmt.Println("Two many strings provided. Please provide a single string")
        return
    }

    providedString := inputStrings[0]
    product := 1
    for i := range(providedString) {
        product = product * int((providedString[i]))
    }
    fmt.Println(product)
}
