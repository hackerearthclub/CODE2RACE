package main

import "fmt"

func main() {
	// - input number of iteration
	I := 0
	fmt.Scanf("%d", &I)
	for i := 0; i < I; i++ {
		fmt.Printf("Iteration#%d\n", i+1)
		N := 0
		arr := []int{}
		fmt.Scanf("%d", &N)

		// - input number to check
		for j := 0; j < N; j++ {
			tmp := 0
			fmt.Scanf("%d", &tmp)
			arr = append(arr, tmp)
		}
		// - print out result
		res := divBy2(arr)
		fmt.Printf("Output#%d: %d\n\n", (i + 1), res)
	}

}

func divBy2(arr []int) (counter int) {
	for i := 0; i < len(arr); i++ {
		if arr[i]%2 == 0 {
			counter++
		}
	}

	return
}
