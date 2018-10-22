package main

import "fmt"
import "os"
import "strconv"
import "math"

func main() {
    inputArgs := os.Args[1:]
    flag := inputArgs[0]
    number := inputArgs[1]

    //Decide on which conversion to make
    if (flag == "1") {
        decimalToOctal(number)
    } else if (flag == "0") {
        octalToDecimal(number)
    } else {
        fmt.Println("Please provide a valid flag - 0 for Octal -> Decimal and 1 for Decimal -> Octal")
    }
}

func octalToDecimal(octal string) {
    //Convert using mathematical method
    total := 0;
    for i, digit := range(octal) {
        digitInt, _ := strconv.Atoi(string(digit))
        total += digitInt * int(math.Pow(8, float64((len(octal) - 1 - i))))
    }
    fmt.Println(total)
}

func decimalToOctal(decimal string) {
    //Convert using divison remainder method
    decimalInt, _ := strconv.Atoi(string(decimal))
    result := ""
    //What is a better way to do this?
    for flag := 1; flag > 0; flag++ {
        quotient := decimalInt / 8
        remainder := decimalInt % 8
        if (quotient == 0) {
            flag = -1
        }
        //Set the new total and append on the remainder
        decimalInt = quotient
        result = strconv.Itoa(remainder) + result
    }
    fmt.Println(result)

}
