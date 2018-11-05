package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println("Enter your text: ")
	reader := bufio.NewReader(os.Stdin)
	inputText, _ := reader.ReadString('\n')
	reverseString := ReverseStringSlice(strings.Split(strings.TrimRight(inputText, "\n"), " "))
	fmt.Print("You reversed text is: ", strings.Join(reverseString, " "))
}

func ReverseStringSlice(inputString []string) []string {
	lastWord := len(inputString) - 1
	for i := 0; i < len(inputString)/2; i++ {
		inputString[i], inputString[lastWord-i] = inputString[lastWord-i], inputString[i]
	}
	return append(inputString, "\n")
}
