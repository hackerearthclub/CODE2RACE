package main

import "fmt"
import "strconv"
import "io/ioutil"
import "strings"
import "os"

func main() {
    inputStrings := os.Args[1:]
    if (len(inputStrings) != 1) {
        fmt.Println("Please provide a single command line argument for the path to the test file")
        return
    }

    nums, _ := readFile(inputStrings[0])

    for i := range(nums) {
        //Skip the first case as this is total test cases
        if (i == 0) {
            continue
        }
        //Calculate the factorial
        fac := calcFactorial(nums[i])
        numString := strconv.Itoa(fac)
        sum := 0
        for j := range(numString) {
            thisNum, _ := strconv.Atoi(string(numString[j]))
            sum += thisNum
        }
        fmt.Println(sum)

    }

}

//Function for reading in from the file
func readFile(fname string) (nums []int, err error) {
    b, err := ioutil.ReadFile(fname)
    if err != nil {
        return nil, err
    }

    //Split on new line
    lines := strings.Split(string(b), "\n")
    // Assign cap to avoid resize on every append.
    nums = make([]int, 0, len(lines))

    for _, l := range lines {
        // Empty line occurs at the end of the file when we use Split.
        if len(l) == 0 { continue }
        // Atoi better suits the job when we know exactly what we're dealing
        // with. Scanf is the more general option.
        n, err := strconv.Atoi(l)
        if err != nil { return nil, err }
        nums = append(nums, n)
    }

    return nums, nil
}

//Function for calculating the factorial
func calcFactorial(num int) (fac int){
    fac = 1
    for i := 0; i < num; i++ {
        fac *= (num - i)
    }
    return fac
}
