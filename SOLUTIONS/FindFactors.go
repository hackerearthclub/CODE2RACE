package main

import (
	"fmt"
)

func main() {
	fmt.Print(FindFactors(36));

}

func FindFactors(number int) []int{
	var factors []int
	i := 1
	for i = 1; i<int(number/2); i++ {
		if int(number) % int(i) == 0 {
			factors = append(factors, i)
		}
	}
	return factors
}

