package main

import "fmt"

func main() {
	I := 0
	fmt.Scanf("%d", &I)
	for i := 0; i < I; i++ {
		fmt.Printf("Iteration#%d\n", i+1)
		N := 0
		fmt.Scanf("%d", &N)

		for n := 1; n <= N; n++ {
			if n%3 == 0 && n%5 == 0 {
				fmt.Println("FizzBuzz")
			} else if n%3 == 0 {
				fmt.Println("Fizz")
			} else if n%5 == 0 {
				fmt.Println("Buzz")
			} else {
				fmt.Println(n)
			}
		}
	}

}
